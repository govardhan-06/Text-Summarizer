import os
import urllib.request as request
import zipfile
from src.logging import logger
from utils.common import get_size
from pathlib import Path
from entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            filename,headers=request.urlretrieve(self.config.source_URL,self.config.local_data_file)
            logger.info(f"Downloaded file {filename} with headers\n{headers}")
        else:
            logger.info(f"File already exists of size {get_size(Path(self.config.local_data_file))}")

    def extract_zip(self):
        '''
        Extract the zip file to the unzip directory
        '''
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r") as zip_ref:
            zip_ref.extractall(unzip_path)