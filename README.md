# Prompose - Prometheus setup with Docker-compose

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
* Run it!

```
$ ADMIN_USER=admin ADMIN_PASSWORD=changeyopasswd docker-compose up
```

## Setup Grafana

## Define alerts

## Setup alerting

## TODO

Production security:
* Enable SSL for Grafana with a Proxy [jwilder/nginx-proxy](https://hub.docker.com/r/jwilder/nginx-proxy/) or [containious/traelik](https://github.com/containous/traefik)?
* Add user authentication via a  Reverse proxy [jwilder/nginx-proxy](https://hub.docker.com/r/jwilder/nginx-proxy/) or [containious/traelik](https://github.com/containous/traefik) for services cAdvisor, Prometheus & AlertManager.
