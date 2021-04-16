import nltk
import pandas as pd
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
sia = SentimentIntensityAnalyzer()

def compute_sentiment(review_text: str):
    sentiment = ''
    compound_score = sia.polarity_scores(review_text)["compound"]
    if compound_score < -0.25 :
      sentiment = 'negative'
    elif compound_score >= -0.25 and compound_score <= 0.25:
      sentiment = 'neutral'
    else:
      sentiment = 'positive'
    return sentiment

def read_data(filename):
  input_data = pd.read_csv(filename)
  input_data = input_data.fillna('.')
  return input_data

def populate_dictionary(scores_aggregate):
  s = set({1, 2, 3, 4, 5})
  for number in s :
    if number not in scores_aggregate.keys():
      scores_aggregate[number] = 0

def calculate_scores():
  input_data = read_data('sample_data.csv')
  array_scores = input_data['How comfortable are you working with arrays?']
  pointer_scores = input_data['How comfortable are you working with pointers?']
  linked_list_scores = input_data['How comfortable are you working with Linked Lists?']
  ta_ratings = input_data['How would you rate your TA?']
  recitation_text = input_data['If you could improve one thing about Recitation, what would it be?']
  array_scores_aggregate = Counter(array_scores)
  linked_list_scores_aggregate = Counter(linked_list_scores)
  pointer_scores_aggregate = Counter(pointer_scores)
  populate_dictionary(array_scores_aggregate)
  populate_dictionary(pointer_scores_aggregate)
  populate_dictionary(linked_list_scores_aggregate)
  agg = ta_ratings.agg(['min', 'max', 'average'])
  ta_max_rating = round((float) (agg['max']), 2)
  ta_min_rating = round((float) (agg['min']), 2)
  ta_average_rating =  round((float) (agg['average']), 2)
  ta_scores = {"ta_max_rating" : ta_max_rating, "ta_min_rating" :ta_min_rating, "ta_average_rating" : ta_average_rating}
  polarity_dictionary = {} 
  for text in recitation_text:
    sentiment = compute_sentiment(text)
    polarity_dictionary[sentiment] = polarity_dictionary.get(sentiment, 0) + 1
    
  return [array_scores_aggregate, pointer_scores_aggregate, linked_list_scores_aggregate, ta_scores, polarity_dictionary]

def main():
  scores = calculate_scores()
  array_scores_aggregate, pointer_scores_aggregate, linked_list_scores_aggregate, ta_scores, polarity_dictionary = scores[0], scores[1], scores[2], scores[3], scores[4]
  print('array scores {}'.format(array_scores_aggregate))
  print('pointer scores {}'.format(pointer_scores_aggregate))
  print('linked list scores {}'.format(linked_list_scores_aggregate))
  print('TA Scores {}' .format(ta_scores))
  print('Polarity Dictionary {}' .format(polarity_dictionary))

from elasticsearch import Elasticsearch


def get_es_credentials():
  return {
      "user": "elastic", 
      "password": "s5B0DDHP35MTfvYLvnPx1afX",
      "cloud_id": "fos-project:dXMtd2VzdDEuZ2NwLmNsb3VkLmVzLmlvJGYwYjZlYzVhYzlkNTQ3ZmY5NWQ3Yjg0YmNlN2Q5MDM1JDFhNWMyNzBlYzk1NjQwOGQ5ZGM4MTUxMjMyNDdhMWM0"
    }

ELASTIC_SETTINGS = get_es_credentials()

def es():
  es = Elasticsearch(
      cloud_id=ELASTIC_SETTINGS["cloud_id"],
      http_auth=(ELASTIC_SETTINGS["user"], ELASTIC_SETTINGS["password"]),
  )

  ta_scores = {"ta_max_rating" : ta_max_rating, "ta_min_rating" :ta_min_rating, "ta_average_rating" : ta_average_rating}
  es.index(index='sw', doc_type='people', id=1, body= array_scores_aggregate)
  es.index(index='sw', doc_type='people', id=2, body= pointer_scores_aggregate)
  es.index(index='sw', doc_type='people', id=3, body= linked_list_scores_aggregate)
  es.index(index='sw', doc_type='people', id=4, body= ta_scores)
  es.index(index='sw', doc_type='people', id=5, body= polarity_dictionary)

  array_scores_1 = es.get(index='sw', doc_type='people', id=1)
  pointer_scores_1 = es.get(index='sw', doc_type='people', id=2)
  linked_list_scores_1 = es.get(index='sw', doc_type='people', id=3)
  ta_scores_1 = es.get(index='sw', doc_type='people', id=4)
  polarity_dictionary_1 = es.get(index='sw', doc_type='people', id=5)


  print(array_scores_1)
  print(pointer_scores_1)
  print(linked_list_scores_1)
  print(ta_scores_1)
  print(polarity_dictionary_1)

main()
print()
es()