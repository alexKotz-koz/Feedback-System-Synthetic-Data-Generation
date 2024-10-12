import random
from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import (
    DataFromPrompt,
    DataFromAttributedPrompt,
    Prompt,
    DataSource,
)


def generateRandomSentiment():
    sentiment = random.randint(0, 1)
    print(sentiment)
    return sentiment


def generateStudentFeedbackAttributed(temperature, outputDirName):
    with DataDreamer(f"./data-dreamer-output/{outputDirName}"):
        gpt4 = OpenAI(model_name="gpt-4")

        attributeGenerationPrompts = DataSource(
            "Attribute Generation Prompts",
            data={
                "prompts": [
                    "Generate the names of 10 graduate school courses, in a comma separated list.",
                    "Generate 10 random instances of the strings,'positive' or 'negative', in a comma separated list.",
                    "Generate 10 random integers between 40 and 80, in a comma separated list.",
                ]
            },
        )

        attributes = Prompt(
            "Generate Attributes",
            inputs={
                "prompts": attributeGenerationPrompts.output["prompts"],
            },
            args={
                "llm": gpt4,
            },
        ).output["generations"]

        studentEvaluationFeedback = (
            DataFromAttributedPrompt(
                "Generate Student Evaluation",
                args={
                    "llm": gpt4,
                    "n": 20,
                    "temperature": temperature,
                    "instruction": (
                        "Generate a student evaluation of teaching feedback comment of the {courseName} graduate school course. Please make the feedback comment {numWords} words. Please make the feedback comment have an overall {sentiment} sentiment. Please format the comment as 'Course Name: {courseName} | Student Feedback: {student feedback comment}."
                    ),
                    "attributes": {
                        "courseName": attributes[0].split(","),
                        "sentiment": attributes[1].split(","),
                        "numWords": attributes[2].split(","),
                    },
                },
                outputs={"generations": "feedback"},
            )
            .select_columns(["feedback"])
            .shuffle()
        )
        print(studentEvaluationFeedback)


def generateStudentFeedback(temperature, outputDirName):
    with DataDreamer(f"./data-dreamer-output/{outputDirName}"):
        gpt4 = OpenAI(model_name="gpt-4")

        studentEvaluationFeedback = DataFromPrompt(
            "Generate Student Evaluation Feedback",
            args={
                "llm": gpt4,
                "n": 20,
                "temperature": temperature,
                "instruction": (
                    "Generate a student evaluation of teaching feedback comment of a graduate school course from the perspective of a student who has just completed the course.",
                    "Please make the feedback comment between 22 and 106 words.",
                    "Please randomly choose between negative or positive sentiment. Make the feedback comment overwhelmingly {your chosen sentiment}.",
                    "Please format the data as: 'Course Name: {course_name} | Student Feedback: {student_feedback_comment}'",
                ),
            },
            outputs={"generations": "feedback"},
        )
        print(studentEvaluationFeedback)


def generateClinicalApplicationFeedback(temperature, outputDirName):
    with DataDreamer(f"./data-dreamer-output/{outputDirName}"):
        gpt4 = OpenAI(model_name="gpt-4")

        clinicalApplicationFeedback = DataFromPrompt(
            "Generate Clinical Application Feedback",
            args={
                "llm": gpt4,
                "n": 20,
                "temperature": temperature,
                "instruction": (
                    "Generate a review of a clinical decision support tool or health care application from the perspective of a practicing medical provider (e.g. doctor, physicans assistant, nurse, or medical assistant).",
                    "Please make the review between 45 and 101 words.",
                    "Please randomly choose between negative or positive sentiment. Make the feedback comment overwhelmingly {your chosen sentiment}.",
                    "Please format the data as: 'Name of Application/Tool: {name_of_app} | Application Review: {application_review}'",
                ),
            },
            outputs={"generations": "feedback"},
        )
        print(clinicalApplicationFeedback)
