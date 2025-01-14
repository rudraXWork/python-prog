import numpy as np
import pandas as pd
from sklearn.datasets import load_linnerud
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report


linnerud = load_linnerud()
X = linnerud.data  
y = linnerud.target 


X_df = pd.DataFrame(X, columns=linnerud.feature_names)
y_df = pd.DataFrame(y, columns=linnerud.target_names)


print("Features:")
print(X_df.head())
print("\nTarget:")
print(y_df.head())


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


gnb = GaussianNB()


gnb.fit(X_train, y_train)


y_pred = gnb.predict(X_test)


accuracy = accuracy_score(y_test, y_pred)
print(f"\nAccuracy: {accuracy * 100:.2f}%")
print("\nClassification Report:")
print(classification_report(y_test, y_pred, target_names=linnerud.target_names))
