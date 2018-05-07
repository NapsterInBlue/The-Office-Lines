import pandas as pd
import numpy as np
import re

def filter_cast(df, minLines=100):
    lineCounts = df['speaker'].value_counts()
    importantPeople = lineCounts[lineCounts > minLines].index

    filtered = df[df['speaker'].isin(importantPeople)]

    return filtered.reset_index(drop=True)


def get_cast_by_scene(df):
    gb = df.groupby(['season', 'episode', 'scene'])

    # Each record will be a list of every present character
    s = gb['speaker'].unique().reset_index(drop=True)

    # Each record is at the present (scene, character) level
    tallCastByScene = s.apply(pd.Series).stack()

    # Consolidate each scene to one row
    castByScene = pd.get_dummies(tallCastByScene).sum(level=0)

    return castByScene

def shared_scene_matrix(castByScene):
    '''
    Pairwise number of shared scenes by character,
    trimmed to a lower-triangular matrix
    '''
    pairs = {char:None for char in castByScene}

    for char in castByScene:
        pairs[char] = castByScene[castByScene[char] > 0].sum()

    pairValues = pd.DataFrame(pairs)
    return np.tril(pairValues, k=-1)
