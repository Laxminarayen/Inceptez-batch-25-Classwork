import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
#from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from imblearn.under_sampling import RandomUnderSampler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from imblearn.pipeline import Pipeline
from sklearn.base import BaseEstimator, ClassifierMixin
import joblib
from custom_model_pipeline import ThresholdClassifier

print("Loading Data...")
train = pd.read_csv('../data/Paitients_Files_Train.csv')
test = pd.read_csv('../data/Paitients_Files_Test.csv')
print("Data Loaded Successfully")
train['Sepssis'].replace({'Positive':1,'Negative':0},inplace=True)

X = train.drop(['ID','Sepssis'], axis=1)
y = train['Sepssis']

print(X.shape, y.shape)
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=0.2, random_state=42)
print("Train Shape: ", train_X.shape, train_y.shape)
pipeline = Pipeline(
    steps = [
        ('imputer', SimpleImputer(strategy='mean')),
        ('scaler', StandardScaler()),
        ('Balanced_Sampling', RandomUnderSampler()),
        ('model', ThresholdClassifier(model=LogisticRegression(), threshold=0.45))
    ]
)
print("Pipeline Created Successfully")
pipeline.fit(train_X, train_y)
print("Pipeline Fitted Successfully")
predict_train = pipeline.predict(train_X)
predict_test = pipeline.predict(test_X)
print("Predictions Made Successfully")
print("Train accuracy_score: \n", accuracy_score(train_y, predict_train))
print("Test accuracy_score: \n", accuracy_score(test_y, predict_test))
print("Train confusion_matrix: \n", confusion_matrix(train_y, predict_train))
print("Test confusion_matrix: \n", confusion_matrix(test_y, predict_test))
print("Train Classification Report:\n", classification_report(train_y, predict_train))
print("Test Classification Report:\n", classification_report(test_y, predict_test))
test_predict_unseen = pipeline.predict(test.drop('ID', axis=1))
print("Final Prediction on Test Data that is unseen to the model")
print(test_predict_unseen)
# Save the pipeline
joblib.dump(pipeline, '../models/model_balanced_threshold_0.45.pkl')
