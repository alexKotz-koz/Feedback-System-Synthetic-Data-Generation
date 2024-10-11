from datadreamer import DataDreamer
from datadreamer.llms import OpenAI
from datadreamer.steps import DataFromPrompt


def generateStudentFeedback(temperature, outputDirName):
    with DataDreamer(f"./{outputDirName}"):
        gpt4 = OpenAI(model_name="gpt-4")

        studentEvaluationFeedback = DataFromPrompt(
            "Generate Student Evalution Feedback",
            args={
                "llm": gpt4,
                "n": 20,
                "temperature": temperature,
                "instruction": (
                    "Generate a student evaluation of teaching feedback comment of a graduate school course from the perspective of a student who has just completed the course.",
                    "Please make the number of words per comment follow an average of 64 with a standard deviation of 21.",
                    "Please format the data as: 'Course Name: {course_name} | Student Feedback: {student_feedback_comment}'",
                ),
            },
            outputs={"generations": "feedback"},
        )
        print(studentEvaluationFeedback)


def generateClinicalApplicationFeedback(temperature, outputDirName):
    with DataDreamer(f"./{outputDirName}"):
        gpt4 = OpenAI(model_name="gpt-4")

        clinicalApplicationFeedback = DataFromPrompt(
            "Generate Clinical Application Feedback",
            args={
                "llm": gpt4,
                "n": 20,
                "temperature": temperature,
                "instruction": (
                    "Generate a review of a clinical decision support tool or health care application from the perspective of a practicing medical provider (e.g. doctor, physicans assistant, nurse, or medical assistant).",
                    "Please make the number of words per comment follow an average of 73 with a standard deviation of 14.",
                    # when I first generated the data I added a type of three p's to application -> reflected in the cleaning of this dataset
                    "Please format the data as: 'Name of Application/Tool: {name_of_app} | Application Review: {application_review}'",
                ),
            },
            outputs={"generations": "feedback"},
        )
        print(clinicalApplicationFeedback)
