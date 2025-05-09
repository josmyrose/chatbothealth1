import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

def train_model():
    df = pd.read_csv("symptoms.csv")
    X = df.drop("Disease", axis=1)
    y = df["Disease"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier()
    clf.fit(X_train, y_train)

    joblib.dump(clf, "disease_model.pkl")
    return clf, X.columns.tolist()

def predict_disease(symptom_dict):
    clf = joblib.load("disease_model.pkl")
    symptoms = pd.DataFrame([symptom_dict])
    prediction = clf.predict(symptoms)
    return prediction[0]
