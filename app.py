from flask import Flask, render_template, request
import pickle
import pandas as pd
from preprocess import extract_features

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        url = request.form.get("url")
        features = extract_features(url)

        df = pd.DataFrame([features])
        pred = model.predict(df)[0]

        prediction = "⚠️ Phishing URL" if pred == 1 else "✔️ Safe URL"

    return render_template("home.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
