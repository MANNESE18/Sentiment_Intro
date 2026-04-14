
import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

imported_sentences = input("Enter the file name for the news sentences:").strip()
info = pd.read_csv(imported_sentences, encoding = 'latin1')
info.columns = ['Sentiment_Provided', 'News']

analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    Score = analyzer.polarity_scores(str(text))
    return Score['compound']

info['Sentiment_Score'] = info['News'].apply(get_sentiment)

def get_label_1(score):
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

def get_label_2(score):
    if score >= 0.5:
        return 'Positive'
    elif score <= -0.5:
        return 'Negative'
    else:
        return 'Neutral'

info['Sentiment_Label_1'] = info['Sentiment_Score'].apply(get_label_1)
info['Sentiment_Label_2'] = info['Sentiment_Score'].apply(get_label_2)

label_counts_1 = info['Sentiment_Label_1'].value_counts()
label_counts_2 = info['Sentiment_Label_2'].value_counts()

print(label_counts_1)
print(label_counts_2)








