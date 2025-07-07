import streamlit as st
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

nltk.download('vader_lexicon')
analyzer = SentimentIntensityAnalyzer()

st.title("🏨 Hotel Review Sentiment Analyzer")

user_input = st.text_area("✍️ Write your hotel review here:")

if st.button("Analyze"):
    score = analyzer.polarity_scores(user_input)
    st.write("### Sentiment Scores")
    st.json(score)

    if score['pos'] > score['neg'] and score['pos'] > score['neu']:
        st.success("✅ Sentiment: Positive 😊")
    elif score['neg'] > score['pos'] and score['neg'] > score['neu']:
        st.error("❌ Sentiment: Negative 😠")
    else:
        st.info("😐 Sentiment: Neutral 🙂")
