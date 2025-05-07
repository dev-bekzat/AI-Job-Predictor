import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# здесь мы загружаем данные 
df = pd.read_csv("combined_datasets.csv")
df = df[['Job Title', 'skills']].dropna()
df = df[df['skills'].str.strip().astype(bool)]


X = df['skills']
y = df['Job Title']


vectorizer = TfidfVectorizer(max_features=1000)
X_vec = vectorizer.fit_transform(X)

# разделяем обучающую и тестовую выборку
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

# обучаем модельку
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# оцениваем
y_pred = model.predict(X_test)
print("📊 Classification Report:\n")
print(classification_report(y_test, y_pred))

# сохраняем эту модель
joblib.dump(model, "job_predictor_model.joblib")
joblib.dump(vectorizer, "vectorizer.joblib")

print("✅ Готово! Модель и вектор сохранены")