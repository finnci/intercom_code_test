# Intercom Code Test

# Problem Description

We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our Dublin office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending).

- You must use the first formula from this Wikipedia article to calculate distance. Don't forget, you'll need to convert degrees to radians.

- The GPS coordinates for our Dublin office are 53.339428, -6.257664.

- You can find the Customer list here.


# Answer Description
I have a InviteCustomers class defined in [distance_invite.py](distance_invite.py), this class can be created with a few parameters, an office param allows us pass in the long/lat coordinates for the office, a customers filepath allows us to find where a list of customers is stored, and a max_distance is used to figure out the max distance between our customers and the office that makes it acceptable to invite the users.

To run the code and interact with this class I have used a basic python script named [run_invites.py](run_invites.py) & [argparse](https://docs.python.org/3/library/argparse.html) to pass in varying configs or customers.txt files, these all fall back on 'reasonale' defaults (mostly based on how the question was phrased.

Pip dependencies are listed, with versions, in [requirements.txt](requirements.txt).

# How to run: Option 1 - local python

First, clone & cd to this repo on a local machine.
To run this code on your own machine, you will need to do as follows:

This can be created on OSX like this, other OS's will likely vary:
```
$ brew install pyenv
$ pyenv install 3.7.4
$ pip install virtualenv
$ mkdir -p ~/.venvs/intercom
$ virtualenv --python=$HOME/.pyenv/versions/3.7.4/bin/python ~/.venvs/intercom
$ . ~/.venvs/intercom/bin/activate
```

Basic:
```
$ pip install -r requirements.txt
$ python run_invites.py

Users To Invite:
4 - Ian Kehoe
5 - Nora Dempsey
6 - Theresa Enright
8 - Eoin Ahearn
11 - Richard Finnegan
12 - Christina McArdle
13 - Olive Ahearn
15 - Michael Ahearn
23 - Eoin Gallagher
24 - Rose Enright
31 - Alan Behan
39 - Lisa Ahearn
```

Run with args:
```
$ python run_invites.py -h
usage: run_invites.py [-h] [--config_path CONFIG_PATH]
                      [--customer_overwrite CUSTOMER_OVERWRITE]

allow a user to define some config files & customer.txt files

optional arguments:
  -h, --help            show this help message and exit
  --config_path CONFIG_PATH
                        file path for config
  --customer_overwrite CUSTOMER_OVERWRITE
                        file path for a different customers.txt
```

For example:
```
$ python run_invites.py --config_path='./config_2.yml' --customer_overwrite="./test_customers.txt"
```
will run the same code, but using a different config_2.yml and a different customers file.

You can run the unittests as follows:
```
$ python tests.py
.No file found at ./ccc.txt
.....
----------------------------------------------------------------------
Ran 6 tests in 0.009s

OK
```

# How to run: Option 2 - Docker


First, clone & cd to this repo on a local machine.

Assuming you have Docker installed you can do as follows with my makefile:
```
make docker_build
```
Then you can run the image as follows:
```
$ docker run intercom_test
Starting real invites

Users To Invite:
4 - Ian Kehoe
5 - Nora Dempsey
6 - Theresa Enright
8 - Eoin Ahearn
11 - Richard Finnegan
12 - Christina McArdle
13 - Olive Ahearn
15 - Michael Ahearn
23 - Eoin Gallagher
24 - Rose Enright
31 - Alan Behan
39 - Lisa Ahearn
```

All the same params as mentioned in Option 1 will also work here.

For example, to pass a new config file you can do as follows:
```
docker run intercom_test --config_path="./config.yml"
```

You can also run the code unittests with the same docker image:
```
$ docker run intercom_test test
running tests
......
----------------------------------------------------------------------
Ran 6 tests in 0.004s

OK
```


# TODO
1. write tests for run_invites.py
2. publish docker image so i can just install & run it without even cloning the repo.
