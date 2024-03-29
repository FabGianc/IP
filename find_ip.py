# Estrae gli indirizzi IP da un file di log e li memorizza in un file txt

import re

# Apri il file in modalità di lettura e leggi il contenuto
with open('file_di_log.log', 'r') as f:
    content = f.read()

# Crea una regex per cercare gli indirizzi IP nel contenuto del file di testo
ip_regex = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
ip_list = re.findall(ip_regex, content)

# Apri un nuovo file in modalità di scrittura e scrivi gli indirizzi IP trovati
with open('file_IP.txt', 'w') as output_file:
    for ip in ip_list:
        output_file.write(ip + '\n')
