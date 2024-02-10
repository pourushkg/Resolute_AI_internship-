from src.mlProject.constants import *
from src.mlProject.utils.common import read_yaml,create_directories
from src.mlProject.entity.config_entity import DataIngestionConfig_for_task_1



class ConfigurationManager:
    def __init__(
        self,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH,
        schema_filepath = SCHEMA_FILE_PATH):

        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self) -> DataIngestionConfig_for_task_1:
        config = self.config.data_ingestion_for_task1

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig_for_task_1(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_dir=config.local_data_dir,

        )

        return data_ingestion_config