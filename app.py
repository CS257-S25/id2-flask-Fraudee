'''This is the main file that runs the Flask web application.'''
from flask import Flask
from ProductionCode import helper_Functions

app = Flask(__name__)

@app.route('/')
def homepage():
    '''This creates the website'''
    return ("Hello World! This is the homepage. <br>"
    "To find the count of self-help meetings type in (url)/meeting/[count]")

def load_data():
    '''This loads the data from the file'''
    helper_Functions.make_data_array()
    return helper_Functions.data

data = load_data()
'''Loads the data from the file and stores it in a variable'''

@app.errorhandler(404)
def page_not_found(e):
    '''This error will pop up when there is an error in the URL.'''
    return str(e) + "sorry, wrong format, do this instead: (url)/meeting_count"

@app.errorhandler(500)
def python_bug(e):
    '''This error will pop up when there is an error in the code'''
    return str(e) + "Eek, a bug!"

@app.route('/meeting_count', strict_slashes=False)
def get_meeting_count():
    '''This will make a page for the counts of self-help meetings'''
    returned_value = helper_Functions.meeting_count()
    return "The average count of meetings attended by the subject is: " + str(returned_value)

if __name__ == '__main__':
    app.run()
