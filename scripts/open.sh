#!/bin/bash

{ # try
    tmux new -s MySoup -n:dev "tmux new-window -n:server 'python3 ./scripts/server.py -s $1 -p $2' | tmux split 'ssh -R 80:localhost:$2 $3.localhost.run'"
} || { # catch
    { 
        tilix -a session-add-down -e ssh -R 80:localhost:$2 $3.localhost.run |
        tilix -a session-add-right -e python3 ./scripts/server.py -s $1 -p $2
    } || {
        {
            xterm -e ssh -R 80:localhost:$2 $3.localhost.run &
            xterm -e python3 ./scripts/server.py -s $1 -p $2
        } || {
            {
                konsole --noclose -e ssh -R 80:localhost:$2 $3.localhost.run &
                konsole --noclose -e python3 ./scripts/server.py -s $1 -p $2
            } || {
                printf "\033[0;38;5;9m\n\nCompatible terminal not found\033[0m\n\n"   
            }
        }
    }
}

