import os
import json

from components.generateSyntheticData import (
    generateClinicalApplicationFeedback,
    generateStudentFeedback,
)

from components.cleanSyntheticData import (
    extractStudentFeedbackData,
    extractClinicalApplicationFeedbackData,
)


def setAPI():
    cwd = os.getcwd()
    secrets = os.path.join(cwd, "secrets")
    with open(f"{secrets}/api.env", "r") as file:
        api_key = file.readline().split("=")[1].strip("\n")
    os.environ["OPENAI_API_KEY"] = api_key


def studentFeedbackData():
    cwd = os.getcwd()

    # DataDreamer Directory
    studentFeedbackOutputDir = os.path.join(os.getcwd(), "student-feedback-output")
    cacheDir = os.path.join(studentFeedbackOutputDir, ".cache")
    dbFile = os.path.join(cacheDir, "OpenAI_gpt-4_d943856c9b1e8f80.db")

    # Extracted Data Directory
    dataDir = os.path.join(cwd, "data")

    extractedStudentFeedbackData = extractStudentFeedbackData(dbFile)

    studentFeedbackFile = os.path.join(dataDir, "student-feedback-data.json")
    with open(studentFeedbackFile, "w") as f:
        json.dump(extractedStudentFeedbackData, f, indent=4)


def clinicalApplicationData():
    cwd = os.getcwd()

    # DataDreamer Directory
    clinicalApplicationOutputDir = os.path.join(
        os.getcwd(), "clinical-application-feedback-output"
    )
    cacheDir = os.path.join(clinicalApplicationOutputDir, ".cache")
    dbFile = os.path.join(cacheDir, "OpenAI_gpt-4_d943856c9b1e8f80.db")

    # Extracted Data Directory
    dataDir = os.path.join(cwd, "data")

    extractedClinicalApplicationFeedbackData = extractClinicalApplicationFeedbackData(
        dbFile
    )

    clinicalApplicationFeedbackFile = os.path.join(
        dataDir, "clinical-application-feedback-data.json"
    )
    with open(clinicalApplicationFeedbackFile, "w") as f:
        json.dump(extractedClinicalApplicationFeedbackData, f, indent=4)


def main():
    setAPI()
    # generateStudentFeedback()
    # generateClinicalApplicationFeedback()
    # studentFeedbackData()
    clinicalApplicationData()


if __name__ == "__main__":
    main()
