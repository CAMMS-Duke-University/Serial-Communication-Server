#!/bin/sh

my_handler(){
  python3 serial-server.py "read"
  EXIT_STATUS=$?
  echo "Serial Server Exit Status: $EXIT_STATUS"
  if [ "$EXIT_STATUS" -eq "0" ]
  then
    # Do work when command exists on success
    echo "Got Success Exit Code: success!!"
  else
      # Do work for when command has a failure exit
      echo "Got Success Exit Code: failure!!"
  fi
}

while true  
do
  #statements
  my_handler
  echo "completed"
  sleep 5
done
