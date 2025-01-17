#!/usr/bin/python3
# Import necessary modules from the Flask framework
from flask import Flask, render_template

# Create an instance of the Flask class
app = Flask(__name__)

# Define the route for the home page ("/")
@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL ("/").
    It renders an HTML page (0-index.html) located in the 'templates' directory.
    """
    return render_template('0-index.html')

# Ensure the app runs when the script is executed directly
if __name__ == "__main__":
    # Start the Flask application on the local server
    app.run()
