'''
Per ottenere informazioni complete sul dominio associato a un indirizzo IP, 
utilizziamo la libreria ipwhois. Assicurati di installare la libreria 
eseguendo il comando pip install ipwhois prima di eseguire lo script.
Per ottenere informazioni aggiuntive anche per gli indirizzi IP senza un'associazione di dominio specifica, 
utilizziamo la libreria socket per eseguire una risoluzione DNS inversa e ottenere il nome host associato a quell'indirizzo IP.
'''

import socket

from ipwhois import IPWhois

''' 
La funzione domain_lookup() utilizza la libreria ipwhois per ottenere informazioni 
sul dominio associato a un indirizzo IP utilizzando il metodo lookup_rdap(). 
Se viene trovata una descrizione ASN nell'output, viene restituita la descrizione corrispondente. 
In caso contrario, viene restituito "N/D"
'''

def domain_lookup(ip_address):
    try:
        obj = IPWhois(ip_address)
        result = obj.lookup_rdap()
        if 'asn_description' in result:
            return result['asn_description']

        # Risoluzione DNS inversa per ottenere il nome host
        hostname = socket.gethostbyaddr(ip_address)[0]
        return hostname
    except Exception:
        pass
    return "N/D"

        
# Definisci il percorso del file contenente gli indirizzi IP
percorso_file_ip = r'C:\Users\Administrator\Downloads\Python\percorso_file_indirizzi_ip.txt'

# Definisci il percorso del file di output
percorso_file_output = r'C:\Users\Administrator\Downloads\Python\percorso_file_output.txt'

# Leggi gli indirizzi IP dal file
indirizzi_ip = []
with open(percorso_file_ip, 'r') as file_ip:
    indirizzi_ip = file_ip.read().splitlines()

# Effettua la ricerca dei domini per gli indirizzi IP
risultati_lookup = {}
for ip in indirizzi_ip:
    dominio = domain_lookup(ip)
    if dominio != "N/D":
        risultati_lookup[ip] = dominio
    
# Stampa a video e salva i risultati del lookup su file
with open(percorso_file_output, 'w') as file_output:
    for ip, dominio in risultati_lookup.items():
        print(f"{ip}: {dominio}")
        file_output.write(f"{ip}: {dominio}\n")
