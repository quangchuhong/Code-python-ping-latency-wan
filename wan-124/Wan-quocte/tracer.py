#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import os
import time
from telegram import *


def tracer_domain(domains):
    for host in domains:
        p1 = subprocess.Popen(['traceroute', host], stdout=subprocess.PIPE)
        output = p1.communicate()[0]
        message = "Kết quả tracer 3 domain time-latency cao *** WAN_124: "\
                 + domains[0] + "--" + domains[1] + "--" + domains[2] + "\n" + str(output)
        telegram_tracer(message)

def tracer_vn(domain_vn):
    for host in domain_vn:
        p1 = subprocess.Popen(['traceroute', host], stdout=subprocess.PIPE)
        output = p1.communicate()[0]

        with open('tracert.txt', 'w') as f:
            f.write(output)
        with open('tracert.txt', 'r') as f:
            list_lines = f.readlines()
        print "số hoop traceroute domain %s: %d " %(host, len(list_lines)-1)


