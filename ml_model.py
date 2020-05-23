import numpy as np
import pandas as pd
import matplotlib.pyplot as pyplot
import seaborn as sns
import pickle

df=pd.read_csv('hiring.csv')

# df.isnull().sum() 
# we saw that the columns 'experience' and 'test_score(out of 10)' had null values.

df['experience'].fillna(0,inplace=True)

df['test_score(out of 10)'].fillna(df['test_score(out of 10)'].mean(),inplace=True)

# in 'experience' , numbers are written as english words , so converting them into numbers:

def word_to_int(w):
    word_dict={'zero':0,'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,'eleven':11,'twelve':12,0:0}
    return word_dict[w]

df['experience'] = df['experience'] .apply(lambda x : (word_to_int(x)))

# features in X , label(target) in y:

X = df.drop('salary($)',axis=1)
y= df['salary($)']

# since dataset is very small , so not splitting it into train and test data i.e. training the model on whole data:
# since 'salary($); is continuous, so using Linear Regression:

from sklearn.linear_model import LinearRegression
lm=LinearRegression()
lm.fit(X,y)

#Saving model to disk
# pickle is the library which helps to dump your model in the form of an extension '.pkl' and it will be dumped in 'wb' i.e. write bytes mode.

pickle.dump(lm,open('lm_model.pkl','wb'))

# 'lm_model.pkl'- this file will be deployed in Heroku environment

#loading model to compare the results

# lm_model = pickle.load(open('lm_model.pkl','rb'))
# print(lm_model.predict([[2,9,6]]))
