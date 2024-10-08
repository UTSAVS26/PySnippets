import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from scipy import stats

class DataUtils:

    @staticmethod
    def load_and_preview_data(file_path, rows=5):
        """
        Function to load a CSV file and display the first few rows.
        """
        data = pd.read_csv(file_path)
        print(f"First {rows} rows of the dataset:")
        print(data.head(rows))
        return data

    @staticmethod
    def basic_statistics(data):
        """
        Function to calculate and print basic statistics for numerical features in the dataset.
        """
        print("Basic Statistics:")
        stats_summary = data.describe()
        print(stats_summary)
        return stats_summary

    @staticmethod
    def missing_data_analysis(data):
        """
        Function to analyze and visualize missing data.
        """
        missing_data = data.isnull().sum().sort_values(ascending=False)
        missing_percent = (missing_data / len(data)) * 100
        missing_info = pd.DataFrame({'Missing Values': missing_data, 'Percentage': missing_percent})
        print(missing_info)

        # Plot missing data
        plt.figure(figsize=(10, 6))
        sns.barplot(x=missing_info.index, y=missing_info['Percentage'])
        plt.title("Percentage of Missing Data by Feature")
        plt.xticks(rotation=90)
        plt.ylabel('Percentage')
        plt.show()

        return missing_info

    @staticmethod
    def data_distribution_analysis(data, feature):
        """
        Function to plot the distribution of a specific feature.
        """
        plt.figure(figsize=(8, 6))
        sns.histplot(data[feature], kde=True, bins=30)
        plt.title(f'Distribution of {feature}')
        plt.xlabel(feature)
        plt.ylabel('Count')
        plt.show()

    @staticmethod
    def correlation_analysis(data, method='pearson'):
        """
        Function to perform and visualize correlation analysis for numerical features.
        """
        correlation_matrix = data.corr(method=method)
        print(f"Correlation Matrix ({method}):")
        print(correlation_matrix)

        # Heatmap visualization
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
        plt.title(f'Correlation Matrix ({method})')
        plt.show()

        return correlation_matrix

    @staticmethod
    def detect_outliers_z_score(data, threshold=3):
        """
        Function to detect outliers using the Z-score method.
        """
        z_scores = np.abs(stats.zscore(data.select_dtypes(include=[np.number])))
        outliers = np.where(z_scores > threshold)
        print(f"Outliers detected using Z-score (threshold={threshold}):")
        print(outliers)
        return outliers

    @staticmethod
    def train_test_split_data(data, target_column, test_size=0.2, random_state=42):
        """
        Function to split the dataset into training and testing sets.
        """
        X = data.drop(columns=[target_column])
        y = data[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
        print(f"Data successfully split: {len(X_train)} training samples, {len(X_test)} testing samples")
        return X_train, X_test, y_train, y_test

    @staticmethod
    def label_encoding(data, columns):
        """
        Function to apply Label Encoding to categorical columns.
        """
        encoder = LabelEncoder()
        for col in columns:
            data[col] = encoder.fit_transform(data[col].astype(str))
        print(f"Label encoding applied to columns: {columns}")
        return data

    @staticmethod
    def feature_scaling(X_train, X_test):
        """
        Function to scale features using StandardScaler.
        """
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        print("Feature scaling completed.")
        return X_train_scaled, X_test_scaled

    @staticmethod
    def plot_categorical_feature(data, feature):
        """
        Function to plot a count plot for a categorical feature.
        """
        plt.figure(figsize=(8, 6))
        sns.countplot(x=feature, data=data)
        plt.title(f'Count Plot of {feature}')
        plt.xticks(rotation=45)
        plt.show()

    @staticmethod
    def correlation_with_target(data, target_column):
        """
        Function to calculate and visualize the correlation of each feature with the target variable.
        """
        correlation = data.corr()[target_column].sort_values(ascending=False)
        print(f"Correlation of features with the target '{target_column}':")
        print(correlation)

        # Plotting the correlation with target
        plt.figure(figsize=(10, 6))
        sns.barplot(x=correlation.index, y=correlation.values)
        plt.title(f'Correlation of Features with {target_column}')
        plt.xticks(rotation=90)
        plt.show()

        return correlation


