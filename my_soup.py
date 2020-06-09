import click
from scripts import banner

@click.command()
@click.option("--scam"    , '-s', default="None" , 
                help="Web template name.   \033[92mpython my_soup.py -s Name\033[0m")
@click.option("--password", '-p', default=False,  
                help="View action history. \033[92mpython my_soup.py -p True\033[0m")
@click.option("--info", '-i', default=False,
                help="View info tools.     \033[92mpython my_soup.py -i True\033[0m")

def main(scam, password, info):
    if (scam != "None"):
        print(f"Scam!! {scam}")
    elif (password):
        print("Holi")
    elif (info):
        banner.info()
    else:
        while (True):
            option = banner.option()
            if(option == None):
                break

if __name__ == "__main__":
    main()