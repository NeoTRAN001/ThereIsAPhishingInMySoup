from flask import Flask
import click

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index'

@click.command()
@click.option("--scam", '-s', default="None" , 
                help="Web template name.   \033[92mpython3 server.py -s Name\033[0m")
def main(scam):
    print(scam)
    app.run(debug=True)

if __name__ == '__main__':
    main()