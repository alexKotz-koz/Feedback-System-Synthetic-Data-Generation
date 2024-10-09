import os
import json
import pickle
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import DataFromPrompt
import sqlite3


def setAPI():
    cwd = os.getcwd()
    secrets = os.path.join(cwd, "secrets")
    with open(f"{secrets}/api.env", "r") as file:
        api_key = file.readline().split("=")[1].strip("\n")
    os.environ["OPENAI_API_KEY"] = api_key


def generateStudentFeedback():
    # session -- uses pythons context manager
    with DataDreamer("./student-feedback-output"):
        gpt4 = OpenAI(model_name="gpt-4")

        studentEvaluationFeedback = DataFromPrompt(
            "Generate Student Evalution Feedback",
            args={
                "llm": gpt4,
                "n": 20,
                "temperature": 0.8,
                "instruction": (
                    "Generate a student evaluation of teaching feedback comment of a graduate school course from the perspective of a student who has just completed the course.",
                    "Please make the number of words per comment follow an average of 64 with a standard deviation of 21.",
                    "Please format the data as: 'Course Name: {course_name} | Student Feedback: {student_feedback_comment}'",
                ),
            },
            outputs={"generations": "feedback"},
        )
        print(studentEvaluationFeedback)


def generateClinicalApplicationFeedback():
    with DataDreamer("./clinical-application-feedback-output"):
        gpt4 = OpenAI(model_name="gpt-4")

        clinicalApplicationFeedback = DataFromPrompt(
            "Generate Clinical Application Feedback",
            args={
                "llm": gpt4,
                "n": 20,
                "temperature": 0.8,
                "instruction": (
                    "Generate a review of a clinical decision support tool or health care application from the perspective of a practicing medical provider (e.g. doctor, physicans assistant, nurse, or medical assistant).",
                    "Please make the number of words per comment follow an average of x with a standard deviation of x.",
                    "Please format the data as: 'Name of Appplication/Tool: {name_of_app} | Application Review: {application_review}'",
                ),
            },
            outputs={"generations": "feedback"},
        )
        print(clinicalApplicationFeedback)


def cleanStudentFeedbackData(data):
    courseName = data.split("|")[0].strip()
    courseName = re.sub(r"^['\"]?Course Name: ?", "", courseName).strip()
    feedback = data.split("|")[1].strip()
    feedback = re.sub(r"^['\"]?Student Feedback: ?", "", feedback).strip()
    feedback = re.sub(r"Course Name:.*$", "", feedback).strip()
    feedback = re.sub(r"['\"\n]+$", "", feedback).strip()

    return courseName, feedback


def extractStudentFeedbackData(dbFile):
    # Connect to the SQLite database
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    extractedStudentFeedbackData = {}
    itr = 1
    for table in tables:
        table_name = table[0]
        # print(f"Table: {table_name}")

        # Fetch column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]
        # print("Columns:", column_names)

        # Fetch data
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        for row in rows[5:]:
            data = row[1]
            if isinstance(data, bytes):
                try:
                    data = pickle.loads(data)
                except pickle.UnpicklingError:
                    print("Error: Data could not be unpickled.")
                    continue

            try:
                courseName, feedback = cleanStudentFeedbackData(data)
            except:
                continue
            # Append to the list
            extractedStudentFeedbackData[itr] = {
                "course_name": courseName,
                "feedback": feedback,
            }
            itr += 1
    # Close the connection
    conn.close()
    return extractedStudentFeedbackData


def main():
    setAPI()
    # generateStudentFeedback()
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


if __name__ == "__main__":
    main()
