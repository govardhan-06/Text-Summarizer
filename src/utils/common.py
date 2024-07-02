import os
from box.exceptions import BoxValueError
import yaml
from src.logging import logger
from box import ConfigBox
from ensure import ensure_annotations
from typing import Any, List
from pathlib import Path

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    '''
    Read a yaml file and return a ConfigBox object
    '''
    try:
        with open(path_to_yaml, 'r') as file:
            content=yaml.safe_load(file)
            print(content)
            print(path_to_yaml)
            logger.info(f"Reading yaml file {path_to_yaml}")
            return ConfigBox(content)
            
    except FileNotFoundError as e:
        logger.error(f"YAML file not found: {path_to_yaml}")
        raise e
    
    except BoxValueError as e:
        logger.error(f"Error reading yaml file: {e}")
        raise BoxValueError(f"Error reading yaml file: {e}")

    except Exception as e:
        raise e

@ensure_annotations
def create_directories(dir_path,verbose=True):
    '''
    Create directories if they do not exist
    '''
    try:
        for path in dir_path:
            if not os.path.exists(path):
                logger.info(f"Creating directory {path}")
                os.makedirs(path)

    except Exception as e:
        logger.error(f"Error creating directory: {e}")
        raise e

@ensure_annotations
def get_size(path:Path) -> int:
    '''
    Get the size of a file in kilo-bytes
    '''
    try:
        size_in_KB=round(os.path.getsize(path)/1024)
        logger.info(f"Getting size of file {path}")
        return size_in_KB
    except Exception as e:
        logger.error(f"Error getting size of file: {e}")
        raise e