import streamlit as st
import joblib
import pandas as pd

# Page settings
st.set_page_config(page_title="Emotion Classifier", page_icon="🤖", layout="centered")

# Load model and vectorizer
model = joblib.load("model.joblib")
vectorizer = joblib.load("vectorizer.joblib")

# Emotion labels mapping
labels = {
    0: "Sadness 😢",
    1: "Anger 😠",
    2: "Love ❤️",
    3: "Surprise 😲",
    4: "Fear 😨",
    5: "Joy 😄"
}

# Custom UI styling
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
    font-size: 16px;
    border-radius: 8px;
    height: 3em;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h2 style='text-align: center;'>🤖 Emotion Detection App</h2>
<p style='text-align: center; color: gray;'>Made by <b>Krish</b></p>
""", unsafe_allow_html=True)

st.markdown("---")

# Input
user_input = st.text_area("✍️ Enter your text:", height=150)

# Predict button
if st.button("🔍 Predict"):
    if user_input.strip() != "":
        
        # Transform input
        input_data = vectorizer.transform([user_input])

        # Prediction
        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)

        predicted_label = labels[prediction[0]]
        confidence = max(probability[0]) * 100

        # Result
        st.markdown("### 📊 Result")
        st.success(f"Prediction: {predicted_label}")
        st.info(f"Confidence: {confidence:.2f}%")

        # Show probabilities
        st.markdown("### 📈 Emotion Probabilities")

        prob_df = pd.DataFrame({
            "Emotion": list(labels.values()),
            "Probability": probability[0]
        })

        st.bar_chart(prob_df.set_index("Emotion"))

    else:
        st.error("⚠️ Please enter some text")

# Footer
st.markdown("---")
st.caption("© 2026 Made by Krish")