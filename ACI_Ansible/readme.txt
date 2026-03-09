This list of playbooks has been tested on the Cisco ACI sandbox
The order to run the playbooks are:
1.ansible-playbook -i inventory/aci_hosts.yml playbooks/setup_physical_domain.yml
2.ansible-playbook -i inventory/aci_hosts.yml playbooks/setup_interface_policies.yml
3.ansible-playbook -i inventory/aci_hosts.yml playbooks/deploy_bare_metal.yml 
