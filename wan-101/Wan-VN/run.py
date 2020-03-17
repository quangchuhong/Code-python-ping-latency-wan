#!/usr/bin/python
# -*- coding: utf-8 -*-
import os, time
from subprocess import call
import sys

call(["python", "ping_latency_02.py"])
call(["python", "ping_latency_01.py"])

call(["python", "ping_latency_03.py"])
