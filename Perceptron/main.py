from perceptronBasics.logging import logger
from perceptronBasics.pipeline.stage_01_ingestion_pipeline import DataIngestionPipeline


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