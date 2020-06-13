import paramiko
import getpass
import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str)
    parser.add_argument('--path', type=str)
    parser.add_argument('--token', type=str)
    parser.add_argument('--numMsg', type=str)

    args = parser.parse_args()

    paths = list(args.path.split(','))

    #ssh client connection to rasberry pi
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    ip = args.ip
    user = "pi"
    pwd = "camelcase" #getpass.getpass("Password: ")

    cli.connect(ip, port = 22, username = user, password = pwd)

    for i in range(int(args.numMsg)):
        print(paths[i])
        cmd = "curl -o {0} https://s3.jp-tok.cloud-object-storage.appdomain.cloud/team-camelcase-object-storage/5ee35c296d617a4c66834d43-korea-info.wav -H 'Authorization: bearer {1}'".format(paths[i], args.token)
        #print(cmd)
        stdin, stdout, stderr = cli.exec_command(cmd)
        lines = stdout.readlines()
        #print(''.join(lines))
        #print status code

    cli.close()
