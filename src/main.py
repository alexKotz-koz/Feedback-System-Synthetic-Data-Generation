import os
import json

from components.generateSyntheticData import (
    generateClinicalApplicationFeedback,
    generateStudentFeedback,
    generateStudentFeedbackAttributed,
    generateRandomSentiment,
)

from components.convertSyntheticData import (
    convertStudentFeedbackData,
    convertClinicalApplicationFeedbackData,
)

from components.feedbackAnalysis import (
    downloadNLTK,
    wordCount,
    importData,
    preprocessText,
    getSentiment,
    setAnalysis,
    cafAnalysis,
)

"""
Abbreviations: 
- CAF: Clinical Application Feedback (Clinical Decision Support Tools or Healthcare Applications)
- SET: Student Evaluations of Teaching Feedback
"""


def setAPI():
    cwd = os.getcwd()
    secrets = os.path.join(cwd, "secrets")
    with open(f"{secrets}/api.env", "r") as file:
        api_key = file.readline().split("=")[1].strip("\n")
    os.environ["OPENAI_API_KEY"] = api_key


def main():
    setAPI()

    # temperature = 1.4

    ### Generate Feedback from DataDreamer
    # setOutputDirName = f"student-feedback-output-temp-{temperature}-d"
    # generateStudentFeedback(temperature=temperature, outputDirName=setOutputDirName)
    ##generateStudentFeedbackAttributed(temperature=0.5, outputDirName=setOutputDirName)

    # cafOutputDirName = f"clinical-application-feedback-output-temp-{temperature}-d"
    # generateClinicalApplicationFeedback(
    #    temperature=temperature, outputDirName=cafOutputDirName
    # )

    ### Clean and otherwise transform the data
    # convertStudentFeedbackData(setOutputDirName, f"student-feedback-data-temp-{temperature}-d.json")
    # convertClinicalApplicationFeedbackData(
    #    cafOutputDirName,
    #    f"clinical-application-feedback-data-temp-{temperature}-d.json",
    # )

    ### Feedback Analysis
    cwd = os.getcwd()
    dataDir = os.path.join(cwd, "data/1-d-converted-synthetic-data")
    cafResults = cafAnalysis(dataDir)

    with open("data/results/caf.json", "w") as file:
        json.dump(cafResults, file)

    setResults = setAnalysis(dataDir)
    with open("data/results/set.json", "w") as file:
        json.dump(setResults, file)


if __name__ == "__main__":
    main()
