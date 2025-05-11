from flask import Flask, request, jsonify, render_template_string
import joblib

app = Flask(__name__)

# Загрузка модели и векторизатора
model = joblib.load("retrained_model.joblib")
vectorizer = joblib.load("retrained_vectorizer.joblib")

# Загрузка HTML и CSS
with open("index.html", encoding="utf-8") as f:
    html_template = f.read()
with open("style.css", encoding="utf-8") as f:
    style_content = f"<style>{f.read()}</style>"

@app.route("/", methods=["GET"])
def home():
    return render_template_string(style_content + html_template, prediction_text="")

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    skills_input = data.get("skills", "")
    vector = vectorizer.transform([skills_input])
    prediction = model.predict(vector)[0]
    return jsonify({"predicted_role": prediction})

if __name__ == "__main__":
    app.run(debug=True)
