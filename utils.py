import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def process_X(X):
    X = np.array(X).reshape(1, -1)
    imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
    imputer.fit(X)
    X = imputer.transform(X)

    ct = ColumnTransformer(transformers=[
                        ('encoder_gender', OneHotEncoder(), [0]),
                        ('encoder_marriage', OneHotEncoder(), [4]),
                        ('encoder_work', OneHotEncoder(), [5]),
                        ('encoder_residence', OneHotEncoder(), [6]),
                        ('encoder_smoking', OneHotEncoder(), [9]),
        ], remainder='passthrough')

    X = np.array(ct.fit_transform(X))

    return X