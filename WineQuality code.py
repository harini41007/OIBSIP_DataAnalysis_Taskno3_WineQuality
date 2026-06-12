#Import libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv('WineQT.csv')
df

#Identify missing values
df.isnull().sum()

#Dataset Information
print(df.info())

#Quality Distribution 
sns.countplot(x="quality", data=df)
plt.title(" Wine Quality Distribution")
plt.show()

#Correlation Heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
plt.title(" FeatureCorrelation Heatmap")
plt.show()

#Convert To classification
df['quality'] =df['quality'].apply(
    lambda x: 1 if x >= 7 else 0
)

#Features & Target
X = df.drop('quality', axis=1)
y = df['quality']

#Train and Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#--1.Random Forest
from sklearn.ensemble import RandomForestClassifier
rf_model = RandomForestClassifier()
rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)
print("Random Forest Accuracy:", accuracy_score(y_test, rf_pred))

#--2.SVC
from sklearn.svm import SVC
svc_model = SVC()
svc_model.fit(X_train, y_train)
svc_pred= svc_model.predict(X_test)
print("SVC Accuracy:", accuracy_score(y_test, svc_pred))

#--3.SGD
from sklearn.linear_model import SGDClassifier
sgd_model = SGDClassifier()
sgd_model.fit(X_train, y_train)
sgd_pred = sgd_model.predict(X_test)
print("SGD Accuracy:", accuracy_score(y_test,sgd_pred))

#Compare Models
results = {
    "Random Forest": accuracy_score(y_test, rf_pred),
    "SVC": accuracy_score(y_test, svc_pred),
    "SGD": accuracy_score(y_test, sgd_pred)
}

for model, acc in results.items():
    print(f"{model}: {acc}")

#Feature important scores
importances = rf_model.feature_importances_
features = X.columns
plt.barh(features,importances)
plt.title("Feature Importance")
plt.show()

# Sample  wine data for testing 
sample = [[7.4,0.7,0,1.9,0.076,11,34,0.9978,3.51,0.56,9.4,0.3]]

prediction = rf_model.predict(sample)

if prediction [0] == 1:
  print("Good Quality Wine")
else:
  print("Bad Quality Wine")





