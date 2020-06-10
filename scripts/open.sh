#!/bin/bash


ADDRESS="$1@ssh.localhost.run"
PORT="80:localhost:$2"
SERVER="python3 ./scripts/server.py -s $1 -p $2"

echo $ADDRESS
echo $PORT

{ # try
    tmux new -s MySoup -n:dev "tmux new-window -n:server '$SERVER' | tmux split 'ssh -R $PORT $ADDRESS'"
} || { # catch
    { 
        tilix -a session-add-down -e ssh -R $PORT $ADDRESS |
        tilix -a session-add-right -e $SERVER
    } || {
        {
            xterm -e ssh -R $PORT $ADDRESS &
            xterm -e $SERVER
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
