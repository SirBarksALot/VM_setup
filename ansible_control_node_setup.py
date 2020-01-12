#!/usr/bin/env python3
import os
import pwd
import distro 
from Crypto.PublicKey import RSA


def check_os():
    os_info = distro.linux_distribution(full_distribution_name=False)
    print(f'Distribution: {os_info[0]}')
    print(f'Major version: {os_info[1]}')
    print(f'Codename: {os_info[2]}')
    return os_info


def create_user(user_name, password):
    os_info = check_os()
    if os_info[1] == 'debian' or os_info[1] == 'ubuntu':
        sudoers_group = 'sudo'
    elif os_info[1] == 'centos':
        sudoers_group == 'wheel'
    else:
        print('System distribution not supported!')
        return

    os.system(f'sudo useradd {user_name} -m -p {password}')
    os.system(f'sudo usermod -aG {sudoers_group} {user_name}')
    print(f'Created user {user_name} and added him to {sudoers_group} group!')

    
def create_ssh_key_pair(user_name, key_name):
    keys_path = {
            'priv': f'/home/{user_name}/.ssh/{key_name}',
            'public': f'/home/{user_name}/.ssh/{key_name}.pub',
            }
    # check if key pair already exists
    if os.path.exists(keys_path['priv']) or os.path.exists(keys_path['public']):
        print(f'Keys already exist!')
    else:
        if not os.path.exists(keys_path['.ssh/']):
            os.makedirs(keys_path['.ssh/'])

        for key, value in keys_path.items():
            if key == 'priv':
                print(f'Generating new priv key: {value}')
                priv_key = RSA.generate(2048)
                with open(value, 'wb+') as f:
                    f.write(priv_key.exportKey('PEM'))
            elif key == 'public':
                print(f'Generating public key: {value}')
                pub_key = priv_key.publickey()
                with open(value, 'wb+') as f:
                    f.write(pub_key.exportKey('OpenSSH'))
            else:
                pass


try:
    pwd.getpwnam('ansible')
    print('User ansible exists!')
except KeyError:
    print('User ansible does not exist.')
    if create_user('ansible', 'Fr!wqQ4#342Sd'):
        create_ssh_key_pair('ansible', 'ansible_key')
