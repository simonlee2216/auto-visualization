import boto3
import matplotlib.pyplot as plt
import pandas as pd
import time

# AWS S3 Configuration
BUCKET_NAME = 'bucket-name'
FILE_KEY = 'data.csv'

def fetch_data_from_s3():
    """Fetch the latest data file from AWS S3."""
    s3 = boto3.client('s3')
    s3.download_file(BUCKET_NAME, FILE_KEY, 'data.csv')
    data = pd.read_csv('data.csv')
    return data

def update_plot():
    """Update the plot in real-time with the latest data."""
    plt.ion()
    fig, ax = plt.subplots()
    while True:
        data = fetch_data_from_s3()
        ax.clear()
        ax.plot(data['Time'], data['Value'], marker='o')
        ax.set_title("Real-time Data Visualization")
        ax.set_xlabel("Time")
        ax.set_ylabel("Value")
        plt.pause(5)

if __name__ == "__main__":
    update_plot()
