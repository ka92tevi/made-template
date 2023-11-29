#!/bin/bash

# Execute the data pipeline
python automatedpipeline.py

database_file="dbrituparna"


# Check if the output file(s) exist
if [ -f "$database_file" ]; then
    echo "Yes! The database file exists."
else
    echo "No database file found!!"
fi
