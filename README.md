# Breast-Cancer-Detection

A collaborative machine learning and web development project that uses a Convolutional Neural Network (CNN) to classify mammography images as benign or malignant through a web-based application.

## About the Project

Breast cancer detection is an important application of medical image analysis and machine learning. This project explores how deep learning can be used to classify mammography images through a web application.

Our team developed a CNN model trained on a mammography image dataset obtained from Kaggle. The trained model was saved in Keras format and integrated into a Python Flask web application. Users can upload a mammography image through the website and receive a predicted classification.

In addition to image classification, the application includes user registration and login functionality. The project brings together machine learning, image preprocessing, backend development, database integration, and frontend design.

This project was developed collaboratively by three team members, with each member focusing primarily on a different part of the system while also helping with the broader project.

## Features

- CNN-based classification of mammography images.
- Image preprocessing before model prediction.
- Integration of a saved TensorFlow/Keras model into a Flask application.
- Web interface for uploading images and displaying predicted classifications.
- User registration and login functionality.
- SQLite database integration for user account information.
- Separate home, service, about, and contact pages.

## Technologies Used

Python - Machine learning and backend programming 
TensorFlow - CNN model training, loading, and prediction 
Flask - Web application and backend routes 
NumPy - Preparing image arrays for model input 
SQLite - Storing user account information 
Flask-SQLAlchemy - Database integration through an object-relational mapper 
Flask-Login - Managing user login sessions 
Pillow - Loading and resizing images 
HTML, CSS, JavaScript - Frontend structure, styling, and interactivity 

## How It Works

1. **Image upload:** The user selects a mammography image through the website.
2. **Image preprocessing:** The application resizes the image to 224 × 224 pixels, converts it into a numerical array, adds a batch dimension, and scales its pixel values by dividing by 255.
3. **Model prediction:** The pre-trained CNN processes the image and predicts a class.
4. **Result display:** The application displays the predicted classification as *Benign* or *Malignant*.

The application loads the saved model from `first_model (3).keras` rather than training a new model each time it runs.

## Project Structure

The main files and directories include:

- `app.py` — Main Flask application, including routes, image preprocessing, and model prediction.
- `templates/` — HTML templates for the website's pages.
- `static/` — Static website assets and the configured directory for uploaded images.
- `requirements.txt` — Python package dependencies.
- `first_model (3).keras` — Saved trained CNN model used for image classification.
- Additional `.keras` files — Other saved model files included in the repository.

## Team Members and Contributions

This project was developed by a team of three. Each member had a primary area of responsibility, but we collaborated and helped one another throughout development.

### Ebba Dhugasa — Machine Learning and CNN Model Development

- Developed and trained the Convolutional Neural Network (CNN).
- Worked with the mammography image dataset obtained from Kaggle.

### Fikr Yared — Backend Development and Model Integration

- Worked on the Python backend using Flask.
- Contributed to integrating the trained machine learning model with the web application.

### Firaol Addis — Frontend Development

- Worked on the website's frontend.
- Contributed to the user interface and website implementation.

Although each team member had a primary focus, the project was a collaborative effort, and contributions extended beyond these individual responsibilities.

## Getting Started

The application was originally developed to run locally. The following instructions provide a starting point for running it on your own machine.

### Prerequisites

- Python installed on your computer.
- Git installed on your computer.
- The project repository, including its required model file and other application files.

### Installation

**1. Clone the repository**

```bash
git clone <repository-url>
cd <repository-folder>
```

Replace the placeholders with the actual repository URL and folder name.

**2. Create a virtual environment**

```bash
python -m venv .venv
```

**3. Activate the virtual environment**

On macOS or Linux:

```bash
source .venv/bin/activate
```

On Windows:

```bash
.venv\Scripts\activate
```

**4. Install the dependencies**

```bash
pip install -r requirements.txt
```

**5. Check the upload directory**

The application saves uploaded images in `static/uploaded image`. Make sure this directory exists before running the application.

**6. Run the application**

```bash
python app.py
```

Open the local address printed in the terminal in your web browser.

The application expects the saved model file `first_model (3).keras` to be available at the path specified in `app.py`. Additional configuration may be necessary depending on the Python and package versions installed.

## Limitations and Future Improvements

This project demonstrates an educational application of deep learning to mammography image classification. It has not been established as a clinically validated diagnostic system and should not be used to make medical decisions.

Potential future improvements include:

- Evaluating the model using appropriate performance metrics on a separate test dataset.
- Improving image upload validation and error handling.
- Improving account security by securely hashing passwords and strengthening application configuration.
- Improving the interface and making the application easier to deploy and maintain.

## Acknowledgments

We acknowledge the publicly available mammography image dataset obtained from Kaggle that supported the model development. 
https://www.kaggle.com/datasets/hayder17/breast-cancer-detection

## Disclaimer

This project is intended for educational and demonstration purposes only. Its predictions are not a substitute for professional medical advice, diagnosis, or treatment.

