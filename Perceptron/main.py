from perceptronBasics.logging import logger
from perceptronBasics.pipeline.stage_01_ingestion_pipeline import DataIngestionPipeline
from perceptronBasics.pipeline.stage_02_validation_pipeline import DataValidationPipeline
from perceptronBasics.pipeline.stage_03_transformation_pipeline import DataTransformationPipeline


STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<")
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataValidationPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<")
    logger.exception(e)
    raise e

STAGE_NAME = "Data Transformation Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataTransformationPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
except Exception as e:
    logger.error(f">>>>>> stage {STAGE_NAME} failed <<<<<<")
    logger.exception(e)
    raise e