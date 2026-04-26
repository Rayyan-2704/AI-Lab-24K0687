import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

spam_data = pd.read_csv("/content/spam.csv", encoding='latin1')
spam_data = spam_data[["v1", "v2"]]
spam_data.columns = ["label", "message"]

spam_data["label"] = spam_data["label"].map({"ham": 0, "spam": 1})
texts = spam_data["message"]
labels = spam_data["label"]

vectorizer = CountVectorizer(stop_words="english")
X_features = vectorizer.fit_transform(texts)
X_train, X_test, y_train, y_test = train_test_split(X_features, labels, test_size=0.2, random_state=42)

log_model = LogisticRegression(max_iter=1000)
log_model.fit(X_train, y_train)

predictions = log_model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))
print("\nClassification Report:\n", classification_report(y_test, predictions))

sample_message = ["Congratulations! You have won a free iPhone. Claim now!!!"]
sample_vector = vectorizer.transform(sample_message)

result = log_model.predict(sample_vector)
print("\nPrediction:", result[0])
print("0 = Not Spam, 1 = Spam")
