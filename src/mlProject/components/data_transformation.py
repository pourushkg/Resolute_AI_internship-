import os 
from mlProject import logger 
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd 
from mlProject.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config


    
    ## Note: You can add different data transformation techniques such as Scaler, PCA and all
    #You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_spliting cz this data is already cleaned up


    def train_test_spliting(self):
        data = pd.read_csv(self.config.data_path)
        scaler = StandardScaler()
        scaler.fit(data.drop('target',axis=1))
        scaled_features = scaler.transform(data.drop('target',axis=1))
        df_feat = pd.DataFrame(scaled_features,columns=data.columns[:-1])
        df_feat["target"] = data['target']

        # Split the data into training and test sets. (0.75, 0.25) split.
        train, test = train_test_split(df_feat)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)