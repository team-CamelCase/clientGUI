import paramiko
import requests
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--ip', type=str)
    parser.add_argument('--filename', type=str)
    parser.add_argument('--frequency', type=str)

    args = parser.parse_args()

    files = list(args.filename.split(','))
    print(len(files))
    print(files)

    #ssh client connection to rasberry pi
    cli = paramiko.SSHClient()
    cli.set_missing_host_key_policy(paramiko.AutoAddPolicy)

    ip = args.ip
    user = "pi"
    pwd = "camelcase"

    cli.connect(ip, port = 22, username = user, password = pwd)
    #cmd = "sudo su"
    directoryPath = "./Desktop/test2/fm_transmitter-master/"

    for i in range(len(files)):
        #cmd = "sox -t wav {0}{1} -r 25000 -c 1 -b 16 -t wav - | sudo ./fm_transmitter-master/fm_transmitter -f {2} -".format(directoryPath, "voice.wav", "100.0")
        stdin, stdout, stderr = cli.exec_command("sox -t wav {0}{1} -r 25000 -c 1 -b 16 -t wav - | sudo ./fm_transmitter-master/fm_transmitter -f {2} -".format(directoryPath, args.filename, args.frequency))
        #print(cmd)
        #stdin, stdout, stderr = cli.exec_command(cmd)
        #print(stdout)
        print(stderr)
        lines = stdout.readlines()
        print(''.join(lines))
        #print status code

    cli.close()
