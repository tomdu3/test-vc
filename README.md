# Random List Generator

This project is a random list generator. It generates a list of random numbers which is of the size defined by the user.


## Explanation

- run program:
    - make environment with: `python -m venv venv`
    - activate environment: `venv\Scripts\activate.bat` in windows or `source venv/bin/activate` in linux
    - install libraries: `pip install -r requirements.txt`
    - then setup `.env` file with your API key (see the sample)
    - then run `python rand_list.py`
    - then run `python testapi.py`
    - then run `python top.py`

- usage of the function:
  - example:
    - `random_list(10)` will generate a list of 10 random numbers from 0 to 100
    - `random_list(-1)` will generate a None, because the limit is less than 0
  

## Deadline for the final project
13 September 2024

## Technologies used

**Programming languages used**:
- Python

**Modules used:**
- `random`
- `cowsay`
- os
- dotenv
- requests
- pprint

© TDCode 2024
