from src.pipeline.phase_01_data_ingestion import DataIngestionPipeline
from src.pipeline.phase_02_data_validation import DataValidationPipeline
from src.pipeline.phase_03_data_transformation import DataTransformationPipeline
from src.pipeline.phase_04_model_trainer import ModelTrainingPipeline
from src.pipeline.phase_05_model_evaluation import ModelEvaluationPipeline
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

STAGE_NAME="Data Transformation Phase"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} initiated <<<<<<<<<<")
    data_transformation_pipeline = DataTransformationPipeline()
    data_transformation_pipeline.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Training Phase"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} initiated <<<<<<<<<<")
    model_trainer_pipeline = ModelTrainingPipeline()
    model_trainer_pipeline.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME="Model Evaluation Phase"

try:
    logger.info(f">>>>>>>>> {STAGE_NAME} initiated <<<<<<<<<<")
    model_eval_pipeline = ModelEvaluationPipeline()
    model_eval_pipeline.main()
    logger.info(f">>>>>>>>> {STAGE_NAME} completed <<<<<<<<<<")
except Exception as e:
    logger.exception(e)
    raise e