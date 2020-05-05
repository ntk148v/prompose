# Prompose

> **NOTE**: For the complete solution, please check [ansitheus](https://github.com/ntk148v/ansitheus).

## Overview

* Inspired by [OpenStack Kolla-ansible](https://github.com/openstack/kolla-ansible): You can recognize that Prompose is very similar with Kolla-ansible.

* Install [Docker](https://www.docker.com/) and [Docker-compose](https://docs.docker.com/compose/) in multiple hosts.

* Easily configure and deploy containerized [Prometheus](https://prometheus.io) stack: Prometheus, Alertmanager,  its [exporter](https://prometheus.io/docs/instrumenting/exporters/), [Telegram Bot for Prometheus's Alertmanager](https://github.com/metalmatze/alertmanager-bot) and [Grafana](https://grafana.com/) in multiple hosts.

## Why Prompose?

* In the origin version, I used [docker-compose](https://docs.docker.com/compose/) to deploy Prometheus monitoring stack. Therefore `Prompose` is born, simply it is `Prometheus + Docker-compose = Prompose`. This version stills available [pure-docker-compose branch.](https://github.com/ntk148v/prompose/tree/pure-docker-compose)

* The current version is using [ansible](https://github.com/ansible/ansible) and its [docker\_service module](https://docs.ansible.com/ansible/2.5/modules/docker_service_module.html) to configure number of exporters, port... and deploy Prometheus stack in several hosts easily.

* Why don't use [docker\_container module](https://docs.ansible.com/ansible/2.5/modules/docker_container_module.html)? Just because I found this **after** [docker\_service](https://docs.ansible.com/ansible/2.5/modules/docker_container_module.html). Maybe will use it in the future?

## Usage guide

* Firstly, you have to install ansible (>=2.4) in your management host. There are multiple ways to install ansible, but you simply use [requirements.txt](./requirements.txt). You should have `python-pip` and `python-dev` as well.

```
$ sudo pip install -r requirements.txt
```

* Create `/etc/prompose` directory and copy [etc/prompose.yml](./etc/prompose.yml) config file. You can put config in whatever directory you want, but then when execute command, you have to use `--configdir` option to point to the directory.

```
$ sudo mkdir /etc/prompose
$ sudo cp etc/prompose.yml /etc/prompose/prompose.yml
```

* Read the config file and [ansible/group\_vars/all.yml](./ansible/group_vars/all.yml) file (The options in this file **can be overriden** in `prompose.yml`') carefully, then do the change in config file you copied in previous step (by default it is )`/etc/prompose/prompose.yml`).

* Prepare your inventory file - defines your hosts. Example file can be found [here](./ansible/inventory/).

* Run Prompose, point to inventory file with option `--inventory|-i`:

```
$ sudo ./tools/prompose -i ansible/inventory/all-in-one -h    
Usage: ./tools/prompose COMMAND [option]

Options:
    --inventory, -i <inventory_path> Specify path to ansible inventory file
    --configdir, -c <config_path>    Specify path to directory with prompose.yml
    --verbose, -v                    Increase verbosity of ansible-playbook
    --help, -h                       Show this usage information
    --images                         Remove images when this option is defined and command is remove
    --volumes                        Remove volumes when this option is defined and command is remove

Commands:
    installdocker                    Install docker & docker-compose in target hosts
    precheck                         Do pre-deployment checks for hosts
    deploy                           Deploy and start all prompose containers
    stop                             Stop all prompose containers
    pull                             Pull all images for containers (only pull, no running containers)
    remove                           Stop and remove all prompose containes (With --images - remove images and --volumes - remove volumes)
    restart                          Restart all prompose containers
```

* Enjoy it!

## Contribute

* If you are interesed with this project, feel free to create a pull request.

* If you have any questions, please contact me via email `kiennt2609@gmail.com`.
