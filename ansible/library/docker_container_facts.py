#!/usr/bin/python

from __future__ import absolute_import, division, print_function

DOCUMENTATION = """
---
module: docker_container_facts

short_description: Get Docker container facts

description:
  - A module that get Docker container facts, to check whether
    the container is running on host. It is inspired by Kolla module [1]
    [1] https://github.com/openstack/kolla-ansible/blob/master/ansible/\
        library/kolla_container_facts.py

options:
  name;
    description:
      - Name or list of name of containers
    required: False
    type: str or list
"""

EXAMPLES = """
- hosts: all
  tasks:
    - name: Get Prometheus container status
      docker_container_facts
        name: prometheus_container_name
"""

from ansible.module_utils.basic import AnsibleModule
import docker


def main():
    argument_spec = dict(
        name=dict(required=False, type='list', default=[])
    )

    module = AnsibleModule(argument_spec=argument_spec)

    results = dict(changed=False, containers=[])
    client = docker.APIClient()
    containers = client.containers()
    names = module.params.get('name')
    if names and not isinstance(names, list):
        names = list(names)
    # Remove empty string
    names = list(filter(None, names))

    for container in containers:
        # Remove '/ prefix character
        container_name = container['Names'][0][1:]
        if names and container_name not in names:
            continue
        results[container_name] = container
    module.exit_json(**results)


if __name__ == '__main__':
    main()
