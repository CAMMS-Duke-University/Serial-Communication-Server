#!/bin/sh

my_handler(){
  python3 exit_handling.py "success"
  EXIT_STATUS=$?
  if [ "$EXIT_STATUS" -eq "0" ]
  then
    # Do work when command exists on success
    echo "Got Success Exit Code: success!!"
  else
      # Do work for when command has a failure exit
      echo "Got Success Exit Code: failure!!"
  fi
}

until my_handler; do
  #statements
  echo "completed"
  sleep 1
done
