import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, roc_auc_score
import pickle

# Simulasi dataset
np.random.seed(42)
data = {
    "annual_income": np.random.randint(20000, 120000, 1000),
    "credit_score": np.random.randint(300, 850, 1000),
    "current_debt": np.random.randint(1000, 50000, 1000),
    "loan_amount": np.random.randint(500, 40000, 1000),
    "loan_status": np.random.choice([0, 1], size=1000)  # 0: Rejected, 1: Approved
}

df = pd.DataFrame(data)

# Pisahkan fitur dan target
X = df.drop(columns=["loan_status"])
y = df["loan_status"]

# Split data train dan test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Latih model Random Forest
model = RandomForestClassifier(n_estimators=100, max_depth=10, random_state=42)
model.fit(X_train, y_train)

# Evaluasi model
y_pred = model.predict(X_test)
y_prob = model.predict_proba(X_test)[:, 1]
print("Accuracy:", accuracy_score(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, y_prob))

# Simpan model ke file
with open("loan_approval_model.pkl", "wb") as model_file:
    pickle.dump(model, model_file)
