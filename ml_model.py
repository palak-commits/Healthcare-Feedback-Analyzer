import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("dataset.csv")

X = data["text"]
y = data["label"]

# Convert text to numbers
vectorizer = CountVectorizer()
X_vector = vectorizer.fit_transform(X)

# Train model
model = MultinomialNB()
model.fit(X_vector, y)

# Save model + vectorizer
with open("ml_model.pkl", "wb") as f:
    pickle.dump(model, f)

with open("vectorizer.pkl", "wb") as f:
    pickle.dump(vectorizer, f)

# Function for prediction
def classify_text(user_input):
    user_vector = vectorizer.transform([user_input])
    return model.predict(user_vector)[0]