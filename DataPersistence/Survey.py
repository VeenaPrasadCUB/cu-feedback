from __future__ import print_function

import pandas as pd
import numpy as np
from download_sheet_to_csv import download_sheet_to_csv
from get_api_services import get_api_services
from get_spreadsheet_id import get_spreadsheet_id

from db import Database

db = Database()
db.start_db()

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
csv_name = "sample_data.csv"

sample_comments = ['no comment, good job','more examples please','slow down, we cannot keep up',
                   'na','none','',
                   'slower!','share your slides please','you\'re doing great!']


def simulate_survey():
    conn = connect_to_db()
    data = pd.DataFrame()
    num_responses = 25
    response_values = [1, 2, 3, 4, 5]
    data['timestamp'] = np.random.choice(['', ''], num_responses)
    data['response_1'] = np.random.choice(response_values, num_responses)
    data['response_2'] = np.random.choice(response_values, num_responses)
    data['response_3'] = np.random.choice(response_values, num_responses)
    data['performance_rating'] = np.random.choice(response_values, num_responses)
    data['comment'] = np.random.choice(sample_comments, num_responses)

    # For the MVP
    data.to_csv(csv_name, index=False)

    # For the ensuing project
    data.to_sql('survey_data', conn, if_exists='replace', index=True)

    conn.close()


def connect_to_db():
    started = db.start_db()
    return started


def download_spreadsheet_as_csv(spreadsheet_name):

    drive, sheets = get_api_services()

    spreadsheet_id = get_spreadsheet_id(drive, spreadsheet_name)

    download_sheet_to_csv(sheets, spreadsheet_id, "Form Responses 1")


def import_data():
    df = pd.read_csv("Form Responses 1.csv")
    df.to_sql()
