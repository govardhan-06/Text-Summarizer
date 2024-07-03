from src.pipeline.phase_01_data_ingestion import DataIngestionPipeline
from src.pipeline.phase_02_data_validation import DataValidationPipeline
from src.logging import logger

STAGE_NAME="Data Ingestion Phase"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} initiated <<<<<<<<<<")
    data_ingestion_pipeline = DataIngestionPipeline()
    data_ingestion_pipeline.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME="Data Validation Phase"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} initiated <<<<<<<<<<")
    data_validation_pipeline = DataValidationPipeline()
    data_validation_pipeline.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e