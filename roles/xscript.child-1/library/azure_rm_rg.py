#!/usr/bin/python
#
# Copyright (c) 2016 Matt Davis, <mdavis@ansible.com>
#                    Chris Houseknecht, <house@redhat.com>
#
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
__metaclass__ = type


ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'certified'}


DOCUMENTATION = '''
---
module: azure_rm_resourcegroup
version_added: "2.1"
short_description: Manage Azure resource groups.
description:
    - Create, update and delete a resource group.
options:
    location:
        description:
            - Azure location for the resource group. Required when creating a new resource group. Cannot
              be changed once resource group is created.
        required: false
        default: null
    name:
        description:
            - Name of the resource group.
        required: true
    state:
        description:
            - Assert the state of the resource group. Use 'present' to create or update and
              'absent' to delete. When 'absent' a resource group containing resources will not be removed unless the
              force option is used.
        default: present
        choices:
            - absent
            - present
        required: false
extends_documentation_fragment:
    - azure
    - azure_tags

author:
    - "Chris Houseknecht (@chouseknecht)"
    - "Matt Davis (@nitzmahone)"

'''

EXAMPLES = '''
    - name: Create a resource group
      azure_rm_resourcegroup:
        name: Testing
        location: westus
        tags:
            testing: testing
            delete: never

    - name: Delete a resource group
      azure_rm_resourcegroup:
        name: Testing
        state: absent
'''
RETURN = '''
contains_resources:
    description: Whether or not the resource group contains associated resources.
    returned: always
    type: bool
    sample: True
state:
    description: Current state of the resource group.
    returned: always
    type: dict
    sample: {
        "id": "/subscriptions/XXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXX/resourceGroups/Testing",
        "location": "westus",
        "name": "Testing",
        "provisioning_state": "Succeeded",
        "tags": {
            "delete": "on-exit",
            "testing": "no"
        }
    }
'''

try:
    from msrestazure.azure_exceptions import CloudError
    from azure.mgmt.resource.resources.models import ResourceGroup
except ImportError:
    pass

from ansible.module_utils.azure_rm_common import AzureRMModuleBase


class AzureRMResourceGroup(AzureRMModuleBase):

    def __init__(self):
        self.module_arg_spec = dict(
            name=dict(type='str', required=True),
            state=dict(type='str', default='present', choices=['present', 'absent']),
            location=dict(type='str'),
            force=dict(type='bool', default=False)
        )

        self.name = None
        self.state = None
        self.location = None
        self.tags = None
        self.force = None

        self.results = dict(
            changed=False,
            contains_resources=False,
            state=dict(),
        )

        super(AzureRMResourceGroup, self).__init__(self.module_arg_spec,
                                                   supports_check_mode=True,
                                                   supports_tags=True)

    def exec_module(self, **kwargs):

        for key in list(self.module_arg_spec.keys()) + ['tags']:
            setattr(self, key, kwargs[key])

        return {
            "name": self.name,
            "location": self.location,
            'changed': True,
            'source_role': 'xscript.child-1'
        }


def main():
    AzureRMResourceGroup()


if __name__ == '__main__':
    main()
