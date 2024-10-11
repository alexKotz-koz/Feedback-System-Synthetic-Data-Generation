import os
import json

from components.generateSyntheticData import (
    generateClinicalApplicationFeedback,
    generateStudentFeedback,
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

    ### Generate Feedback from DataDreamer

    # setOutputDirName = "student-feedback-output-temp-.8"
    # setOutputDirName = "student-feedback-output-temp-.5"
    # setOutputDirName = "student-feedback-output-temp-.2"
    setOutputDirName = "student-feedback-output-temp-1.1"
    # generateStudentFeedback(temperature=1.1, outputDirName=setOutputDirName)

    # cafOutputDirName = "clinical-application-feedback-output-temp-.8"
    # cafOutputDirName = "clinical-application-feedback-output-temp-.5"
    # cafOutputDirName = "clinical-application-feedback-output-temp-.2"
    # cafOutputDirName = "clinical-application-feedback-output-temp-1.1"
    # generateClinicalApplicationFeedback(temperature=1.1, outputDirName=cafOutputDirName)

    ### Clean and otherwise transform the data
    convertStudentFeedbackData(setOutputDirName, "student-feedback-data-temp-1.1.json")
    # convertClinicalApplicationFeedbackData(cafOutputDirName, "clinical-application-feedback-data-temp-1.1.json")

    ### Feedback Analysis
    """cwd = os.getcwd()
    dataDir = os.path.join(cwd, "data")
    cafAnalysis(dataDir)
    setAnalysis(dataDir)
"""


if __name__ == "__main__":
    main()
