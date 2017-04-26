#!/usr/bin/env python
"""This Script deploys a copy from a remote database to the local database
"""
import subprocess
import os

__Author__ = "Adam Szablya"
__date__ = "8/31/2016"
__version__ = "1.0"


def create_ssh_connection():
    key = raw_input("please provide the absolute path to the ssh .pem file: ")
    scp = "scp -i " + key + " user@yourWebsite.com:/home/user/_backup/mysql/* ."
    subprocess.call(scp, shell=True)


def deploy_sql():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    print dir_path
    for file in os.listdir(dir_path):
        print file
        if "dbBackup" in file:
            backup = file
    loadsql = "mysql -u root -p -P 3306 dbname < " + str(backup)
    try:
        subprocess.call(loadsql, shell=True)
    except SystemError as e:
        print(e)
    finally:
        print("\nsql database has been loaded")


if __name__ == "__main__":
    print("\nINFO: please make sure that openSSH is installed on your machine before "
          "proceeding and have mysql exe is your system32 folder")
    create_ssh_connection()
    deploy_sql()