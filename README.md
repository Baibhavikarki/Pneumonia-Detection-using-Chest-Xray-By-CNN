# Pneumonia Detection App

This simple web application uses a convolutional neural network (CNN) to detect pneumonia from chest X-ray images. The app is built with [Streamlit](https://streamlit.io/) for the web interface, and TensorFlow powers the prediction model.

## Features

- **Upload an X-ray image:** Upload a chest X-ray image in PNG, JPG, or JPEG format.
- **Predict pneumonia or normal:** The model outputs a prediction score, allowing the app to classify the X-ray as either pneumonia-positive or normal.

## Prerequisites

- Python 3.6 or higher
- TensorFlow
- Streamlit
- PIL (Pillow)

## Installation

1. Clone this repository:
   git clone https://github.com/yourusername/your-repo-name.git
## Navigate into the project directory:
cd your-repo-name
## Install the required packages:

pip install -r requirements.txt

## The requirements.txt should contain:
plaintext
Copy code
streamlit
pillow
tensorflow
numpy

## Model
Ensure you have the pre-trained model (chest_xray_1.h5) in the project directory.

## Running the App
Run the app using Streamlit:
streamlit run app.py
This will start the web application, which you can access at http://localhost:8501 by default.

## Usage
Upload a chest X-ray image using the "Choose an image..." button.
Click "Predict" to view the model's prediction.

## Interpretation
Normal: The model predicts the X-ray is likely normal.
Pneumonia: The model detects signs of pneumonia.
