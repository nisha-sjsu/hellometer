<h1>Store Statistics Flask App</h1>
<h2>Description</h2>
Store Statistics Flask App is a web application built with Flask for analyzing statistics related to store operations, such as customer arrival times, wait times, order times, and payment times.

<h2>Installation</h2>
Clone this repository to your local machine.<br>
Install the required dependencies by running pip install -r requirements.txt.<br>
Run the Flask app by executing python app.py.<br>

<h2>Usage</h2>
Enter the store ID in the input field.<br>
Click the "Plot Statistics" button to fetch and display the statistics.<br>
Various charts will be displayed showing different aspects of store statistics.<br>

<h2>Routes</h2>
⦿ <b>/</b>: Displays the index page where users can input the store ID and plot statistics.<br>
⦿ <b>/data/{store_id}/statistics</b>: Fetches and returns overall statistics for a specific store.<br>
⦿ <b>/data/{store_id}/peakHours</b>: Fetches and returns peak hours data for a specific store.<br>
⦿ <b>/data/{store_id}/arrivalTime</b>: Fetches and returns arrival time distribution data for a specific store.<br>
⦿ <b>/data/{store_id}/waitTime</b>: Fetches and returns wait time distribution data for a specific store.<br>
⦿ <b>/data/{store_id}/orderTime</b>: Fetches and returns order time distribution data for a specific store.<br>
⦿ <b>/data/{store_id}/paymentTime</b>: Fetches and returns payment time distribution data for a specific store.<br>

<h2>File Structure</h2>
<img width="247" alt="Screenshot 2024-05-07 at 10 01 52 PM" src="https://github.com/nisha-sjsu/hellometer/assets/111548210/2b883394-ec41-4482-a2bf-596163ad753b">

<h2>Dependencies</h2>
⦿ Flask<br>
⦿ pandas<br>
⦿ Chart.js<br>
