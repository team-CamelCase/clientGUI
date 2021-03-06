import paramiko
import getpass
import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str)
    parser.add_argument('--path', type=str)
    parser.add_argument('--token', type=str)

    args = parser.parse_args()

    #ssh client connection to rasberry pi
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    print(args.ip, args.path, args.token)
    ip = args.ip
    user = "pi"
    pwd = "camelcase" #getpass.getpass("Password: ")

    cli.connect(ip, port = 22, username = user, password = pwd)
    directoryPath = './Desktop/test2/fm_transmitter-master/'
        cmd = "curl -v -o {1}{0} https://s3.jp-tok.cloud-object-storage.appdomain.cloud/team-camelcase-object-storage/{2} -H 'Authorization: bearer {3}'".format(args.path, directoryPath, args.path, args.token)
    #print(cmd)
    stdin, stdout, stderr = cli.exec_command(cmd)
    print("------------------")
    print(stdout)
    print(stderr)
    lines = stdout.readlines()
    print(''.join(lines))
    #print status code

    cli.close()
