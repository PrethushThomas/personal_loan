 
from pycaret.classification import load_model, predict_model
import streamlit as st
import pandas as pd
import numpy as np
model = load_model('bank_loan')






def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

def run():
    from PIL import Image
    image = Image.open('/content/Personal_Loan.jpg')
    image_office = Image.open('/content/bank.jpg')
    st.image(image,use_column_width=True)
    add_selectbox = st.sidebar.selectbox(
    "How would you like to predict?",
    ("Online", "Batch"))
    st.sidebar.info('This app is created to predict if customer is eligible for personal loan or not')
    st.sidebar.success('https://www.pycaret.org')
    st.sidebar.image(image_office)
    st.title("Predicting chance to have personal loan")
    if add_selectbox == 'Online':
        ID=st.number_input('ID' , min_value=1.0, max_value=10000.0, value=1.0)
        Age=st.number_input('Age',min_value=1.0, max_value=70.0, value=1.0)
        Experience=st.number_input('Experience',min_value=1.0, max_value=50.0, value=1.0)
        Income=st.number_input('Income',min_value=1.0, max_value=500.0, value=1.0)
        ZIP_Code=st.number_input('ZIP Code',min_value=1.0, max_value=100000.0, value=1.0)
        Family=st.number_input('Family',min_value=1.0, max_value=10.0, value=1.0)
        CCAvg=st.number_input('CCAvg',min_value=0.0, max_value=10.0, value=1.0)
        Education= st.selectbox('Education',['Undergrad','Graduate','Advanced/Professional'])
        Mortgage=st.number_input('Mortgage',min_value=0.0, max_value=1000.0, value=1.0)
        Securities_Account=st.number_input('Securities Account',min_value=0.0, max_value=1.0, value=1.0)
        CD_Account=st.number_input('CD Account',min_value=0.0, max_value=1.0, value=1.0)
        Online=st.number_input('Online',min_value=0.0, max_value=1.0, value=1.0)
        CreditCard=st.number_input('CreditCard',min_value=0.0, max_value=1.0, value=1.0)
        output=""
        input_dict={'ID':ID,'Age':Age,'Experience':Experience,'Income':Income,'ZIP Code':ZIP_Code,'Family':Family,'CCAvg' : CCAvg,'Education':Education,'Mortgage':Mortgage,'Securities Account':Securities_Account,'CD Account':CD_Account,'Online':Online,'CreditCard':CreditCard}
        input_df = pd.DataFrame([input_dict])
        if st.button(" predict eligible or not"):
            output = predict(model=model, input_df=input_df)
            output = str(output)
            if output == '0' :
              output="SORRY! YOU ARE NOT ELIGIBLE FOR PERSONAL LOAN"
            else:
              output="CONGRATS! YOU ARE ELIGIBLE FOR PERSONAL LOAN"
        st.success('The Prediction   --  {}'.format(output))
    if add_selectbox == 'Batch':
        file_upload = st.file_uploader("Upload csv file for predictions", type=["csv"])
        if file_upload is not None:
            data = pd.read_csv(file_upload)            
            predictions = predict_model(estimator=model,data=data)
            st.write(predictions)
def main():
    run()

if __name__ == "__main__":
  main()
