#https://cloud.google.com/natural-language/docs/setup#linux-or-macos
#https://www.youtube.com/watch?v=-13yIXiyFAs&ab_channel=sentdex

# Imports the Google Cloud client library
from google.cloud import language_v1

# Instantiates a client
client = language_v1.LanguageServiceClient()

# The text to analyze
text = "Hello World!"
document = language_v1.Document(
    content=text, type_=language_v1.Document.Type.PLAIN_TEXT
)

# Detects the sentiment of the text
sentiment = client.analyze_sentiment(
    request={"document": document}
).document_sentiment

print(sentiment.score)

#print("Text: {}".format(text))
#print("Sentiment: {}, {}".format(sentiment.score, sentiment.magnitude))