import numpy as np
import pandas as pd
from pandas import DataFrame, Series

from utils import time_my_func
from obtain import load_file_to_db # type: ignore
from scrub import import_filter_df, get_target_df # type: ignore
from scrub import remove_zv_missings # type: ignore
from scrub import create_dummified_df # type: ignore
from scrub import clip_categorical # type: ignore
from backup import backup_df # type: ignore

path_raw = "data/raw/gravity_contact_20180406.csv"
path_clean = "data/raw/clean_contact.csv"
path_clean_db = "data/interim/clean.db"

# --- Declare Helper Objects ---

dict_replace_1 = {}
def replace_spaces(i):
    return "_".join([x.lower().strip() for x in i.split()])

def get_x_from_y():
    """
    """
    pass

# --- Declare Data Processing Functions ---

@time_my_func
def engineer_features(df):
    """
    """
    print("Scrubbing Cell Description")
    num_items_cellDescr = df['CELL_DESCRIPTION'].map(lambda i: len(str(i).split("|")))
    indexes_to_drop = \
    (num_items_cellDescr
     .where(lambda i: i != 9)
     .dropna()
     .index
     .tolist())

    df.drop(indexes_to_drop, inplace=True)

    dict_replace_cellDescr = {
        k:v for k, v in zip(
            df['CELL_DESCRIPTION'].drop_duplicates().values,
            df['CELL_DESCRIPTION'].drop_duplicates().map(lambda i: Series(i.split("|")).to_dict()).values
        )
    }

    df_cellDescr = DataFrame(df['CELL_DESCRIPTION'].map(lambda i: dict_replace_cellDescr.get(i, None)).tolist())
    df.drop('CELL_DESCRIPTION', axis=1, inplace=True)

    cols_df_cellDescr = {
        0: 'CAMPAIGN_BRAND_CDS',
        1: 'CAMPAIGN_STATUS_CDS',
        2: 'CAMPAIGN_TYPE_CDS',
        3: 'CAMPAIGN_CONTENT_1_CDS',
        4: 'CAMPAIGN_CONTENT_2_CDS',
        5: 'CAMPAIGN_CONTENT_3_CDS'
    }

    df_cellDescr.drop(range(6, 9), axis=1, inplace=True)
    df_cellDescr.rename(columns=cols_df_cellDescr, inplace=True)

    print("Creating Campaign Brand")
    if 'CAMPAIGN_BRAND' in df.columns:
        df.drop('CAMPAIGN_BRAND', axis=1, inplace=True)
    else:
        pass

    df.loc[:, 'CAMPAIGN_BRAND'] = df_cellDescr['CAMPAIGN_BRAND_CDS'].values

    print("Creating Campaign Status")
    df.loc[:, 'CAMPAIGN_STATUS'] = df_cellDescr['CAMPAIGN_STATUS_CDS'].values

    print("Creating Campaign Type")
    dict_replace_CampaignType = {
        "00": "Welcome_Email",
        "01": "Email_w_ItemRaffle",
        "02": "Event_Email_wo_Item",
        "03": "Event_Email_w_Item",
        "04": "Email_w_Pack",
        "05": "Email_w_eVoucher",
        "06": "Email_wo_Incentive",
        "07": "SMS_w_eVoucher",
        "08": "SMS_Info",
        "09": "SMS_w_REG_Code",
        "10": "Postal_Mail",
        "11": "Pack_Mail",
        "12": "Unknown",
        "13": "Postal_Mail_w_eVoucher",
        "14": "Postal_Mail_w_item",
        "15": "Postal_Mail_w_REG_Code",
        "16": "Email_w_Everything"
    }

    df.loc[:, 'CAMPAIGN_TYPE'] = \
    (df_cellDescr['CAMPAIGN_TYPE_CDS']
     .fillna('_missing_')
     .map(lambda i: str(i).zfill(2))
     .replace(dict_replace_CampaignType)
     .pipe(clip_categorical, COVERAGE=0.99)
     .values
    )

    print("Creating Campaign Content")
    dict_replace_campaign_content = {
        'Other': 'Other',
        'day_00': 'day_00',
        'ipsos': 'ipsos',
        'ipsos_panel': 'ipsos',
        'iqos_national': 'iqos_national',
        'mgm_march_transition': 'mgm',
        'mgm_spring_last_march_push': 'mgm',
        'ob01_better2018_care': 'ob01_betterCare',
        'ob01_betterstories_2018_care': 'ob01_betterCare',
        'personicx_main_accessoires': 'personicx',
        'pr_amplification_newsarticle': 'pr_amplification',
        'valentines_day_2018': 'valentines_day',
        'valentines_day_white_mail_evoucher': 'valentines_day',
        'valentinesday_pack_mail': 'valentines_day'
    }

    df.loc[:, 'CAMPAIGN_CONTENT'] = \
    (df_cellDescr['CAMPAIGN_CONTENT_1_CDS']
     .map(lambda i: i.strip().lower())
     .pipe(clip_categorical, COVERAGE=0.88)
     .replace(dict_replace_campaign_content)
     .values
    )

    del df_cellDescr

    print("Scrubbing Channel")
    df.loc[:, 'CHANNEL'] = \
    (df['CHANNEL']
     .map(replace_spaces)
     .pipe(clip_categorical)
     .values
    )


    df.drop(['CONTACT_HISTORY_ID'], axis=1, inplace=True)
    return df

def aggregate_df(df, df_y, cols_flags):
    """
    """
    ckey = df.CONSUMER_KEY.sample(1).iloc[0]
    try:
        _, conversion_measure, date_survey = df_y.query("CONSUMER_KEY == {}".format(ckey)).values[0]
        dfrp = df.query("CONSUMER_KEY == {}".format(ckey))
        dfrp = dfrp[dfrp.SELECTION_DATE <= date_survey]

        s1 = dfrp[cols_flags].mean()

        if len(s1) > 1:
            pass
        else:
            s1 = Series(0, index=cols_flags)

        weekend_responses = \
        (df
         .SELECTION_DATE
         .dt.strftime("%a")
         .value_counts()
         .reindex(['Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri'])
        )

        s2 = Series({
            'num_contacts': dfrp.shape[0],
            'num_months_active_contacts': dfrp.SELECTION_DATE.dt.strftime("%b_%Y").nunique(),
            'num_days_bw_lastContact_survey': (date_survey - dfrp.SELECTION_DATE.max())/np.timedelta64(1, 'D'),
            'perc_contacts_weekend': weekend_responses.loc[['Sat', 'Sun']].sum()/weekend_responses.sum(),
            'y': conversion_measure
        })
        return pd.concat([s1, s2])
    except:
        errors_aggregate_df.append(ckey)
        pass

@time_my_func
def get_aggregated_df(df, aggfunc):
    """
    """
    df_y = get_target_df()
    cols_flags = [x for x in df.columns if x.startswith('flag_')]

    df_aggregated = \
    (df
     .groupby("CONSUMER_KEY")
     .apply(aggfunc, df_y=df_y, cols_flags=cols_flags)
    )

    return df_aggregated


if __name__ == '__main__':
    errors_aggregate_df = []
    df_aggregated = (import_filter_df(path_raw)
                     .pipe(remove_zv_missings)
                     .pipe(engineer_features)
                     .pipe(create_dummified_df)
                     .pipe(get_aggregated_df, aggfunc=aggregate_df)
                    )

    backup_df(df=df_aggregated, path_clean=path_clean)

    tbl_ = path_clean.split('/')[-1].replace('clean_', '').replace('.csv', '').strip()
    load_file_to_db(path_to_file=path_clean,
            path_to_db=path_clean_db,
            table_name=tbl_,
            delim=',')