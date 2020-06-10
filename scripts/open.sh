#!/bin/bash

{ # try
    konsole --noclose -e ssh -R 80:localhost:$2 $3.localhost.run &
    konsole --noclose -e python3 ./scripts/server.py -s $1 -p $2
} || { # catch
    { 
        xterm -e ssh -R 80:localhost:$2 $3.localhost.run &
        xterm -e python3 ./scripts/server.py -s $1 -p $2
    } || {
        gnome-terminal -x ssh -R 80:localhost:$2 $3.localhost.run &
        gnome-terminal -x python3 ./scripts/server.py -s $1 -p $2
    }
}