# Deploy Wekan with pyinfra

This project is meant to provide PoC for deployment of Wekan kanban dashboard (https://wekan.github.io).


# Prerequisites

Fedora 38 Server/Cloud edition with ssh access without password for user that is going to be in deployment.
Python 3.8 is required on instance that is going to run script.

# Installation

1. git clone this project
2. create virtualenv and activate it
3. pip install -r requirements.txt
4. Edit inventories/wekan.py and replace example.com with dns/ip address of your Fedora instance.
5. Edit conf.json if default wekan user is not created, use one that you want.
6. Run the following command (it will install dependencies and start application):
```shell
pyinfra inventories/wekan.py deployment.py
```
7. You can in order to verify that everything went well run:
```shell
pytest --hosts='ssh://{user}@{dns/ip}' 
```


