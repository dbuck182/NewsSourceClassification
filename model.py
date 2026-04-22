# 1. Load the CSV files & Preprocess the data
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
csv_file_path = 'data/news_headlines.csv'
news_df = pd.read_csv(csv_file_path)
# ... ...
news_df['source'] = news_df['Link'].str.extract(r'www\.(.*?)\.')

# 2. Split the data into training and testing sets
# (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(news_df['Title'], news_df['source'], test_size=0.20, random_state=42)
# ... ...
# 3. Convert the labels to binary values (0 for ’FoxNews’, 1 for ’NBC’)
y_train = y_train.apply(lambda x: 1 if x == 'foxnews' else 0)
y_test = y_test.apply(lambda x: 1 if x == 'foxnews' else 0)
# 4. Convert the text data to TF-IDF features
vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
X_train_tfidf = vectorizer.fit_transform(X_train)
X_test_tfidf = vectorizer.transform(X_test)
# 5. Train a Logistic Regression model
model = LogisticRegression(max_iter=100)
model.fit(X_train_tfidf, y_train)
# 6. Make predictiosn on the test set
y_pred = model.predict(X_test_tfidf)
# 7. Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")
print("Classification Report:\n", classification_report(y_test, y_pred)
)

## Result
# Accuracy: 0.6649
# Classification Report:
# precision recall f1-score support
# 0 0.69 0.54 0.60 358
# 1 0.65 0.78 0.71 400

# accuracy 0.66 758
# macro avg 0.67 0.66 0.66 758
# weighted avg 0.67 0.66 0.66 758