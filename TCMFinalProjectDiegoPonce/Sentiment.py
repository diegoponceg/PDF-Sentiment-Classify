# Imports the Google Cloud client library
from google.cloud import language
from google.cloud.language import enums
from google.cloud.language import types
import os
import Classify


def sentimentan(pdftext):
    # the path to your credentials, otherwise use mine which can be found in the .json file. Make sure the path is correct
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "/Users/diegoponce/Desktop/TCMFinalProjectDiegoPonce/MyCredentials.json"
    client = language.LanguageServiceClient()
    text = pdftext
    document = types.Document(
    content=text,
    type=enums.Document.Type.PLAIN_TEXT)
    sentiment = client.analyze_sentiment(document=document).document_sentiment

    print('Text: {}'.format(text))
    print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))

    Classify.classify(text)