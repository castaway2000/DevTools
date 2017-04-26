#!/usr/bin/env python
"""
This module is framework for mutithreaded functionality.
"""
import socket
import time
from datetime import datetime
from multiprocessing import Process
import gevent


class Replicant(object):
    """multithreading class"""

    def __init__(self, data, process):
        self.data = data
        self.target = None
        self.process = process

        self.proc = None

    def robot(self):
        """worker for thread"""
        value = self.data[0]
        return {'value': value}

    def multiprocess(self):
        """multiprocessing command"""
        self.proc = Process(target=self.target)
        self.proc.start()
        return self.proc

    def end_process(self):
        """kill when process is done"""
        self.process.terminate()
        time.sleep(0.1)
        if self.process.is__alive():
            raise "the process is unable to die"


class TrafficGenerator(object):
    """trafic generation class"""
    def __init__(self, vip, port, duration, rate):
        self.vip = vip
        self.port = port
        self.duration = duration
        self.rate = rate

        self.greenlets = None
        self.con = []
        self.data = 'ping'


    def generate_traffic(self, vip, port, rate=3, duration=10):
        """prepares traffic to send"""
        self.greenlets = [gevent.Greenlet(self.connect(vip, port))
                          for _ in range(rate*duration)]
        self.send_traffic(self.greenlets, rate)

    def connect(self, host, port, data=''):
        """uses localhost as a user connection"""
        data = self.data
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect((host, port))
            sock.sendall(data)
            recv = sock.recv(1024)
            recv_data, server_info, recv_time = recv.split()
            received = '%s, %s, %s' % (recv_data, server_info,
                                       recv_time)
            print received
        finally:
            sock.close()

    def send_traffic(self, greenlets, rate):
        """send conncurrent traffic per second"""
        self.con = []
        while bool(10000 < datetime.today().microsecond < 50000) != True:
            gevent.sleep(0.1)

        # open connections per seccond
        for gre in greenlets:
            gre.start()
            gevent.sleep(0.99/ rate)

        # wait for response
        gevent.sleep(1)
        for gre in greenlets:
            while not gre.ready():
                gevent.sleep(0.1)
            try:
                self.con.append(gre.get(timeout=0.1))
            except gevent.Timeout as err:
                raise err
        return self.con