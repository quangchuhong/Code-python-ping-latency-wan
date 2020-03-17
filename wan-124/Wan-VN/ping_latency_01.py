#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, time
import subprocess
from telegram import *
from tracer import *


def ping(ip_dest):

    cmd = "ping -I 192.168.17.223 -c 4 {}".format(ip_dest).split(' ')
    try:
        output = subprocess.check_output(cmd).decode().strip()
        lines = output.split("\n")
        total = lines[-2].split(',')[3].split()[1]
        loss = lines[-2].split(',')[2].split()[0]
        timing = lines[-1].split()[3].split('/')
        return {
            'type': 'rtt',
            'min': timing[0],
            'avg': timing[1],
            'max': timing[2],
            'mdev': timing[3],
            'total': total,
            'loss': loss,
        }
    except Exception as e:
        print(e)
        return None

## check host error
def check_host(ip_dest):
    for hostname in ip_dest:
        response = os.system("ping -c 2 " + hostname)
        if response == 0:
            pingstatus = "Network Active"
        else:
            pingstatus = "Network Error"
            status = "Network error - hostname: " + str(hostname)
            telegram_network_error(status)    ## check host error

## check paket_loss 3 host       
def check_loss(ip_dest):
    ping_01 = ping(ip_dest[0])
    ping_02 = ping(ip_dest[1])
    ping_03 = ping(ip_dest[2])
    loss_01 = ping_01['loss'].split('%')
    loss_02 = ping_02['loss'].split('%')
    loss_03 = ping_03['loss'].split('%')
    if int(loss_01[0]) >= 10 and int(loss_02[0]) >= 10 and \
       int(loss_03[0]) >= 10:
        message = "WAN-124-HTC -VN- packet loss 3 host đồng thời: "\
                 + str(ip_dest[0]) + " ," + str(ip_dest[1]) + " ,"\
                 + str(ip_dest[2])
        ketqua = "Packet loss: " + str(ip_dest[0]) + ": " +\
                 str(ping_01['loss']) + " ," + str(ip_dest[1]) + ": " +\
                 str(ping_02['loss']) + " , " + str(ip_dest[2]) + ": " +\
                 str(ping_03['loss'])
        telegram_packet_loss(message), telegram_packet_loss(ketqua)
    else:
        print "packet loss 0%"

## check latency network
def check_latency(ip_dest):
    ping_01 = ping(ip_dest[0])
    ping_02 = ping(ip_dest[1])
    ping_03 = ping(ip_dest[2])
    if int(float(ping_01['avg'])) >= 50 and int(float(ping_02['avg'])) >= 50 and\
       int(float(ping_03['avg'])) >= 50:
        message = "WAN-124-HTC -VN- Latency 3 host đồng thời Cao > 50ms: " +\
                  str(ip_dest[0]) + " ," + str(ip_dest[1]) + " ," +\
                  str(ip_dest[2])
        ketqua = "Latency Cao tren 50ms: " + str(ip_dest[0]) + ": " +\
                 str(ping_01['avg']) + "ms---" + str(ip_dest[1]) + ": " +\
                 str(ping_02['avg']) + "ms---" + str(ip_dest[2]) + ": " +\
                 str(ping_03['avg'])+"ms"
        telegram_wan_vietnam(message)
        telegram_wan_vietnam(ketqua)
        # traceroute domain
        tracer_domain(ip_dest)
    else:
        print "Network Latency OK!"
while True:
    ip_dest=['baomoi.com','tiki.vn','lazada.vn']
    #check_host(ip_dest)
    check_latency(ip_dest)
    check_loss(ip_dest)
    time.sleep(10)





