# AI Daily Expense Predictor

## 📌 Project Overview

The **AI Daily Expense Predictor** is a simple machine learning project that predicts a person's daily spending based on a few important factors such as income, day type (weekday or weekend), and previous expenses.
The goal of this project is to demonstrate how machine learning can be used to analyze spending patterns and provide predictions that help users manage their daily budget more effectively.

This project was developed as part of the **Fundamentals of AI and Machine Learning course**.

---

## ❓ Problem Statement

Many individuals struggle to track and control their daily expenses. Without understanding spending patterns, it becomes difficult to plan budgets effectively.
This project addresses that problem by building a machine learning model that predicts the expected daily expense based on past financial behavior.

---

## 🧠 Machine Learning Approach

This project uses **Linear Regression**, a supervised learning algorithm, to learn the relationship between different factors affecting daily spending.

The model analyzes historical data and learns patterns between:

* Monthly Income
* Day Type (Weekday or Weekend)
* Previous Day's Expense

Using this information, the model predicts the expected expense for a new day.

---

## 🛠 Technologies Used

* Python
* Pandas (Data processing)
* Scikit-learn (Machine Learning)

---

## 📂 Dataset

The dataset contains past examples of daily spending with the following features:

| Column          | Description                            |
| --------------- | -------------------------------------- |
| Income          | Monthly income of the individual       |
| Day             | 0 = Weekday, 1 = Weekend               |
| PreviousExpense | Expense from the previous day          |
| Expense         | Actual daily expense (target variable) |

Example dataset row:

Income,Day,PreviousExpense,Expense
25000,1,450,550

---

## 📁 Project Structure

```
daily-expense-predictor
│
├── ai_expense_predictor.py
├── expense_data.csv
├── README.md
└── requirements.txt
```

---

## ▶️ How to Run the Project

### 1️⃣ Install Dependencies

Install the required Python libraries:

pip install pandas scikit-learn

### 2️⃣ Run the Program

Run the Python file:

python ai_expense_predictor.py

### 3️⃣ Enter User Input

The program will ask for:

* Monthly Income
* Day Type (0 = Weekday, 1 = Weekend)
* Previous Expense

The model will then predict the expected daily expense.

---

## 💡 Example Output

Predicted Daily Expense: ₹494.23

---

## 🚀 Future Improvements

Some possible improvements for this project include:

* Adding more features such as location or lifestyle habits
* Using larger datasets for better predictions
* Building a graphical user interface (GUI)
* Creating a web or mobile application

---

## 📌 Conclusion

This project demonstrates how machine learning can be used to analyze financial behavior and predict daily spending. Even with a simple dataset and algorithm, AI can provide useful insights that help individuals manage their finances more effectively.
