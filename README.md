# ansible-role
### Overview
- There are 3 roles in this repo
  - `xscript.parent`
  - `xscript.child-1`
  - `xscript.child-2`
- Role `xscript.parent` is included in top level playbook.yml
- Role `xscript.parent` dynamically includes the other two roles using `include_role` directive
  - When Ansible version is 2.4, `xscript.child-1` will be included
  - When Ansible version is 2.5, `xscript.child-2` will be included
- Both `xscript.child-1` and `xscript.child-2` have a embedded module called `azure_rm_rg`
- Top level playbook.yml have a task using `azure_rm_rg` module

### Usage
- Navigate to the root folder of current repo
- Run `ansible-playbook playbook.yml -vv`
- Checkout the console output to see which role's `azure_rm_rg` module is used

