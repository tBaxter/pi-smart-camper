import re
import subprocess

def get_current_network():
    """
    Attempts to get the name of the current wifi network. 
    Macs don't have iwgetid so it will just mock a result.
    For our purposes that's OK.
    """
    try:
        
        network = subprocess.check_output(['iwgetid', '-r']).decode('utf-8').rstrip()
    except FileNotFoundError:
        network = "Mock dev network"
    return network

def get_network_details():
    """
    Return the details for the current network.
    """
    network_name = get_current_network()
    networks = get_all_networks()
    for nw in networks:
        if nw['essid'] == network_name:
            return nw

def get_all_networks():
    """
    Return dict of all networks found on the wlan0 interface.
    
    If you're on a Mac, it will return mock data
    because iwlist isn't available.
    """
    try:
        networks = parse(scan(interface='wlan0'))
    except FileNotFoundError:
        networks = mock_data
    return networks


# Below here is essentially just https://github.com/iancoleman/python-iwlist
# Cause I couldn't install from pypi and installing from github wasn't working.

cellNumberRe = re.compile(r"^Cell\s+(?P<cellnumber>.+)\s+-\s+Address:\s(?P<mac>.+)$")
regexps = [
    re.compile(r"^ESSID:\"(?P<essid>.*)\"$"),
    re.compile(r"^Protocol:(?P<protocol>.+)$"),
    re.compile(r"^Mode:(?P<mode>.+)$"),
    re.compile(r"^Frequency:(?P<frequency>[\d.]+) (?P<frequency_units>.+) \(Channel (?P<channel>\d+)\)$"),
    re.compile(r"^Encryption:(?P<encryption>.+)$"),
    re.compile(r"^Quality=(?P<signal_quality>\d+)/(?P<signal_total>\d+)\s+Signal level=(?P<signal_level_dBm>.+) d.+$"),
    re.compile(r"^Signal level=(?P<signal_quality>\d+)/(?P<signal_total>\d+).*$"),
]

# Detect encryption type
wpaRe = re.compile(r"IE:\ WPA\ Version\ 1$")
wpa2Re = re.compile(r"IE:\ IEEE\ 802\.11i/WPA2\ Version\ 1$")

# Runs the comnmand to scan the list of networks.
# Must run as super user.
# Does not specify a particular device, so will scan all network devices.
def scan(interface='wlan0'):
    cmd = ["iwlist", interface, "scan"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    points = proc.stdout.read().decode('utf-8')
    return points

# Parses the response from the command "iwlist scan"
def parse(content):
    cells = []
    lines = content.split('\n')
    for line in lines:
        line = line.strip()
        cellNumber = cellNumberRe.search(line)
        if cellNumber is not None:
            cells.append(cellNumber.groupdict())
            continue
        wpa = wpaRe.search(line)
        if wpa is not None :
            cells[-1].update({'encryption':'wpa'})
        wpa2 = wpa2Re.search(line)
        if wpa2 is not None :
            cells[-1].update({'encryption':'wpa2'}) 
        for expression in regexps:
            result = expression.search(line)
            if result is not None:
                if 'encryption' in result.groupdict() :
                    if result.groupdict()['encryption'] == 'on' :
                        cells[-1].update({'encryption': 'wep'})
                    else :
                        cells[-1].update({'encryption': 'off'})
                else :
                    cells[-1].update(result.groupdict())
                continue
    return cells

#### THIS IS MOCK DATA FOR TESTING ON MACS (they don't have iwlist)
mock_data = [
    {
        "cellnumber": "01",
        "mac": "00:11:22:33:44:55",
        "essid": "This is mock data.",
        "mode": "Master",
        "frequency": "2.437",
        "frequency_units": "GHz",
        "channel": "6",
        "encryption": "off",
        "signal_quality": "32",
        "signal_total": "70",
        "db": "-78"
    },
    {
        "cellnumber": "02",
        "mac": "FE:DC:BA:98:76:54",
        "essid": "Iwlist isn't available on a Mac.",
        "protocol": "IEEE 802.11bgn",
        "mode": "Master",
        "frequency": "2.462",
        "frequency_units": "GHz",
        "channel": "11",
        "encryption": "wpa",
        "signal_quality": "43",
        "signal_total": "100"
    },
    {
        "cellnumber": "03",
        "mac": "FE:DC:BA:98:76:54",
        "essid": "Mock dev network",
        "protocol": "IEEE 802.11bgn",
        "mode": "Master",
        "frequency": "2.462",
        "frequency_units": "GHz",
        "channel": "11",
        "encryption": "wpa",
        "signal_quality": "62",
        "signal_total": "100"
    }
]
