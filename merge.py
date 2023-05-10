import os

# Definisci la cartella di output
cartella_output = 'percorso_cartella_output'

# Definisci il percorso del file di output finale
percorso_file_output = 'percorso_file_unificato.txt'

# Crea una lista vuota per contenere il contenuto dei file di output
contenuto_unificato = []

# Elabora tutti i file nella cartella di output
for nome_file in os.listdir(cartella_output):
    percorso_file = os.path.join(cartella_output, nome_file)

    if os.path.isfile(percorso_file):
        # Leggi il contenuto del file di output
        with open(percorso_file, 'r') as file_output:
            contenuto_file = file_output.readlines()

        # Aggiungi il contenuto del file alla lista unificata
        contenuto_unificato.extend(contenuto_file)

# Scrivi il contenuto unificato nel file di output finale
with open(percorso_file_output, 'w') as file_unificato:
    file_unificato.writelines(contenuto_unificato)
