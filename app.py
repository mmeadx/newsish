# Import the functions we need from flask
from flask import Flask
from flask import render_template 
from flask import jsonify

# Import username and password 
# from config import password

# Instantiate the Flask application. (Chocolate cake recipe.)
# This statement is required for Flask to do its job. 
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0 # Effectively disables page caching


# DEFINE APP ROUTES TO SPECIFIC PAGES

@app.route("/index.html")
def IndexRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''
     # Open a session, run the query, and then close the session again

    webpage = render_template("index.html")

    return webpage 


@app.route("/about.html")
def ChartsRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''
     # Open a session, run the query, and then close the session again

    webpage = render_template("about.html")

    return webpage

@app.route("/team.html")
def TeamRoute():
    ''' This function runs when the browser loads the index route. 
        Note that the html file must be located in a folder called templates. '''
     # Open a session, run the query, and then close the session again

    webpage = render_template("team.html")

    return webpage 

# This statement is required for Flask to do its job. 
# Think of it as chocolate cake recipe. 
if __name__ == '__main__':
    app.run(debug=True)