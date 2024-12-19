from flask import Flask, request, jsonify
import pandas as pd
import pickle

# Load model
with open("loan_approval_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

app = Flask(__name__)

@app.route("/ping", methods=["GET"])
def ping():
    return jsonify({"status": "API is running"})

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Ambil data input JSON
        input_data = request.json
        if not input_data:
            return jsonify({"error": "No input data provided"}), 400
        
        # Konversi data ke DataFrame
        df = pd.DataFrame(input_data)
        
        # Prediksi
        predictions = model.predict(df)
        probabilities = model.predict_proba(df)[:, 1]
        
        # Format hasil
        results = [
            {
                "input": row.to_dict(),
                "prediction": "Loan Approved" if pred == 1 else "Loan Rejected",
                "probability": prob
            }
            for _, row in df.iterrows()
            for pred, prob in zip(predictions, probabilities)
        ]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/", methods=["GET"])
def home():
    return jsonify({"message": "Welcome to the Loan Approval API!"})

@app.route("/favicon.ico")
def favicon():
    return "", 204  # Respon kosong dengan kode status 204 (No Content)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
