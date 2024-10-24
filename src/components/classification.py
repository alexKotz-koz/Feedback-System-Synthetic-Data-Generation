import os
import pandas as pd
import json
from sklearn.metrics import accuracy_score, f1_score


def importManualLabelData(filepath, start_row, end_row, colname):
    # Read the specified rows from the XLSX file into a pandas DataFrame
    df = pd.read_excel(
        filepath, header=0, skiprows=start_row, nrows=end_row - start_row
    )
    df.columns = df.columns.str.strip()

    df = df.drop(columns=["Feedback", "~Attribute(s)", "~Consequence", "~Value"])
    df = df.rename(
        columns={
            colname: "name",
            "Has Attribute": "hasAttribute",
            "Has Consequence(s)": "hasConsequence",
            "Has Value": "hasValue",
        }
    )
    return df


def importGPTLabelData(filepath, colname):
    with open(filepath, "r") as file:
        data = json.load(file)

    rows = []

    for _, comment in data.items():
        rowData = {}
        for col, item in comment.items():
            if col in [colname, "hasAttribute", "hasConsequence", "hasValue"]:
                rowData[col] = item
        rows.append(rowData)

    df = pd.DataFrame(
        rows, columns=[colname, "hasAttribute", "hasConsequence", "hasValue"]
    )
    df = df.rename(
        columns={
            colname: "name",
            "Has Attribute": "hasAttribute",
            "Has Consequence(s)": "hasConsequence",
            "Has Value": "hasValue",
        }
    )
    return df


def calcMetrics(manDF, gptDF):
    manualCAF = pd.read_csv("data/accuracy-temp/manualCAF.csv")
    gptCAF = pd.read_csv("data/accuracy-temp/gptCAF.csv")
    manualSET = pd.read_csv("data/accuracy-temp/manualSET.csv")
    gptSET = pd.read_csv("data/accuracy-temp/gptSET.csv")

    yTrue = manDF[["hasAttribute", "hasConsequence", "hasValue"]]
    yPred = gptDF[["hasAttribute", "hasConsequence", "hasValue"]]

    # Calculate accuracy and F1 score
    accuracy = accuracy_score(yTrue, yPred)
    f1 = f1_score(yTrue, yPred, average="weighted")

    return accuracy, f1


def evaluate():
    cwd = os.getcwd()
    dataDir = os.path.join(cwd, "data/labeled-data")

    manualLabelFile = os.path.join(dataDir, "SyntheticFeedbackToEvaluate.xlsx")
    cafGPTLabelFile = os.path.join(dataDir, "clinical-application-feedback.json")
    setGPTLabelFile = os.path.join(dataDir, "student-feedback-data.json")

    manunalCAF = importManualLabelData(
        manualLabelFile, start_row=1, end_row=22, colname="appName"
    )
    manualSET = importManualLabelData(
        manualLabelFile, start_row=24, end_row=45, colname="courseName"
    )

    gptCAF = importGPTLabelData(cafGPTLabelFile, "appName")
    gptSET = importGPTLabelData(setGPTLabelFile, "courseName")

    parentDataDir = os.path.join(cwd, "data")
    accuracyTempDir = os.path.join(parentDataDir, "accuracy-temp")
    manualSET.to_csv(f"{accuracyTempDir}/manualSET.csv")
    manunalCAF.to_csv(f"{accuracyTempDir}/manualCAF.csv")
    gptCAF.to_csv(f"{accuracyTempDir}/gptCAF.csv")
    gptSET.to_csv(f"{accuracyTempDir}/gptSET.csv")

    cafAccuracy, cafF1 = calcMetrics(manunalCAF, gptCAF)
    setAccuracy, setF1 = calcMetrics(manualSET, gptSET)

    print(f"CAF Accuracy: {cafAccuracy}")
    print(f"CAF F1 Score: {cafF1}")

    print(f"SET Accuracy: {setAccuracy}")
    print(f"SET F1 Score: {setF1}")
