import paramiko
import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str)
    parser.add_argument('--filename', type=str)
    parser.add_argument('--frequency', type=str)

    args = parser.parse_args()

    #ssh client connection to rasberry pi
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    ip = args.ip
    user = "pi"
    pwd = "camelcase"

    cli.connect(ip, port = 22, username = user, password = pwd)
    cmd = "./pifm " + args.filename + " " + args.frequency
    stdin, stdout, stderr = cli.exec_command(cmd)
    lines = stdout.readlines()
    print(''.join(lines))
    #print status code

    cli.close()
