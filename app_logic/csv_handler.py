#!/usr/bin/python
import csv
import os
import json
from datetime import datetime

def get_csv_name(rework_step):
    """generate date based file name"""
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"{rework_step}_data_{date_str}.csv"
    return filename

def check_ref(reference):
    """check Reference"""
    filename = 'data/refs.csv'
    if not os.path.exists(filename):
        return None
    with open(filename, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip headers
        for row in reader:
            if row[1] == reference:
                return row
    return None

def save_to_csv(path, data):
    """Append a new row to the daily CSV file."""
    # Create the file with headers if it doesn't exist
    if not os.path.exists(path):
        with open(path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Operator Code",
                             "Famille",
                             "Reference",
                             "DATEPROD",
                             "LINEPROD",
                             "Rework Card",
                             "Fault",
                             "Process",
                             "Start Time",
                             "End Time",
                             "Rework Time"])
    # Append data
    with open(path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)


def read_from_csv(path, rework_card):
    """Read and find a row in the daily CSV file by rework_card."""
    if not os.path.exists(path):
        return None
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip headers
        for row in reader:
            if row[5] == rework_card:
                return row
    return None


def update_csv(path, rework_card, end_time, rework_time):
    """Update the daily CSV file with end_time and rework_time."""
    if not os.path.exists(path):
        return
    rows = []
    with open(path, mode="r") as file:
        reader = csv.reader(file)
        headers = next(reader)  # Save headers
        rows.append(headers)
        for row in reader:
            if row[2] == rework_card:
                row[4] = end_time
                row[5] = rework_time
            rows.append(row)
    with open(path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(rows)

def load_json():
    """load list Errors"""
    filename = 'data/failure_list.json'
    with open(filename, "r", encoding='utf-8') as f:
        return json.load(f)
