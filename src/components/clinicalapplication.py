import os
import pandas as pd


def calcAvg():
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)

    data = os.path.join(parent_dir, "data")
    fdbdata = os.path.join(data, "FeedbackClassificationDataset.csv")
    with open(fdbdata, "r") as file:
        feedback = pd.read_csv(file)
        feedback.dropna()

        comments = feedback["Comment"]
        applications = feedback["Application/Product"]

        avg_words_per_app = feedback.groupby("Application/Product")["Comment"].apply(
            lambda x: x.str.split().str.len().mean()
        )

        overall_avg_words = avg_words_per_app.mean()
        overall_sd_words = avg_words_per_app.std()

        print(
            f"Overall average number of words across all applications: {overall_avg_words}"
        )
        print(
            f"Standard deviation of words across all applications: {overall_sd_words}"
        )


calcAvg()
