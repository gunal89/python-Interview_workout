import re

# IP Validatinn

ip_lists = ["192.168.126.21", "10.254.251.210", "10.128.256.256", "192.168.125.123", "192.162.221"]
ip_pattern = re.compile("^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$")
for ip in ip_lists:
    if re.search(ip_pattern, ip):
        print "{} --> is Valid IP".format(ip)
    else:
        print "{} --> is not valid IP".format(ip)

# Mail-ID Validation

mail_lists = ["its@gmail.com1", "mike13445@yahoomail9.server", "rase23@ha_ch.com", "daniyal@gmail.coma", "thatisit@thatisit"]
for mail in mail_lists:
    if re.match("(([A-Za-z0-9._-]{1,})\@[A-Za-z0-9]{1,}\.[A-Za-z0-9]{1,})", mail):
        print "{} --> Valid Mail Format".format(mail)
    else:
        print "{} --> InValid Mail Format".format(mail)

# Mac Validation
mac_lists = ["00:0a:95:9d:68:16", "00:0a:95:9d:68:16", "00:02:95:97:68:16", "00a:0ab:95b:910:6a8:1f6", "00:0a:95:9d:68"]
for mac in mac_lists:
    if re.search("(([A-Za-z0-9]{2,3}\:){5}[A-Za-z0-9]{2,3})", mac):
        print("{} --> is Valid Mac Address".format(mac))
    else:
        print("{} --> is not Valid Mac Address".format(mac))


from collections import defaultdict

d = defaultdict(list)
letter_list = list()
name, letter = map(int,raw_input().split())
for i in range(0,name):
    d[raw_input()].append(i+1)
print d

for l in range(0,letter):
    letter_list.append(raw_input())
print letter_list

for let in letter_list:
    if let in d.keys():
        print "".join(map(str, d[let]))
    else:
        print -1










