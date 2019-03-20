from flask import Flask, render_template, request
# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/")
def hello():
    message = "Creating Web page"
    return render_template('form_ex.html', message=message)

# run the application
if __name__ == "__main__":
    app.run()