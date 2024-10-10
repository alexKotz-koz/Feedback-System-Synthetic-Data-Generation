import os
import json
import pandas as pd


def wordCount(data):
    totalNumWords = 0
    for feedback in data["feedback"]:
        totalNumWords += len(feedback.split())
    averageNumWords = totalNumWords / len(data)
    return totalNumWords, averageNumWords


def importData(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    data = pd.DataFrame.from_dict(data, orient="index")
    return data
