# Backstory:
You are a junior developer working on your first web development project. Your task is to create a simple web application using Flask that displays a welcome message on the homepage and a list of items on a separate page. This project will help you get acquainted with the basics of Flask and routing.

# Objective:
Build a Flask web application with two routes - one for the homepage (/) displaying a welcome message and another for a page displaying a list of items (/items).

# Tasks:
1) Install Flask using pip install Flask.
2) Create a new Python file named app.py for your Flask application.
3) Set up the basic structure of a Flask application.
4) Define a route / that displays a welcome message.
5) Define a route /items that displays a list of items (e.g., "Item 1", "Item 2", "Item 3").
6) Run the Flask application and test it in your browser.

# Requirements:
- Flask installed (pip install Flask).

# Test Case:
Access the root route (/) and verify that it displays a welcome message.
Access the /items route and verify that it displays a list of items.

# Remember
Flask uses the render_template function to render HTML templates.
Routes are defined using the @app.route decorator.
You can pass data from your Python code to HTML templates using template variables.