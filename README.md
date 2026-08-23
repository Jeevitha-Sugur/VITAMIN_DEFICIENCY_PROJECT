Vitamin Deficiency Detection 🩺

📌 Project Overview

Vitamin Deficiency Detection is a machine learning-based web application that predicts a possible vitamin deficiency based on user-selected symptoms.

The application uses a Random Forest Classifier trained on symptom-related data and provides predictions through an interactive Streamlit web interface.

«Note: This project is developed for educational purposes and should not be considered a substitute for professional medical diagnosis.»

🎯 Objective

The objective of this project is to develop a simple and user-friendly application that can identify a possible vitamin deficiency based on common symptoms.

✨ Features

- 🩺 Symptom-based input
- 🤖 Machine learning prediction
- 🌳 Random Forest Classifier
- 🖥️ Interactive Streamlit interface
- ⚡ Instant prediction
- 📊 CSV-based dataset
- 💾 Pre-trained model stored using Pickle

🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Streamlit
- Pickle
- CSV

📂 Project Structure

VITAMIN_DEFICIENCY_PROJECT/
│
├── app/
│   └── app.py
│
├── data/
│   └── dataset.csv
│
├── model/
│   ├── train_model.py
│   └── model.pkl
│
└── README.md

🔍 Symptoms Used

The application takes the following symptoms as input:

- Fatigue
- Pale Skin
- Hair Loss
- Bone Pain
- Vision Problem

Each symptom can be selected using the Streamlit interface.

⚙️ How It Works

1. The user selects values for different symptoms.
2. The selected symptoms are provided as input to the machine learning model.
3. The trained Random Forest Classifier analyzes the input.
4. The application predicts a possible vitamin deficiency.
5. The result is displayed on the Streamlit interface.

Example Output

Possible Deficiency: Vitamin A

🧠 Machine Learning Model

The project uses a Random Forest Classifier for prediction.

The trained model is saved as:

model/model.pkl

The model is trained using the dataset available in:

data/dataset.csv

🚀 How to Run the Project

1. Clone the repository

git clone https://github.com/Jeevitha-Sugur/VITAMIN_DEFICIENCY_PROJECT.git

2. Navigate to the project folder

cd VITAMIN_DEFICIENCY_PROJECT

3. Install the required libraries

pip install pandas scikit-learn streamlit

4. Run the application

python -m streamlit run app/app.py
or
py -m streamlit run app/app.py

The Streamlit application will open in your web browser.

📊 Example

The user selects symptom values such as:

- Fatigue
- Pale Skin
- Hair Loss
- Bone Pain
- Vision Problem

After clicking the Predict button, the application displays a possible vitamin deficiency.

🔮 Future Improvements

- Add more symptoms and vitamin deficiencies.
- Use a larger and more diverse dataset.
- Improve prediction accuracy.
- Add prediction confidence scores.
- Improve the user interface.
- Deploy the application online.
- Provide general information about each vitamin deficiency.

⚠️ Disclaimer

This application is intended for educational and demonstration purposes only. The prediction should not be considered a medical diagnosis. Users should consult a qualified healthcare professional for medical advice.

👩‍💻 Author

Jeevitha Sugur

GitHub: https://github.com/Jeevitha-Sugur
