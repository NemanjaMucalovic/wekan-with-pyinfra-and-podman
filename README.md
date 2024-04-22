# Deploy Wekan Kanban Board with pyinfra and Podman

This project is meant to provide PoC for deployment of Wekan kanban dashboard (https://wekan.github.io), using  pyinfra
package to handle installation and configuration (https://pyinfra.com) while application itself is running using rootless
Podman (https://podman.io) in combination with quadlet feature.
Test for deployment are written using pytest-testinfra package (https://testinfra.readthedocs.io/en/latest/index.html)


# Prerequisites

Fedora 38/39 Server/Cloud edition with ssh access without password for user that is going to be used in deployment.
Python 3.8 is required on instance that is going to run script.

# Installation

1. git clone this project
```shell
git clone https://github.com/NemanjaMucalovic/wekan-with-pyinfra-and-podman.git
```
2. Create python virtualenv inside repo root directory and activate it
```shell
python3 -m virtualenv venv && source venv/bin/activate
```
3. install required dependencies
```shell
pip install requirements.txt
```
4. Edit conf.json and replace example.com with the DNS/IP address of your Fedora instance, 
   and replace ssh_user with the appropriate username.


5. Run the following command (it will install required packages, copy files and start application):
```shell
pyinfra inventories/wekan.py deployment.py
```
6. You can in order to verify that everything went well run tests:
```shell
pytest --hosts='ssh://{user}@{dns/ip}' 
```

7. Open http://{dns/ip}:8080 in your browser.

If tests have passed but application is not reachable, check firewall settings or VPS access rules.


