import pandas as pd
from sklearn.linear_model import LinearRegression

# Train model once
data = pd.read_csv("house_data.csv")

X = data[["Area", "Bedrooms", "Age"]]
y = data["Price"]

model = LinearRegression()
model.fit(X, y)

def predict_price(area, bedrooms, age):
    prediction = model.predict([[area, bedrooms, age]])
    return prediction[0]

