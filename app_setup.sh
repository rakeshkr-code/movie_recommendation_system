#!/bin/bash
echo "==============================================================="
echo "Welcome !! This will setup your local virtual environment"
echo "And will install all the required python libraries"
echo "---------------------------------------------------------------"

if [ -d "env" ]; then
	echo "env folder already exists, installing requirements using pip"
else
	echo "creating env and then installing requirements using pip"
	virtualenv env # in windows: python -m venv env
fi

source env/bin/activate	# in windows: CALL env\Scripts\activate

pip install -r requirements.txt

deactivate

