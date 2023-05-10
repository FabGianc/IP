# Ricerca il contenuto di un file (k_path) all'interno di tutti i file presenti in una cartella (s_path)
# Lo script viene usato per verificare se in nei file di log contenuti nella cartella <s_path> 
# vi sono exit node di TOR <k_path>

# Import Module
import os

# file contenente le chiavi di ricerca
k_path = 'C:\\Users\\Desktop\\tor-exit-nodes.lst'

# Cartella dei file in cui ricercare
s_path = 'C:\\Users\\Desktop\\Log_IP'

# Definisco la directory di lavoro
os.chdir(s_path)

def trova_nel_file(k_path, file_s_path):
    # apriamo entrambi i file, con with non abbiamo bisogno di eseguire il close finale
    with open(k_path, 'r') as reader, open(file_s_path, 'r') as search:
        i = 0 # contatore per le corrispondenze
        for line in reader:
            l = line.replace('\n', '')
            
            for line1 in search:
                if l in line1:
                    i+=1
                    print(i, ' ', l, '--->', line1,  end='')
                    key = l
                
            search.seek(0) # riporta all'inizio del file
        if i > 0:
            print(i, 'occorrenze di',key, 'nel file', file_s_path)
        else:
            print('Nessuna corrispondenza trovata nel file', file_s_path)


# itera tutti i file
for file in os.listdir():
	file_s_path = file
	trova_nel_file(k_path, file_s_path)	
