import streamlit as st
import joblib

model = joblib.load("sentiment_model.pkl")

st.title("🎬 Movie Review Sentiment Analysis")

review = st.text_area("Enter a movie review:")

if st.button("Predict Sentiment"):
    if review.strip():
        prediction = model.predict([review])[0]
        probabilities = model.predict_proba([review])[0]

        sentiment = "Positive" if prediction == 1 else "Negative"
        confidence = probabilities.max()

        st.success(f"Prediction: {sentiment}")
        st.write(f"Confidence: {confidence:.2%}")
    else:
        st.warning("Please enter a review.")