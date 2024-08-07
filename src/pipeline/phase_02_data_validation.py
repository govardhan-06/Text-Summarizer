from config.configuration import ConfigurationManager
from src.logging import logger
from src.components.data_validation import DataValidation

class DataValidationPipeline:
    def __init__(self):
        pass

    def main(self):
        config=ConfigurationManager()
        data_Validation_config=config.get_data_validation_config()
        data_Validation=DataValidation(config=data_Validation_config)
        data_Validation.validate_all_files_exist()