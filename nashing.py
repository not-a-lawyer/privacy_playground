
import pandas as pd


import names

if __name__ == "__main__":

    #import train data from Kaggle Titanic

    real_names = pd.read_csv('train.csv', usecols=["Name"])

    print(real_names.head())


    #Hashing Names

    fake_names = real_names.apply(lambda x: names.get_full_name(),
                                    axis=1)

    print(fake_names.head())








