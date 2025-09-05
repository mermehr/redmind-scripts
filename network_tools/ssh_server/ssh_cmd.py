#!/usr/bin/env python3
# ssh_cmd.py - Script for sending command from a client to an SSH server
import paramiko

def ssh_command(ip, port, user, passwd, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)

    _, stdout, stderr = client.exec_command(cmd)
    output = stdout.readlines() + stderr.readlines()
    if output:
        print('--- Output ---')
        for line in output:
            print(line.strip())

if __name__ == '__main__':
    import getpass
    # user = getpass.getuser()
    user = input('Username: ')
    password = getpass.getpass()
    ip = input('Enter server IP: ') or '192.168.56.101'
    port = input('Enter port or <CR>: ') or 2222
    cmd = input('Enter command or <CR>: ') or 'id'
    ssh_command(ip, port, user, password, cmd)
