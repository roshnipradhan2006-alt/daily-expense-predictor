# =====================================================
#        AI Daily Expense Predictor (ML Project)
#        Course: Fundamentals of AI & ML
# =====================================================

import pandas as pd
from sklearn.linear_model import LinearRegression


# -----------------------------------------------------
# 1. Program Header
# -----------------------------------------------------
print("\n======================================")
print("        AI DAILY EXPENSE PREDICTOR")
print("======================================\n")


# -----------------------------------------------------
# 2. Load Dataset
# -----------------------------------------------------
print("📂 Loading dataset...")

data = pd.read_csv(r"C:\Users\hp\Downloads\expense_data.csv")

print("✅ Dataset loaded successfully!\n")


# -----------------------------------------------------
# 3. Prepare Features and Target
# -----------------------------------------------------
# Features = Inputs used for prediction
# Target = Value we want to predict

features = data[['Income', 'Day', 'PreviousExpense']]
target = data['Expense']


# -----------------------------------------------------
# 4. Train Machine Learning Model
# -----------------------------------------------------
print("🤖 Training the AI model...")

model = LinearRegression()
model.fit(features, target)

print("✅ Model training completed!\n")


# -----------------------------------------------------
# 5. Take User Input
# -----------------------------------------------------
print("Please enter the following details:\n")

income = float(input("💰 Enter your monthly income (₹): "))
day = int(input("📅 Enter day type (0 = Weekday, 1 = Weekend): "))
previous_expense = float(input("🧾 Enter your previous day's expense (₹): "))

print("\n🔍 Predicting today's expense...\n")


# -----------------------------------------------------
# 6. Make Prediction
# -----------------------------------------------------
prediction = model.predict(
    pd.DataFrame([[income, day, previous_expense]],
    columns=['Income', 'Day', 'PreviousExpense'])
)

predicted_expense = round(prediction[0], 2)


# -----------------------------------------------------
# 7. Display Result
# -----------------------------------------------------
print("======================================")
print("📊 PREDICTION RESULT")
print("======================================")

print(f"Predicted Daily Expense: ₹{predicted_expense}")

print("======================================")
print("Thank you for using the AI Expense Predictor! 😊")
print("======================================\n")
