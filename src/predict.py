import joblib

model = joblib.load(r'E:\Customer_Churn_Prediction\artifacts\logistic_model.pkl')
preprocessor = joblib.load(r'E:\Customer_Churn_Prediction\artifacts\preprocessor.pkl')


def predict_customer(customer_df):
    customer_processed= preprocessor.transform(customer_df)
    prediction = model.predict(customer_processed)
    probability = model.predict_proba(customer_processed)[0][1]
    return prediction[0] , probability



# testing our inference pipeline


