def get_ip_addresses(filename):
    ip_addresses = []
    with open(filename, 'r') as file:
        for line in file:
            ip = line.strip()
            if is_valid_ip(ip):
                ip_addresses.append(ip)
    return ip_addresses

def is_valid_ip(ip):
    # Verifica se un indirizzo IP è valido
    # Vengono considerati validi solo gli IPv4
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or int(part) < 0 or int(part) > 255:
            return False
    return True

# Definisci i percorsi dei file di input e output
filename1 = 'tor_exit_nodes.txt'
filename2 = 'file_unificato.txt'
output_file = 'risultato.txt'

# Ottieni gli indirizzi IP dai file di input
ip_addresses1 = get_ip_addresses(filename1)
ip_addresses2 = get_ip_addresses(filename2)

# Trova gli indirizzi IP comuni a entrambi i file
common_ip_addresses = list(set(ip_addresses1) & set(ip_addresses2))

# Scrivi gli indirizzi IP comuni sul file di output
with open(output_file, 'w') as file:
    file.write("Indirizzi IP comuni:\n")
    for ip in common_ip_addresses:
        print(ip)
        file.write(ip + '\n')

print("Risultati salvati su", output_file)
