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
        # self.__data.columns = col
        print self.__data.head()

    def sort_dataset(self):
        # sort dataframe by column value
        # print self.__data.sort_values(by='label',ascending=1)
        # sort by last name or value in string
        reg=[reg for reg in self.__data['label']]
        print reg
        print sorted(self.__data['label'],key=lambda x: len(x))


    def drop_column(self):
        sd=[]
        # print self.__data.drop('label',axis=1).head()
        # print self.__data.drop(['label','message'],axis=1)
        # print self.__data.message[(self.__data.label != 'ham') & (self.__data.message.map(lambda x: len(x) == 5)) ]
        sd.append(self.__data.label[self.__data['message'].map(lambda x: len(x) == 5)])
        print sd

    def drop_duplicated(self):
        print self.__data['label'].drop_duplicates()


if __name__ == "__main__" :
    path = '/Users/badrkhamis/learning_path/python/classfication_scitit-learn/sms.csv'
    pointer = Panda(path)
    # pointer.basic_panda()
    pointer.drop_column()

    # pointer.drop_duplicated()
