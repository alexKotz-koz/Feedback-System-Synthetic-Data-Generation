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
python3 main.py [options]
```
Options:
- `-h, --help`: Show help menu


<br>
Example:

1. After navigating to src (cd src), run the following command:
```sh
python3 main.py ...
```

## Description of Data

- Location of sythnetically generated data: /src/data/
     - real-world/FeedbackClassificationDataset.csv: A manually extracted dataset of athenaHealth EHR marketplace application store reviews Extracted the ... 
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

### Description of output

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