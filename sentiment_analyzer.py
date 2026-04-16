print("Simple AI Sentiment Analyzer")

text = input("Enter a sentence: ").lower()

positive_words = ["good", "happy", "great", "excellent", "nice"]
negative_words = ["bad", "sad", "worst", "angry", "poor"]

if any(word in text for word in positive_words):
    print("Positive sentiment 😊")
elif any(word in text for word in negative_words):
    print("Negative sentiment 😢")
else:
    print("Neutral sentiment 😐")