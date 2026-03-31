import pandas as pd
from sklearn.linear_model import LinearRegression

data = pd.read_csv("expense_data.csv")

X = data[['Income','Day','PreviousExpense']]
y = data['Expense']

model = LinearRegression()
model.fit(X,y)

prediction = model.predict([[25000,1,400]])

print("Predicted Expense:", prediction[0])
