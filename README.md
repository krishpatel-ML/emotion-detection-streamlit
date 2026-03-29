🤖 Emotion Detection App (Streamlit)

A machine learning web application that classifies text into emotions like sadness, anger, love, surprise, fear, and joy using Logistic Regression.

---

🚀 Features

- 🔍 Real-time text emotion prediction
- 📊 Displays prediction confidence
- 📈 Visualizes probabilities using charts
- 🎨 Clean and interactive UI built with Streamlit
- ⚡ Fast and lightweight model

---

🧠 Model Details

- Algorithm: Logistic Regression
- Text Vectorization: TF-IDF
- Classes:
  - Sadness 😢
  - Anger 😠
  - Love ❤️
  - Surprise 😲
  - Fear 😨
  - Joy 😄

---

🏗️ Project Structure

emotion-detection-streamlit/
│
├── app.py
├── model.joblib
├── vectorizer.joblib
├── requirements.txt
├── README.md

---

⚙️ Installation & Setup

1. Clone the repository

git clone https://github.com/krishpatel-ML/emotion-detection-streamlit
cd emotion-detection-streamlit

2. Install dependencies

pip install -r requirements.txt

3. Run the app

streamlit run app.py

---

🧪 Example Input

I am feeling very happy and excited today!

👉 Output: Joy 😄

---

📊 How It Works

1. User inputs text
2. Text is transformed using TF-IDF
3. Logistic Regression model predicts emotion
4. Output is displayed with confidence score

---

🛠️ Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- Joblib

---

👨‍💻 Author

Krish
Made with ❤️ using Streamlit

---

⭐ Future Improvements

- Add file upload (CSV prediction)
- Deploy on cloud (Streamlit Cloud)
- Improve model accuracy with advanced NLP models

---

📌 Notes

- Ensure "model.joblib" and "vectorizer.joblib" are in the same directory as "app.py"
- Use the same preprocessing as training data

---
