from perceptronBasics.config.configuration import ConfigurationManager
from perceptronBasics.components.data_transformation import DataTransformation

class DataTransformationPipeline:
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(config= data_transformation_config)
        data_transformation = data_transformation.convert()