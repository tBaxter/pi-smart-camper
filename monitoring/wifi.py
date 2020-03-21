import subprocess

import iw_parse

def get_networks():
    return iw_parse.get_interfaces(interface='wlan0')

def get_current_network():
    return subprocess.check_output('iwgetid', '-r')