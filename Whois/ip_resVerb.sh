#!/bin/bash
for ip in `cat ip_list.txt`
do
   echo $ip
   hostname=v4.whois.cymru.com
   `whois -h $hostname " -v $ip" >> whois-res2.txt`
 done


