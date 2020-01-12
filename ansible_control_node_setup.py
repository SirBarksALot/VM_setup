#!/usr/bin/env python3
import os
import crypt
import distro 
from Crypto.PublicKey import RSA


def check_os():
    os_info = distro.linux_distribution(full_distribution_name=False)
    print(f'Distribution: {os_info[0]}')
    print(f'Major version: {os_info[1]}')
    print(f'Codename: {os_info[2]}')
    return os_info
    
    
def create_ssh_key_pair(user_name, key_name):
    keys_path = {
            'priv': f'/home/{user_name}/.ssh/{key_name}',
            'public': f'/home/{user_name}/.ssh/{key_name}.pub',
            }
    # check if key pair already exists
    if os.path.exists(keys_path['priv']) or os.path.exists(keys_path['public']):
        print(f'Keys already exist!')
    else:
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
                print('Something went wrong!')


def create_user(name, password):
    pass


check_os()
create_ssh_key_pair('filiplez18', 'my_key')
