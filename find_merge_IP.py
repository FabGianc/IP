# Estrae gli indirizzi IP da più file all'interno della cartella <percorso_cartella_input>
# e li memorizza all'interno della cartella <percorso_cartella_output>
# Crea un file <percorso_file_unificato.txt> dove viene fatto il merge di tutti gli indirizzi IP
# e successivamente vengono rimossi i duplicati

import os
import re

# Definisci la cartella di input, la cartella di output e il percorso del file unificato
cartella_input = r'percorso_cartella_output'
cartella_output = r'percorso_cartella_output'
percorso_file_unificato = 'percorso_file_unificato.txt'

# Crea la cartella di output se non esiste già
if not os.path.exists(cartella_output):
    os.makedirs(cartella_output)

# Crea la regex per cercare gli indirizzi IP
pattern_ip = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

# Elabora tutti i file nella cartella di input e unisci gli indirizzi IP
indirizzi_ip_unificati = set()
for nome_file in os.listdir(cartella_input):
    percorso_file_input = os.path.join(cartella_input, nome_file)

    if os.path.isfile(percorso_file_input):
        # Leggi il contenuto del file di input
        with open(percorso_file_input, 'r') as file_input:
            contenuto = file_input.read()

        # Trova gli indirizzi IP nel contenuto del file
        indirizzi_ip = pattern_ip.findall(contenuto)

        # Aggiungi gli indirizzi IP alla lista unificata
        indirizzi_ip_unificati.update(indirizzi_ip)

        # Scrivi gli indirizzi IP nel file di output
        percorso_file_output = os.path.join(cartella_output, nome_file)
        with open(percorso_file_output, 'w') as file_output:
            for ip in indirizzi_ip:
                file_output.write(ip + '\n')

# Scrivi gli indirizzi IP unificati nel file unificato
with open(percorso_file_unificato, 'w') as file_unificato:
    for ip in indirizzi_ip_unificati:
        file_unificato.write(ip + '\n')
