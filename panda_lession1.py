import pandas as pd
import numpy as np

class Panda:
    def __init__(self,path):
        dataset = pd.read_csv(path,header=None,names=['label','message'])
        self.__data = dataset

    def basic_panda(self):
        print self.__data.shape
        print self.__data.head()
        print self.__data.dtypes
        print type(self.__data)
        self.__data.describe(include=['object'])

    def column_name(self):
        self.__data.rename(columns={'label':'Labels'},inplace=True)
        col = ['label','message']
        # self.__data.columns = col

        col = self.__data.columns.str.replace('l','A')
        self.__data.columns = col
        print self.__data.head()
if __name__ == "__main__" :
    path = '/Users/badrkhamis/learning_path/python/classfication_scitit-learn/sms.csv'
    pointer = Panda(path)
    pointer.basic_panda()
    pointer.column_name()
