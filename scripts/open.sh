#!/bin/bash


ADDRESS="$1@ssh.localhost.run"
PORT="80:localhost:$2"
SERVER="python3 ./server.py -t $1 -p $2"

{ # try
    xterm -e ssh -R $PORT $ADDRESS |
    xterm -e $SERVER
} || { # catch
    { 
        tilix -a session-add-down -e ssh -R $PORT $ADDRESS |
        tilix -a session-add-right -e $SERVER
    } || {
        {
            tmux new -s MySoup -n:dev "tmux new-window -n:server '$SERVER' | tmux split 'ssh -R $PORT $ADDRESS'"
        } || {
            {
                konsole --noclose -e ssh -R $PORT $ADDRESS &
                konsole --noclose -e $SERVER
            } || {
                printf "\033[0;38;5;9m\n\nCompatible terminal not found\033[0m\n\n"   
            }
        }
    }
}
