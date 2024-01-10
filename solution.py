# app.py

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to my Flask Web App!"

@app.route('/items')
def items():
    item_list = ["Item 1", "Item 2", "Item 3"]
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True)
