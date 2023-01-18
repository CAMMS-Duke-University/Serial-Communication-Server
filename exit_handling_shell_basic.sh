#!/bin/sh

python3 exit_handling.py "success"
echo "Got Success Exit Code: $?"

echo "================================"
echo ""

python3 exit_handling.py "failure"
echo "Got Failure Exit Code: $?"

echo "================================"
echo ""

python3 exit_handling.py "success"
EXIT_STATUS=$?
echo "Got Success Exit Code: $EXIT_STATUS"


echo "================================"
echo ""

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

# Reference:
# - https://medium.com/@anupkumarray/working-with-exit-codes-between-python-shell-scripts-177931204291
#   - https://unix.stackexchange.com/questions/7704/what-is-the-meaning-of-in-a-shell-script
