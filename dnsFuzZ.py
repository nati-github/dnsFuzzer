#!/usr/bin/python

from scapy.all import *
send(IP(dst="")/UDP()/fuzz(DNS()), loop=1)


