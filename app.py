from flask import Flask, jsonify, render_template
import pandas as pd
import csv
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def process_data(file_path):
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data = list(reader)

        for row in data:
            row['Arrival Time'] = datetime.strptime(row['Arrival Time'], '%Y-%m-%d %H:%M:%S')

        return data

def get_data(store_id):
    file_path = f"data/{store_id}.csv"
    data = process_data(file_path)
    return data

# Route to fetch statistics
@app.route('/data/<store_id>/statistics')
def get_statistics(store_id):
    file_path = f"data/{store_id}.csv"
    data = process_data(file_path)
    total_customers = len(data)
    total_wait_time = sum(float(row['wait']) for row in data)
    total_order_time = sum(float(row['order']) for row in data)
    total_payment_time = sum(float(row['payment']) for row in data)
    total_service_time = sum(float(row['Total Time']) for row in data)

    average_wait_time = total_wait_time / total_customers
    average_order_time = total_order_time / total_customers
    average_payment_time = total_payment_time / total_customers
    average_service_time = total_service_time / total_customers

    statistics = {
        'total_customers': total_customers,
        'average_wait_time': average_wait_time,
        'average_order_time': average_order_time,
        'average_payment_time': average_payment_time,
        'average_service_time': average_service_time
    }

    return jsonify(statistics)

# Route to fetch peak hours data
@app.route('/data/<store_id>/peak-hours')
def get_peak_hours_data(store_id):
    data = pd.read_csv(f"data/{store_id}.csv")
    data['Arrival Time'] = pd.to_datetime(data['Arrival Time'])
    data['Hour'] = data['Arrival Time'].dt.hour
    hourly_data = data.groupby('Hour')['Total Time'].mean().to_dict()
    return jsonify(hourly_data)

# Route to fetch arrival times
@app.route('/data/<store_id>/arrival-times')
def get_arrival_times(store_id):
    data = get_data(store_id)
    arrival_times = [row['Arrival Time'] for row in data]
    return jsonify(arrival_times)

if __name__ == '__main__':
    app.run(debug=True)
