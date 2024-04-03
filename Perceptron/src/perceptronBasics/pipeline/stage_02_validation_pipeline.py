from perceptronBasics.config.configuration import ConfigurationManager
from perceptronBasics.components.data_validation import DataValidation

class DataValidationPipeline():
    def __init__(self):
        pass

    def main():
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config= data_validation_config)
        data_validation.validate_all_files_exists()