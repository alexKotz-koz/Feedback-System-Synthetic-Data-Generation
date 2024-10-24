# Feedback System Synthetic Data Generation
> This project uses DataDreamer and OpenAI GPT-4 to synthetically create two datasets for feedback classification.

## Installation

OS X & Linux:
1. Clone or download the repository.
2. Set up miniconda environment:
    - If miniconda is not installed on the local machine, please follow the steps outlined here before continuing: [Miniconda installation](https://docs.anaconda.com/free/miniconda/)
    - Once miniconda is installed, create the conda environment by copying this command into a shell (terminal) with an active base conda environment:
        ```sh
        conda env create -f conda_env.yml
        ```
    - Then activate the new conda environment:
        ```sh
        conda activate feedback_system_synthetic_data_generation
        ```
    - Due to the current version of datadreamer.dev, please follow these additional steps to add the datadreamer package to the project:
        ```sh
        pip install datadreamer.dev
        pip install uninstall huggingface-hub
        pip install huggingface-hub==0.24.7
        ```

## Usage example
1. Open a terminal and navigate to /src/:
```sh
cd src
```
2. Use the following command to run the project: 
```sh
python3 main.py
```
<br>

## Description of Data

- Location of sythnetically generated data: /src/data/
    - Directories:
        - data/accuracy-temp: Preprocessed labeled data for manual labelling and LLM labelling.
        - data/labeled-data: Two JSON files containing the information from the Chat-GPT labeling exercise. Full chat history used to generate these data can be found @: https://chatgpt.com/share/6717049f-cc4c-8003-9cf7-734c6993b586 
        - real-world/FeedbackClassificationDataset.csv: A manually extracted dataset of athenaHealth EHR marketplace application store reviews. This dataset was used to identifiy the range of number of words per clinical decision support tool/ health care application review feedback data. https://marketplace.athenahealth.com/
        
    - 1-a-converted-synthetic-data/clinical-application-feedback-data-temp-{temperature}.json: Synthetic clinical decision support tool/healthcare application reviews
        - Arguments:
            - llm: gpt4
            - n: 20
            - temperature: [0.2, 0.5, 0.8, 1.1]
            - instruction: 
                1. "Generate a review of a clinical decision support tool or health care application from the perspective of a practicing medical provider (e.g. doctor, physicans assistant, nurse, or medical assistant).",
                2. "Please make the number of words per comment follow an average of 73 with a standard deviation of 14.",
                3. "Please format the data as: 'Name of Application/Tool: {name_of_app} | Application Review: {application_review}'"
        
    - 1-a-converted-synthetic-data/student-feedback-data-temp-{temperature}.json: Synthetic student evaluation of teaching-like data. 
        - Arguments:
            - llm: gpt4
            - n: 20
            - temperature: [0.2, 0.5, 0.8, 1.1]
            - instruction:
                1. "Generate a student evaluation of teaching feedback comment of a graduate school course from the perspective of a student who has just completed the course.",
                2. "Please make the number of words per comment follow an average of 64 with a standard deviation of 21.",
                3. "Please format the data as: 'Course Name: {course_name} | Student Feedback: {student_feedback_comment}'"

    \* 1-b-converted-synthetic-data was discarded. This version leveraged the DataFromAttributedPrompt method, which returned unfavorable results.

    - 1-c-converted-synthetic-data/clinical-application-feedback-data-temp-{temperature}.json: Synthetic clinical decision support tool/healthcare application reviews
        - Arguments:
            - llm: gpt4
            - n: 20
            - temperature: [0.2, 0.5, 0.8, 1.1]
            - instruction: 
                1. "Generate a review of a clinical decision support tool or health care application from the perspective of a practicing medical provider (e.g. doctor, physicans assistant, nurse, or medical assistant).",
                2. **"Please make the feedback comment between 22 and 106 words.",**
                3. **"Please randomly choose between negative or positive sentiment. Make the feedback comment overwhelmingly {your chosen sentiment}.",**
                4. "Please format the data as: 'Name of Application/Tool: {name_of_app} | Application Review: {application_review}'"
        
    - 1-c-converted-synthetic-data/student-feedback-data-temp-{temperature}.json: Synthetic student evaluation of teaching-like data. 
        - Arguments:
            - llm: gpt4
            - n: 20
            - temperature: [0.2, 0.5, 0.8, 1.1]
            - instruction:
                1. "Generate a student evaluation of teaching feedback comment of a graduate school course from the perspective of a student who has just completed the course.",
                2. **"Please make the review between 45 and 101 words.",**
                3. **"Please randomly choose between negative or positive sentiment. Make the feedback comment overwhelmingly {your chosen sentiment}.",**
                4. "Please format the data as: 'Course Name: {course_name} | Student Feedback: {student_feedback_comment}'"


    - 1-d-converted-synthetic-data/clinical-application-feedback-data-temp-{temperature}.json: Synthetic clinical decision support tool/healthcare application reviews
        - Arguments:
            - llm: gpt4
            - n: 20
            - temperature: [0.2, 0.5, 0.8, 1.1, 1.4]
            - instruction: 
                1. "Generate a review of a clinical decision support tool or health care application from the perspective of a practicing medical provider (e.g. doctor, physicans assistant, nurse, or medical assistant).",
                2. "Please make the feedback comment between **5** and 106 words.",
                3. "Please randomly choose between negative or positive sentiment. Make the feedback comment overwhelmingly {your chosen sentiment}.",
                4. "Please format the data as: 'Name of Application/Tool: {name_of_app} | Application Review: {application_review}'"
        
    - 1-d-converted-synthetic-data/student-feedback-data-temp-{temperature}.json: Synthetic student evaluation of teaching-like data. 
        - Arguments:
            - llm: gpt4
            - n: 20
            - temperature: [0.2, 0.5, 0.8, 1.1, 1.4]
            - instruction:
                1. "Generate a student evaluation of teaching feedback comment of a graduate school course from the perspective of a student who has just completed the course.",
                2. "Please make the review between **5** and 101 words.",
                3. "Please randomly choose between negative or positive sentiment. Make the feedback comment overwhelmingly {your chosen sentiment}.",
                4. "Please format the data as: 'Course Name: {course_name} | Student Feedback: {student_feedback_comment}'"


### Description of output
The current activate code in main.py will run feedback analysis on the 1-d-converted-synthetic-data dataset. Results from the feedback analysis can be found in src/data/results (set = Student Evaluation of Teaching | caf = Clinical Application Feedback). Sentiment analysis, lexical diversity, average word count, and total word count for each file is located in the two results files. Previous analyses can be found under the 2-{a-d}-sentiment-analyzed directories, where this data is embedded in the same file as the actual data. Additionally, the call to evaluate() in main.py will generate accuracy and f1 scores for the manually labelled vs Chat-GPT v 4o labelled data.

---

## Requirements
- Python 3.9 or higher. 
    - This project was developed in python v3.11 and has been tested with python 3.9 thru 3.12.
- Miniconda (see Installation section for further instructions).
- macOS or Linux based operating system.

## Contributing

1. Fork it (<https://github.com/alexKotz-koz/...>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

## Citations:
```sh
@misc{patel2024datadreamer,
      title={DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows}, 
      author={Ajay Patel and Colin Raffel and Chris Callison-Burch},
      year={2024},
      eprint={2402.10379},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
1. Ajay Patel, Colin Raffel, and Chris Callison-Burch. 2024. DataDreamer: A Tool for Synthetic Data Generation and Reproducible LLM Workflows. arXiv. https://doi.org/10.48550/arxiv.2402.10379
2. Hutto, C.J. & Gilbert, E.E. (2014). VADER: A Parsimonious Rule-based Model for
Sentiment Analysis of Social Media Text. Eighth International Conference on
Weblogs and Social Media (ICWSM-14). Ann Arbor, MI, June 2014.