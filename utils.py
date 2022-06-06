import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder

def process_X(X):

    sample_dict = {}
    for x in X:
        key, value = x
        sample_dict[key] = value

    sample = pd.DataFrame(sample_dict, index=[0])

    sample = pd.DataFrame({
        'gender': 'Male',
        'age': 21,
        'hypertension': 0,
        'heart_disease': 0,
        'ever_married': 'No',
        'work_type': 'Never_worked',
        'Residence_type': 'Urban',
        'avg_glucose_level': 100,
        'bmi': 18.4,
        'smoking_status': 'never smoked'
    }, index=[0])

    gender_cols = ['Male', 'Female', 'Other']
    ever_married_cols = ['Yes', 'No']
    work_type_cols = ['Private', 'Self-employed', 'Govt_job', 'children', 'Never_worked']
    residence_type_cols = ['Urban', 'Rural']
    smoking_status_cols = ['formerly smoked', 'never smoked', 'smokes', 'Unknown']

    overall_cols = [
        ("gender", gender_cols),
        ("ever_married", ever_married_cols),
        ("work_type", work_type_cols),
        ("Residence_type", residence_type_cols),
        ("smoking_status", smoking_status_cols),
    ]

    df = pd.DataFrame()

    for x in overall_cols:
        df_s = pd.DataFrame({
            x[0]: x[1]
        })
        df1 = pd.get_dummies(df_s)
        df = pd.concat([df, df1], axis=1)
    
    df_c = pd.get_dummies(sample).reindex(columns=df.columns, fill_value=0)

    df_nc = pd.DataFrame()
    print(sample.columns)
    for c in sample.columns:
        if sample[str(c)].dtype != object:
            s = pd.DataFrame({
                c: sample[str(c)].values[0]
            }, index=[0])
            df_nc = pd.concat([df_nc, s], axis=1)


    final_df = pd.concat([df_c, df_nc], axis=1)

    print("Here the final df")
    
    return final_df

def predict(sample, model):
    prediction = -1
    try:
        prediction = model.predict(sample)
    except:
        print("Can't predict")
    return prediction