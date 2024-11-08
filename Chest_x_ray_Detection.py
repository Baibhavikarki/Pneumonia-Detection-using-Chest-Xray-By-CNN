import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load your pneumonia detection model
model = tf.keras.models.load_model('chest_xray_1.h5')


# Function to preprocess the image for prediction


def preprocess_image(image):
    # Convert the image to grayscale
    image = image.convert('L')  # 'L' mode for grayscale in PIL
    # Resize to 150x150 as expected by the model
    img = image.resize((150, 150))
    img_array = np.array(img) / 255.0  # Normalize pixel values between 0 and 1
    # Add channel dimension for grayscale (150, 150, 1)
    img_array = np.expand_dims(img_array, axis=-1)
    # Add batch dimension (1, 150, 150, 1)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Function to make predictions using the model


def make_prediction(image):
    preprocessed_img = preprocess_image(image)
    prediction = model.predict(preprocessed_img)
    return prediction


# Streamlit App Interface
st.title("Pneumonia Detection App")

st.write("Upload a chest X-ray image to check for pneumonia.")

uploaded_file = st.file_uploader(
    "Choose an image...", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Chest X-ray", use_column_width=True)

    # Make a prediction if the user clicks the button
    if st.button('Predict'):
        prediction = make_prediction(image)
        st.write(prediction)  # Show the prediction score

        # Interpret the prediction result
        if prediction[0][0] > 0.5:
            st.write("The model predicts: Normal")
        else:
            st.write("The model predicts: Pneumonia")
