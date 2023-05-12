'''
Utilizza la libreria requests per effettuare una richiesta API al servizio di verifica 
degli indirizzi IP di Tor. Per installarla utilizzare il comando pip install requests. 
Dopo aver eseguito lo script, ti verrà chiesto di inserire l'indirizzo IP da verificare. 
Lo script effettuerà una richiesta all'URL del servizio di verifica di Tor e verificherà 
se l'indirizzo IP specificato è un nodo di uscita di Tor o meno.
'''

import requests

def is_tor_exit_node(ip_address):
    url = f"https://check.torproject.org/exit-addresses"
    response = requests.get(url)
    response_text = response.text

    return ip_address in response_text

ip_to_check = input("Inserisci l'indirizzo IP da verificare: ")
result = is_tor_exit_node(ip_to_check)

if result:
    print("L'indirizzo IP è un nodo di uscita di Tor.")
else:
    print("L'indirizzo IP non è un nodo di uscita di Tor.")
