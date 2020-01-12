1. Create ansible control node instance.
2. Clone this repo and run ansible_control_node_setup.py, this will:
  a) create user ansible on the instance you are on
  b) generate ssh key pair
3. Add generated public key to GCP GCE metadata (api, manually)
