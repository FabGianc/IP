#!/bin/bash
for ip in `cat ip_list_comp.txt`
do
   echo $ip
   hostname=v4.whois.cymru.com
   `whois -h $hostname " -c -p $ip" >> whois-res.txt`
 done


