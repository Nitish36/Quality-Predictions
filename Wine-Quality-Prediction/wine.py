import pickle
import streamlit as st

quality = ["3. Worst Quality", "8. Worse Quality", "4. Bad Quality", "7. Good Quality", "6. Better Quality", "5. Best quality"]

# Load the trained model from the pickle file
model = pickle.load(open('test.pkl', 'rb'))

# Create sliders for input features
fixed_acid = st.slider("fixed_acid:", 4.0, 16.0, 0.1)
volatile_acidity = st.slider("volatile_acidity:", 0.0, 1.6, 0.01)
citric_acid = st.slider("citric_acid:", 0.0, 1.0, 0.01)
residual_sugar = st.slider("residual_sugar:", 0.5, 16.0, 0.1)
chlorides = st.slider("chlorides:", 0.010, 0.615, 0.001)
free_sulfur_dioxide = st.slider("free_sulfur_dioxide", 0, 75, 1)
total_sulfur_dioxide = st.slider("total_sulfur_dioxide:", 5, 289, 1)
density = st.slider("density:", 0.0, 1.0, 0.1)
pH = st.slider("pH:", 2.5, 4.5, 0.01)
sulphates = st.slider("sulphates:", 0.3, 2.0, 0.01)
alcohol = st.slider("alcohol:", 8.0, 15.0, 1.0)

# Predict wine quality based on input features
input_data = [[fixed_acid, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]]
y_pred = model.predict(input_data)[0]
predicted_quality = quality[y_pred]

# Display predicted quality and print corresponding message
clicked = st.button("Submit")
if clicked:
    st.success(predicted_quality)
    print(predicted_quality)
