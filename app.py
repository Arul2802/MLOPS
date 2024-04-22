import streamlit as st
import pickle
import numpy as np

# Load the saved Linear Regression model
with open('gdp.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Function to predict GDP per capita using the loaded model
def predict_GDPpercapita(Overall_rank,Score,Social_support,Healthy_life_expectancy,Freedom_to_make_life_choices,Generosity,Perceptions_of_corruption):
    features = np.array([Overall_rank,Score,Social_support,Healthy_life_expectancy,Freedom_to_make_life_choices,Generosity,Perceptions_of_corruption])
    features = features.reshape(1,-1)
    GDPpercapita = model.predict(features)
    return GDPpercapita[0]

# Streamlit UI
st.title('GDP PER CAPITA PREDICTION')
st.write("""   
Enter the values for the input features to predict GDP per capita.
""")

# Input fields for user
Overall_rank = st.number_input('Overall rank')
Score = st.number_input('Score')
Social_support = st.number_input('Social support')
Healthy_life_expectancy = st.number_input('Healthy life expectancy')
Freedom_to_make_life_choices= st.number_input('Freedom_to_make_life_choices')
Generosity = st.number_input('Generosity')
Perceptions_of_corruption = st.number_input('Perceptions of corruption')

# Prediction button
if st.button('Predict'):
    # Predict Sport
    GDPpercapita_prediction = predict_GDPpercapita(Overall_rank,Score,Social_support,Healthy_life_expectancy,Freedom_to_make_life_choices,Generosity,Perceptions_of_corruption)
    st.write(f"Predicted GDPpercapita: {GDPpercapita_prediction}")