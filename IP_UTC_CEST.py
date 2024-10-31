"""
Script Python che processa il file txt fornito, estrae gli indirizzi IP e le date in UTC, 
quindi li converte in orario italiano (CET o CEST, a seconda del periodo dell'anno)
"""

import pytz
from datetime import datetime

# Definizione del fuso orario per l'Italia (CET/CEST gestito automaticamente)
italy_tz = pytz.timezone('Europe/Rome')
utc_tz = pytz.utc

def convert_utc_to_italy(utc_time_str, date_format='%d/%m/%Y %H:%M:%S'):
    # Converte la stringa in oggetto datetime UTC
    utc_time = datetime.strptime(utc_time_str, date_format)
    utc_time = utc_tz.localize(utc_time)

    # Converte da UTC a orario italiano
    italy_time = utc_time.astimezone(italy_tz)
    return italy_time

def process_file(input_file, output_file):
    result = []

    with open(input_file, 'r') as file:
        for line in file:
            # Separazione dell'indirizzo IP e della data
            parts = line.strip().split()
            ip = parts[0]
            date_str = parts[1]
            time_str = parts[2]
            datetime_str = f"{date_str} {time_str}"

            # Conversione della data e ora da UTC a orario italiano
            italy_time = convert_utc_to_italy(datetime_str)

            # Formattazione del risultato
            result.append(f"{ip} {italy_time.strftime('%d/%m/%Y %H:%M:%S %Z%z')}")

    # Scrittura dell'output nel file specificato
    with open(output_file, 'w') as out_file:
        for line in result:
            out_file.write(line + '\n')

# Esegui il processo
input_file = r'C:\Users\Administrator\Dropbox\Sorgenti\PYTHON\2_IP\Voda.txt'  # Il file che hai caricato
output_file = r'C:\Users\Administrator\Dropbox\Sorgenti\PYTHON\2_IP\output_converted_times.txt'
process_file(input_file, output_file)

print(f"Il file è stato processato e i risultati sono stati salvati in {output_file}.")
