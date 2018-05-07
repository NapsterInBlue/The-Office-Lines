import pandas as pd
import re

def clean_line_text(df):
    badChars = re.compile('[^A-Z \-?\.&\'\[\],*!\%]', re.I)
    df['line_text'] = df['line_text'].map(lambda x: badChars.sub('', x))
    return df

def clean_speaker_names(df):
    df['speaker'] = df['speaker'].str.strip().str.lower()
    return df



def drop_deleted_scenes(df):
    df = df[df['deleted'] == False]
    del df['deleted']
    return df.reset_index(drop=True)


def do_all_data_loading():
    df = pd.read_csv('data/the-office-lines-scripts.csv')
    df = clean_line_text(df)
    df = clean_speaker_names(df)
    df = drop_deleted_scenes(df)


