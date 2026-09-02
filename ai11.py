from textblob import TextBlob
text = input("Enter a sentence for sentiment analysis: ")
blob = TextBlob(text)
polarity = blob.sentiment.polarity
subjectivity = blob.sentiment.subjectivity
if polarity > 0:
    sentiment = "Positive"
elif polarity < 0:
    sentiment = "Negative"
else:
    sentiment = "Neutral"
print(f"Sentiment: {sentiment}")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")
print("Thank you for using the sentiment analysis tool!")