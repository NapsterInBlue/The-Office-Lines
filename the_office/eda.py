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
