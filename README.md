# Stackular API v0.1a

A working prototype code for a RESTful API for Stackular app. Tested and worked best under `nginx` + `wsgi`.
 
## Prerequisites

+ Python 3.5
+ Flask Restful
+ SQL Alchemy
+ Psycopg2
+ PostgreSQL

## Installation

+ Create a PostgreSQL database named `stackular`. Name of the database and psql credentials can be modified in `config.py` file.
+ Install required Python packages: `pip install -r requirements.txt` 
+ To setup DB schema, run this script: `python setupdb.py` and follow the prompt.

Run `server.py` to start the server manually.

## Contributors
+ Paul Burakov