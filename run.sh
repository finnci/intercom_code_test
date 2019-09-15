#!/bin/bash -e
if [[ $1 = "test" ]]; then
	echo "running tests"
	exec python tests.py
else
	echo "Starting real invites"
    exec python run_invites.py $1 $2
fi