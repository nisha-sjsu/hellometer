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
    total_wait_time = sum(float(row['wait']) for row in data if row['wait'])
    total_order_time = sum(float(row['order']) for row in data if row['order'])
    total_payment_time = sum(float(row['payment']) for row in data if row['payment'])
    total_service_time = sum(float(row['Total Time']) for row in data if row['Total Time'])

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
@app.route('/data/<store_id>/peakHours')
def get_peak_hours_data(store_id):
    data = pd.read_csv(f"data/{store_id}.csv")
    data['Arrival Time'] = pd.to_datetime(data['Arrival Time'])
    data['Hour'] = data['Arrival Time'].dt.hour
    hourly_data = data.groupby('Hour')['Total Time'].mean().to_dict()
    return jsonify(hourly_data)

@app.route('/data/<store_id>/arrivalTime')
def get_arrival_time(store_id):
    data = pd.read_csv(f"data/{store_id}.csv")
    data['Arrival Time'] = pd.to_datetime(data['Arrival Time'])
    data['Hour'] = data['Arrival Time'].dt.hour
    hour_counts = data.groupby('Hour').size().reset_index(name='Count')
    hour_counts_dict = hour_counts.set_index('Hour').to_dict()['Count']
    
    return jsonify(hour_counts_dict)

@app.route('/data/<store_id>/waitTime')
def wait_time_by_hour(store_id):
    data = pd.read_csv(f"data/{store_id}.csv")
    data['Arrival Time'] = pd.to_datetime(data['Arrival Time'])
    data['Hour'] = data['Arrival Time'].dt.hour
    wait_time_by_hour = data.groupby('Hour')['wait'].mean().to_dict()

    return jsonify(wait_time_by_hour)

@app.route('/data/<store_id>/orderTime')
def order_time_by_hour(store_id):
    data = pd.read_csv(f"data/{store_id}.csv")
    data['Arrival Time'] = pd.to_datetime(data['Arrival Time'])
    data['Hour'] = data['Arrival Time'].dt.hour
    order_time_by_hour = data.groupby('Hour')['order'].mean().to_dict()

    return jsonify(order_time_by_hour)

@app.route('/data/<store_id>/paymentTime')
def payment_time_by_hour(store_id):
    data = pd.read_csv(f"data/{store_id}.csv")
    data['Arrival Time'] = pd.to_datetime(data['Arrival Time'])
    data['Hour'] = data['Arrival Time'].dt.hour
    payment_time_by_hour = data.groupby('Hour')['payment'].mean().to_dict()

    return jsonify(payment_time_by_hour)

if __name__ == '__main__':
    app.run(debug=True)
