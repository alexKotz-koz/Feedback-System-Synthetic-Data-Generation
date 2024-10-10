import json
import pickle
import re
import pandas as pd
import numpy as np
import sqlite3


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

        # Fetch column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]

        # Fetch data
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()
        for row in rows:
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
                "courseName": courseName,
                "feedback": feedback,
            }
            itr += 1
    # Close the connection
    conn.close()
    return extractedStudentFeedbackData


def cleanClinicalApplicationFeedbackData(data):
    appName = data.split("|")[0].strip()
    appName = re.sub(r"^['\"]?Name of Ap{2,3}lication/Tool: ?", "", appName).strip()
    feedback = data.split("|")[1].strip()
    feedback = re.sub(r"^['\"]?Application Review: ?", "", feedback).strip()
    feedback = re.sub(r"Name of Ap{2,3}lication/Tool:.*$", "", feedback).strip()
    feedback = re.sub(r"['\"\n]+$", "", feedback).strip()

    return appName, feedback


def extractClinicalApplicationFeedbackData(dbFile):
    # Connect to the SQLite database
    conn = sqlite3.connect(dbFile)
    cursor = conn.cursor()

    # Fetch all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    extractedClinicalApplicationFeedbackData = {}
    itr = 1
    for table in tables:
        table_name = table[0]
        # Fetch column names
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        column_names = [col[1] for col in columns]

        # Fetch data
        cursor.execute(f"SELECT * FROM {table_name};")
        rows = cursor.fetchall()

        for row in rows:
            data = row[1]
            if isinstance(data, bytes):
                try:
                    data = pickle.loads(data)
                except pickle.UnpicklingError:
                    print("Error: Data could not be unpickled.")
                    continue
            try:
                appName, feedback = cleanClinicalApplicationFeedbackData(data)
            except:
                continue
            # Append to the list
            extractedClinicalApplicationFeedbackData[itr] = {
                "appName": appName,
                "feedback": feedback,
            }
            itr += 1
    # Close the connection
    conn.close()
    return extractedClinicalApplicationFeedbackData
