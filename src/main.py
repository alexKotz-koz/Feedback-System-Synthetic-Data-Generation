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

from components.feedbackAnalysis import wordCount, importData


def setAPI():
    cwd = os.getcwd()
    secrets = os.path.join(cwd, "secrets")
    with open(f"{secrets}/api.env", "r") as file:
        api_key = file.readline().split("=")[1].strip("\n")
    os.environ["OPENAI_API_KEY"] = api_key


def main():
    setAPI()
    # generateStudentFeedback()
    # generateClinicalApplicationFeedback()
    """convertStudentFeedbackData(
        "student-feedback-output-temp-.5", "student-feedback-data-2.json"
    )
    convertClinicalApplicationFeedbackData(
        "clinical-application-feedback-output-temp-.5",
        "clinical-application-feedback-data-2.json",
    )"""

    cwd = os.getcwd()
    dataDir = os.path.join(cwd, "data")

    clinicalApplicationFeedbackDataFilepath = os.path.join(
        dataDir, "clinical-application-feedback-data.json"
    )
    clinicalApplicationFeedbackData2Filepath = os.path.join(
        dataDir, "clinical-application-feedback-data-2.json"
    )

    clinicalApplicationFeedbackData = importData(
        clinicalApplicationFeedbackDataFilepath
    )
    clinicalApplicationFeedbackData2 = importData(
        clinicalApplicationFeedbackData2Filepath
    )

    clinicalApplicationFeedbackNumWords, clinicalApplicationFeedbackAvgWords = (
        wordCount(clinicalApplicationFeedbackData)
    )

    clinicalApplicationFeedback2NumWords, clinicalApplicationFeedback2AvgWords = (
        wordCount(clinicalApplicationFeedbackData2)
    )

    print(
        f"Total Word Count clinicalApplicationFeedback: {clinicalApplicationFeedbackNumWords}"
    )
    print(
        f"Avg Word Count clinicalApplicationFeedback: {clinicalApplicationFeedbackAvgWords}"
    )

    print(
        f"Total Word Count clinicalApplicationFeedback2: {clinicalApplicationFeedback2NumWords}"
    )
    print(
        f"Avg Word Count clinicalApplicationFeedback: {clinicalApplicationFeedback2AvgWords}"
    )


if __name__ == "__main__":
    main()
