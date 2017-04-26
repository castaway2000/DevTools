#!/usr/bin/env python
import subprocess
import getpass
import datetime as dt
__author__ = 'Adam Szablya'
"""
step 1: dump a backup of the prod database
step 2: acquire the dev database
step 3: load the dev database into the prod database
step 4: check for success: if not success then handle failure
"""


def backup_db(dbfile):
    print("provide the root password for the production database")
    prod = "mysqldump -u root -p prodDB > /home/ec2-user/_backup/mysql/" + dbfile
    try:
        subprocess.check_call(prod, shell=True)
    except subprocess.CalledProcessError as e:
        print(e)


def dev_dump(filename):
    print("provide the root password for the development database")
    dev = "mysqldump -u root -p devDB > /home/ec2-user/_backup/mysql/" + filename
    try:
        subprocess.check_call(dev, shell=True)
    except subprocess.CalledProcessError as e:
        print(e)


def loaddb(devfile, backup):
    load = "mysql -u root -p prodDB < /home/user/_backup/mysql/" + devfile
    try:
        subprocess.call(load, shell=True)
    except subprocess.CalledProcessError as e:
        print(e)
        if "password" not in e:
            reload = "mysql -u root -p prodDB < /home/user/_backup/mysql/" + backup
        try:
            print("ALERT! - SAFETY NET ACTIVATED: LOADING LAST BACKUP")
            subprocess.call(reload, shell=True)
        except subprocess.CalledProcessError as e:
            print(e)
            print("FATAL ERROR PLEASE MANUALLY RELOAD THE DATABASE")


def main():
    d = dt.datetime.now()
    timestamp = str(d.month) + str(d.day) + str(d.hour) + str(d.second)
    backup_name = "dbBackup" + timestamp + ".sql"
    dev_file = "devdump" + timestamp + ".sql"
    backup_db(backup_name)
    dev_dump(dev_file)
    loaddb(dev_file, backup_name)


if __name__ == "__main__":
    main()
    