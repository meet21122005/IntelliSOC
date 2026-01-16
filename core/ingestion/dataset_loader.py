import pandas as pd
import requests
import time
import os

API = "http://127.0.0.1:5000/api/logs"

def stream_dataset(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.csv'):
                file_path = os.path.join(root, file)
                df = pd.read_csv(file_path)
                for _, row in df.iterrows():
                    log = row.to_dict()
                    requests.post(API, json=log)
                    time.sleep(0.5)

if __name__ == "__main__":
    stream_dataset("botsv3_data_set")