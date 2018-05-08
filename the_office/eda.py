import pandas as pd
import re

def line_search(df, line, speaker=None):
    if speaker:
        speaker = df['speaker'] == speaker
    else:
        speaker = True

    line = line.replace(' ', '\s*')
    line = df['line_text'].str.contains(line, regex=True, flags=re.I)

    return df[line & speaker]


def get_dialogue(df, season, episode, scenes=None):
    season = df['season'] == season
    episode = df['episode'] == episode

    if scenes:
        if type(scenes) != list:
            scenes = [scenes]
        else:
            scenes = list(range(*scenes))

        scenes = df['scene'].isin(scenes)
    else:
        scenes = True

    return df[season & episode & scenes]

def a_spoke_after_b(df, personA, personB):
    sameScene = (df.groupby(['season', 'episode'])['scene']
                   .transform(_within_two_scenes))
    aAfterB = (df.groupby(['season', 'episode'])['speaker']
                   .transform(lambda x: _within_two_lines(x, personA, personB)))

    return sameScene & aAfterB


def _within_two_lines(col, personA, personB):
    a = col == personA
    b = col.shift(1) == personB
    c = col.shift(2) == personB

    return a & (b | c)

def _within_two_scenes(col):
    return (col - col.shift(2)) < 2
