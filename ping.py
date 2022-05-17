import os
hostname = "http://54.242.209.160:8000/" #example
response = os.system("ping -c 1 " + hostname)

#and then check the response...
if response == 0:
  print (hostname, 'is up!')
else:
  print (hostname, 'is down!')