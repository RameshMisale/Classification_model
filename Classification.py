import streamlit as st
import pickle
import pandas as pd

st.markdown("<h1 style='text-align: center;'>House Price Prediction</h1>", unsafe_allow_html=True)

# Create a centered container for the input features using HTML and CSS
st.markdown(
    """
    <div style="display: flex; justify-content: center; align-items: center;">
        <div>
            <h2>Input Features</h2>
            <p>Age: <input type='number' id='age'></p>
            <p>BMI: <input type='number' id='bmi'></p>
            <p>Glucose: <input type='number' id='glucose'></p>
            <p>Insulin: <input type='number' id='insulin'></p>
            <p>HOMA: <input type='number' id='homa'></p>
            <p>Leptin: <input type='number' id='leptin'></p>
            <p>Adiponectin: <input type='number' id='adiponectin'></p>
            <p>Resistin: <input type='number' id='resistin'></p>
            <p>MCP.1: <input type='number' id='mcp1'></p>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)

# Load your pre-trained classification model using pickle
with open('Classification_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Center the prediction button using HTML and CSS
st.markdown(
    """
    <div style="text-align: center;">
        <button onclick="predict()">Predict</button>
    </div>
    <script>
        function predict() {
            const age = document.getElementById('age').valueAsNumber;
            const bmi = document.getElementById('bmi').valueAsNumber;
            const glucose = document.getElementById('glucose').valueAsNumber;
            const insulin = document.getElementById('insulin').valueAsNumber;
            const homa = document.getElementById('homa').valueAsNumber;
            const leptin = document.getElementById('leptin').valueAsNumber;
            const adiponectin = document.getElementById('adiponectin').valueAsNumber;
            const resistin = document.getElementById('resistin').valueAsNumber;
            const mcp1 = document.getElementById('mcp1').valueAsNumber;
            
            const input_data = {
                Age: age,
                BMI: bmi,
                Glucose: glucose,
                Insulin: insulin,
                HOMA: homa,
                Leptin: leptin,
                Adiponectin: adiponectin,
                Resistin: resistin,
                MCP1: mcp1
            };
            
            fetch('/predict', {
                method: 'POST',
                body: JSON.stringify(input_data),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.text())
            .then(data => {
                alert("Prediction: " + data);
            });
        }
    </script>
    """,
    unsafe_allow_html=True
)
