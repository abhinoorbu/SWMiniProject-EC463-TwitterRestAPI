#https://cloud.google.com/natural-language/docs/setup#linux-or-macos
#https://www.youtube.com/watch?v=-13yIXiyFAs&ab_channel=sentdex

# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "The 2022 Apple Event was a great success. Apple launched many new iPhones, and other devices. The airpods pro gen 2 look really cool. The apple watch ultra is very expensive, but also very cool!"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

response = client.classify_text(document=document)
for category in response.categories:
        print("=" * 80)
        print(f"category  : {category.name}")
        print(f"confidence: {category.confidence:.0%}")

print(sentiment.score)

#print("Text: {}".format(text))
#print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))