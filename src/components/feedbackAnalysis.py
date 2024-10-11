import os
import json
import pandas as pd

from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# Only use to initialize nltk (first time use)
def downloadNLTK():
    import nltk

    nltk.download("all")


def importData(filepath):
    with open(filepath, "r") as file:
        data = json.load(file)
    data = pd.DataFrame.from_dict(data, orient="index")
    return data


def wordCount(data):
    totalNumWords = 0
    for feedback in data["feedback"]:
        totalNumWords += len(feedback.split())
    averageNumWords = totalNumWords / len(data)
    return totalNumWords, averageNumWords


def preprocessText(feedback):
    tokens = word_tokenize(feedback.lower())

    filteredTokens = [
        token for token in tokens if token not in stopwords.words("english")
    ]

    lemmatizer = WordNetLemmatizer()
    lemmatizedTokens = [lemmatizer.lemmatize(token) for token in filteredTokens]

    processedFeedback = " ".join(lemmatizedTokens)

    return processedFeedback


def getSentiment(feedback):
    analyzer = SentimentIntensityAnalyzer()
    scores = analyzer.polarity_scores(feedback)
    # sentiment = 1 if scores["pos"] > 0 else 0
    return scores


def cafAnalysis(dataDir):
    analyzedDir = os.path.join(dataDir, "2-b-sentiment-analyzed")
    os.makedirs(analyzedDir, exist_ok=True)

    for file in os.listdir(dataDir):
        filePath = os.path.join(dataDir, file)

        filename = filePath.split("/")[-1]
        temp = filename.split("-")[-2:]
        temp = "".join(temp).replace(".json", "")
        if os.path.isfile(filePath):
            if "clinical-application-feedback" in filePath:
                cafData = importData(filepath=filePath)
                cafNumWords, cafAvgWords = wordCount(cafData)
                print(
                    f"\nTotal Word Count clinicalApplicationFeedback-{temp}: {cafNumWords}"
                )
                print(
                    f"Avg Word Count clinicalApplicationFeedback-{temp}: {cafAvgWords}\n"
                )

                processedFeedback = cafData["feedback"].apply(preprocessText)
                cafData["sentiment"] = processedFeedback.apply(getSentiment)
                newFileName = f"clinicalApplicationFeedback-{temp}"
                newFilePath = os.path.join(analyzedDir, newFileName)
                cafData.to_json(f"{newFilePath}.json")


def setAnalysis(dataDir):
    analyzedDir = os.path.join(dataDir, "2-b-sentiment-analyzed")
    os.makedirs(analyzedDir, exist_ok=True)
    for file in os.listdir(dataDir):
        filePath = os.path.join(dataDir, file)

        filename = filePath.split("/")[-1]
        temp = filename.split("-")[-2:]
        temp = "".join(temp).replace(".json", "")
        if os.path.isfile(filePath):
            if "student-feedback" in filePath:
                setData = importData(filepath=filePath)
                setNumWords, setAvgWords = wordCount(setData)
                print(f"\nTotal Word Count studentFeedback-{temp}: {setNumWords}")
                print(f"Avg Word Count studentFeedback-{temp}: {setAvgWords}\n")

                processedFeedback = setData["feedback"].apply(preprocessText)
                setData["sentiment"] = processedFeedback.apply(getSentiment)
                newFileName = f"studentFeedback-{temp}"
                newFilePath = os.path.join(analyzedDir, newFileName)
                setData.to_json(f"{newFilePath}.json")
