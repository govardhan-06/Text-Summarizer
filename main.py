from src.pipeline.phase_01_data_ingestion import DataIngestionPipeline
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