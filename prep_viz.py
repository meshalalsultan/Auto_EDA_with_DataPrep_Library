from dataprep.eda import create_report
import pandas as pd
import numpy as np
# loading dataset

df = pd.read_csv('heart-disease.csv')
print(df.head())
report = create_report(df).show_browser()

df2 = pd.read_csv('Groceries_dataset.csv')
print(df2.head())
