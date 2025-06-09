"""Simple AI Social Engineering Detector.

This script trains a logistic regression classifier on a small sample dataset of
automated phishing messages versus legitimate human messages.
"""

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

DATA_PATH = "sample_emails.csv"


def train_model(csv_path: str):
    """Train a text classifier and return the fitted pipeline."""
    data = pd.read_csv(csv_path)
    X_train, X_test, y_train, y_test = train_test_split(
        data["text"], data["label"], test_size=0.2, random_state=42
    )
    model = Pipeline(
        [
            ("tfidf", TfidfVectorizer()),
            ("clf", LogisticRegression(max_iter=1000)),
        ]
    )
    model.fit(X_train, y_train)
    accuracy = model.score(X_test, y_test)
    print(f"Model trained. Test accuracy: {accuracy:.2f}")
    return model


if __name__ == "__main__":
    classifier = train_model(DATA_PATH)
    while True:
        text = input("Enter email text (or 'quit'): ")
        if text.lower() == "quit":
            break
        prediction = classifier.predict([text])[0]
        print(f"Prediction: {prediction}\n")
