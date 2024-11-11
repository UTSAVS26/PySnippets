import zipfile
import os
import logging

def handle_response(response, save_path):
    try:
        content_type = response.headers.get('Content-Type', '')
        if 'application/zip' in content_type:
            with open('temp.zip', 'wb') as f:
                f.write(response.content)
            with zipfile.ZipFile('temp.zip', 'r') as zip_ref:
                zip_ref.extractall(save_path)
            os.remove('temp.zip')
            logging.info("Zip file processed and extracted.")
        else:
            logging.info("Response content type: {content_type} - no special handling applied.")
    except Exception as e:
        logging.error(f"Failed to handle response: {e}")