import os
import json
from components.cleanSyntheticData import (
    extractStudentFeedbackData,
    extractClinicalApplicationFeedbackData,
)


def convertStudentFeedbackData(syntheticDataDir, outputFileName):
    cwd = os.getcwd()

    # DataDreamer Directory
    studentFeedbackOutputDir = os.path.join(cwd, syntheticDataDir)
    cacheDir = os.path.join(studentFeedbackOutputDir, ".cache")
    dbFile = os.path.join(cacheDir, "OpenAI_gpt-4_d943856c9b1e8f80.db")

    # Extracted Data Directory
    dataDir = os.path.join(cwd, "data")

    extractedStudentFeedbackData = extractStudentFeedbackData(dbFile)

    studentFeedbackFile = os.path.join(dataDir, outputFileName)
    with open(studentFeedbackFile, "w") as f:
        json.dump(extractedStudentFeedbackData, f, indent=4)


def convertClinicalApplicationFeedbackData(syntheticDataDir, outputFileName):
    cwd = os.getcwd()

    # DataDreamer Directory
    clinicalApplicationOutputDir = os.path.join(cwd, syntheticDataDir)
    cacheDir = os.path.join(clinicalApplicationOutputDir, ".cache")
    dbFile = os.path.join(cacheDir, "OpenAI_gpt-4_d943856c9b1e8f80.db")

    # Extracted Data Directory
    dataDir = os.path.join(cwd, "data")

    extractedClinicalApplicationFeedbackData = extractClinicalApplicationFeedbackData(
        dbFile
    )

    clinicalApplicationFeedbackFile = os.path.join(dataDir, outputFileName)
    with open(clinicalApplicationFeedbackFile, "w") as f:
        json.dump(extractedClinicalApplicationFeedbackData, f, indent=4)
