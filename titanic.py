import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


df_train = pd.read_csv('train.csv')
df_test = pd.read_csv('test.csv')

df_train.head(5)