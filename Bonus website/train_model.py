import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer

# Загрузка и подготовка данных
df = pd.read_csv("filtered_dataset.csv")
df = df[['Job Title', 'skills']].dropna()
df = df[df['skills'].str.strip().astype(bool)]

X = df['skills']
y = df['Job Title']

# Векторизация текста
vectorizer = TfidfVectorizer(max_features=1000)
X_vec = vectorizer.fit_transform(X)

# Деление на train и test
X_train, X_test, y_train, y_test = train_test_split(X_vec, y, test_size=0.2, random_state=42)

# Обучение модели
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Сохранение модели и векторизатора
joblib.dump(model, "retrained_model.joblib")
joblib.dump(vectorizer, "retrained_vectorizer.joblib")

print("✅ Модель переобучена и сохранена.")
