from __future__ import print_function

import random
import sqlite3

import pandas as pd
from download_sheet_to_csv import download_sheet_to_csv
from get_api_services import get_api_services
from get_spreadsheet_id import get_spreadsheet_id


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
csv_name = "Form Responses 1.csv"

sample_comments = ['no comment, good job','more examples please','slow down, we cannot keep up',
                   'na','none','',
                   'slower!','share your slides please','you\'re doing great!']


def simulate_survey(ta_name):
    taid = ''
    if ta_name == 'Jay':
        taid = 'jalu'
    elif ta_name == 'Nischal':
        taid = 'nipa'
    elif ta_name == 'Pradyoth':
        taid = 'prsr'
    elif ta_name == 'Shruthi':
        taid = 'shsr'
    else:
        taid = 'vepr'

    data_line = []
    conn = connect_to_db()
    for i in range(10):
        data_line = [taid, 'CSCI5828_S21',random.randint(1,5), random.randint(1,5),
                     random.randint(1,5), random.randint(1,5), sample_comments[i]]

        sql_command = 'INSERT INTO survey_data (ta_cuid, cct, response_1, response_2, ' \
                      'response_3, performance_rating, comment) VALUES %r;' % tuple(data_line)
        conn.execute(sql_command)

    conn.close()


def connect_to_db():
    conn = None
    try:
        conn = sqlite3.connect('raw_data.db')
    except Exception as e:
        print(e)

    return conn


def download_spreadsheet_as_csv(spreadsheet_name):

    drive, sheets = get_api_services()

    spreadsheet_id = get_spreadsheet_id(drive, spreadsheet_name)

    download_sheet_to_csv(sheets, spreadsheet_id, "Form Responses 1")


def import_data():
    df = pd.read_csv("Form Responses 1.csv")
    columns = df.columns
    topic1 = columns[3].split(' ')[-2]
    topic2 = columns[4].split(' ')[-2]
    topic3 = columns[5].split(' ')[-2]
    # I'll finish the rest later, when I complete the unit tests. This functionality is
    # not necessary for the demo.
