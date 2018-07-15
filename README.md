# Prompose - Prometheus setup with Docker-compose

> NOTE: This is a completely docker-compose version. Use only docker-compose, no additional packages required.

A monitoring solution for Docker hosts and containers with [Prometheus](https://prometheus.io/), [Grafana](http://grafana.org/), [cAdvisor](https://github.com/google/cadvisor), 
[NodeExporter](https://github.com/prometheus/node_exporter) and alerting with [AlertManager](https://github.com/prometheus/alertmanager).

Inspired by [stefanprodan/dockprom](https://github.com/stefanprodan/dockprom) & [vegasbrianc/prometheus](https://github.com/vegasbrianc/prometheus).

## Pre-requisites

* Docker
* docker-compose

## Installation

* Clone the project locally to your host.
* If you would like to change which targets should be monitored or make configuration changes, update `prometheus/prometheus.yml`.
* If you want to change alert rules, check `prometheus/alert.rules`.
* Update `alertmanager/config.yml`.
* Update `prometheus/alert.rules`, define your own rules.
* Run it!

```
# Install controller node (which hosts prometheus, grafana, alertmanager...)
$ ADMIN_USER=admin ADMIN_PASSWORD=changeyopasswd docker-compose up
# Install target nodes
$ docker-compose -f docker-compose.exporters.yml up -d
```

* To use Docker private registry, for example with Docker registry host 10.69.96.69:6969/cloud/

```
$ ADMIN_USER=admin ADMIN_PASSWORD=changeyopasswd PRIVATE_REGISTRY=10.69.96.69:6969 NAMESPACE=cloud docker-compose -f docker-compose.private-repos.yml up -d
$ PRIVATE_REGISTRY=10.69.96.69:6969 NAMESPACE=cloud docker-compose -f docker-compose.private-repos.exporters.yml up -d
```

* To use Telegram for alerting purpose, use docker-compose.telegram.* template, for example:

```
$ TELEGRAM_USER_ID=12345 TELEGRAM_TOKEN=XXXX docker-compose -f docker-compose.telegram.yml
```

* **NOTE**: In Docker version 17.05, we may face some problems with /sys/fs/cgroup/cpu,cpuacct (Failed to start container manager: inotify_add_watch /sys/fs/cgroup/cpuacct,cpu: no such file or directory): Run the following commands to live with it without upgrade Docker version:

```
$ mount -o remount,rw '/sys/fs/cgroup' && ln -s /sys/fs/cgroup/cpu,cpuacct /sys/fs/cgroup/cpuacct,cpu
```

## Setup Grafana

## Define alerts

## Setup alerting

## TODO

Production security:
* Update new version with Ansible to manage configuration. The idea: users define themselves which services (exporters) they want to enable (for example, `enable_prometheus: true`) then with a conditional in template files, `prompose` automatically generates docker-compose file and run it.
* Enable SSL for Grafana with a Proxy [jwilder/nginx-proxy](https://hub.docker.com/r/jwilder/nginx-proxy/) or [containious/traelik](https://github.com/containous/traefik)?
* Add user authentication via a  Reverse proxy [jwilder/nginx-proxy](https://hub.docker.com/r/jwilder/nginx-proxy/) or [containious/traelik](https://github.com/containous/traefik) for services cAdvisor, Prometheus & AlertManager.
