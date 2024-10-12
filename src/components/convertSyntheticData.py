import os
import json
from components.cleanSyntheticData import (
    extractStudentFeedbackData,
    extractClinicalApplicationFeedbackData,
)


def convertStudentFeedbackData(syntheticFileName, outputFileName):
    cwd = os.getcwd()

    # DataDreamer Directory
    dataDreamerDir = os.path.join(cwd, "data-dreamer-output")
    studentFeedbackOutputDir = os.path.join(dataDreamerDir, syntheticFileName)
    cacheDir = os.path.join(studentFeedbackOutputDir, ".cache")
    dbFile = os.path.join(cacheDir, "OpenAI_gpt-4_d943856c9b1e8f80.db")

    # Extracted Data Directory
    dataDir = os.path.join(cwd, "data")
    syntheticDataDir = os.path.join(dataDir, "1-c-converted-synthetic-data")
    os.makedirs(syntheticDataDir, exist_ok=True)

    extractedStudentFeedbackData = extractStudentFeedbackData(dbFile)

    studentFeedbackFile = os.path.join(syntheticDataDir, outputFileName)

    with open(studentFeedbackFile, "w") as f:
        json.dump(extractedStudentFeedbackData, f, indent=4)


def convertClinicalApplicationFeedbackData(syntheticFileName, outputFileName):
    cwd = os.getcwd()

    # DataDreamer Directory
    dataDreamerDir = os.path.join(cwd, "data-dreamer-output")
    clinicalApplicationOutputDir = os.path.join(dataDreamerDir, syntheticFileName)
    cacheDir = os.path.join(clinicalApplicationOutputDir, ".cache")
    dbFile = os.path.join(cacheDir, "OpenAI_gpt-4_d943856c9b1e8f80.db")

    # Extracted Data Directory
    dataDir = os.path.join(cwd, "data")
    syntheticDataDir = os.path.join(dataDir, "1-c-converted-synthetic-data")
    os.makedirs(syntheticDataDir, exist_ok=True)

    extractedClinicalApplicationFeedbackData = extractClinicalApplicationFeedbackData(
        dbFile
    )

    clinicalApplicationFeedbackFile = os.path.join(syntheticDataDir, outputFileName)
    with open(clinicalApplicationFeedbackFile, "w") as f:
        json.dump(extractedClinicalApplicationFeedbackData, f, indent=4)
