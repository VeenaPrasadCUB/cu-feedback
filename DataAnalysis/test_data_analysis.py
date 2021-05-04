# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import unittest
from data_analysis import *
from unittest.mock import patch
from collections import Counter
import pandas as pd
import numpy as np


class TestStringMethods(unittest.TestCase):

    # unit test for testing compute_sentiment
    def test_compute_sentiment(self):
        self.assertEqual(compute_sentiment('Hi example test'), 'neutral')
        self.assertEqual(compute_sentiment('Good'), 'positive')
        self.assertEqual(compute_sentiment('Bad'), 'negative')
    
    #acceptance test for data_analysis file
    def test_calculate_scores(self):
        scores_list = calculate_scores()
        expected_results = [Counter({5: 14, 4: 8, 3: 6, 1: 0, 2: 0}),
                            Counter({4: 15, 3: 7, 5: 5, 1: 1, 2: 0}),
                            Counter({3: 10, 4: 10, 5: 5, 2: 2, 1: 1}),
                            {'ta_average_rating': 4.68, 'ta_max_rating': 5.0, 'ta_min_rating': 3.0},
                            {'negative': 1, 'neutral': 15, 'positive': 12}]
        self.assertEqual(len(scores_list), 5)
        self.assertNotEqual(len(scores_list), 10)
        self.assertEqual(scores_list, expected_results)
    
    # Unit test to demonstrate mocking of read_data function present in the data_analysis module. 
    
    @patch('data_analysis.read_data')
    def test_calculate_scores_using_mock(self, mocked_obj):
        
        data = pd.DataFrame()
        num_responses = 10
        sample_comments = ['no comment, good job','more examples please','slow down, we cannot keep up',
                   'na','none','',
                   'slower!','share your slides please','you\'re doing great!']
        response_values = [1]
        data['Timestamp'] = np.random.choice(['', ''], num_responses)
        data['How comfortable are you working with arrays?'] = np.random.choice(response_values, num_responses)
        data['How comfortable are you working with pointers?'] = np.random.choice(response_values, num_responses)
        data['How comfortable are you working with Linked Lists?'] = np.random.choice(response_values, num_responses)
        data['How would you rate your TA?'] = np.random.choice(response_values, num_responses)
        data['If you could improve one thing about Recitation, what would it be?'] = np.random.choice(sample_comments, num_responses)
        mocked_obj.return_value = data
        input_data = pd.read_csv('sample_data.csv')
        input_data = input_data.fillna('.')
        self.assertEqual(read_data('sample_data.csv')['How would you rate your TA?'][0], input_data['How would you rate your TA?'][0])


    #integration test to check read_data and populate_dictionary modules are integrated correctly.
    def test_integration(self):
        input_data = read_data('sample_data.csv')
        array_scores = input_data['How comfortable are you working with arrays?']
        array_scores_aggregate = Counter(array_scores)
        expected_array_scores_aggregate = Counter({5: 14, 4: 8, 3: 6})
        self.assertEqual(expected_array_scores_aggregate, array_scores_aggregate)
        actual_results = populate_dictionary(array_scores_aggregate)
        expected_results = None
        self.assertEqual(actual_results, expected_results)
    
if __name__ == '__main__':
    unittest.main()