'''
Utilizza la libreria requests per effettuare una richiesta API al servizio di verifica 
degli indirizzi IP di Tor. Per installarla utilizzare il comando pip install requests. 
Lo script legge gli indirizzi IP da verificare da un file di testo e effettuerà una richiesta 
all'URL del servizio di verifica di Tor e risponderà se l'indirizzo IP specificato è un nodo 
di uscita di Tor o meno.

Durante l'esecuzione, lo script chiederà di inserire il nome del file che contiene gli indirizzi IP
da verificare e il nome del file di output in cui verranno salvati i risultati. 
I risultati saranno scritti nel file di output con una riga per ogni indirizzo IP, 
indicando se è un nodo di uscita di Tor o meno.

Eseguilo nella stessa cartella dove si trova il file da analizzare.
'''

import requests

def is_tor_exit_node(ip_address):
    url = "https://check.torproject.org/exit-addresses"
    response = requests.get(url)
    response_text = response.text

    return ip_address in response_text

# Leggi gli indirizzi IP da un file di testo
filename = input("Inserisci il nome del file che contiene gli indirizzi IP: ")
with open(filename, 'r') as file:
    ip_addresses = file.read().splitlines()

# Verifica se gli indirizzi IP sono nodi di uscita di Tor e salva i risultati in un file
output_filename = input("Inserisci il nome del file di output: ")
with open(output_filename, 'w') as output_file:
    for ip_address in ip_addresses:
        result = is_tor_exit_node(ip_address)
        if result:
            output_file.write(f"L'indirizzo IP {ip_address} è un nodo di uscita di Tor.\n")
        else:
            output_file.write(f"L'indirizzo IP {ip_address} non è un nodo di uscita di Tor.\n")

print("Verifica completata. I risultati sono stati salvati nel file di output.")
