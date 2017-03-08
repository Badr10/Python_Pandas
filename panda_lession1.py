import pandas as pd
import numpy as np

class Panda:
    def __init__(self,path):
        dataset = pd.read_csv(path)
        self.__data = dataset

    def basic_panda(self):
        print self.__data.shape
        print self.__data.head()

    def column_name(self):
        

if __name__ == "__main__" :
    path = '/Users/badrkhamis/learning_path/python/classfication_scitit-learn/sms.csv'
    pointer = Panda(path)
    pointer.basic_panda()
