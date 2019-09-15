# intercom_code_test

How to run the program
======================
Note:

Run the following with a version of Python3 inside a virtualenv.

Created on OSX like this:
```
$ brew install pyenv
$ pyenv install 3.7.4
$ pip install virtualenv
$ mkdir -p ~/.venvs/intercom
$ virtualenv --python=$HOME/.pyenv/versions/3.5.6/bin/python ~/.venvs/intercom
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
