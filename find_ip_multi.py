import os
import re

# Definisci la cartella di input e di output
cartella_input = 'E:\Laservideo\\150820_DEMASI_Catanzaro\W3SVC1'
cartella_output = 'percorso_cartella_output'

# Crea la cartella di output se non esiste già
if not os.path.exists(cartella_output):
    os.makedirs(cartella_output)

# Crea la regex per cercare gli indirizzi IP
pattern_ip = re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b')

# Elabora tutti i file nella cartella di input
for nome_file in os.listdir(cartella_input):
    percorso_file_input = os.path.join(cartella_input, nome_file)
    percorso_file_output = os.path.join(cartella_output, nome_file)
    print(nome_file)

    if os.path.isfile(percorso_file_input):
        # Leggi il contenuto del file di input
        with open(percorso_file_input, 'r') as file_input:
            contenuto = file_input.read()

        # Trova gli indirizzi IP nel contenuto del file
        indirizzi_ip = pattern_ip.findall(contenuto)

        # Scrivi gli indirizzi IP nel file di output
        with open(percorso_file_output, 'w') as file_output:
            for ip in indirizzi_ip:
                file_output.write(ip + '\n')
