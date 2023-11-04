# Simulated MAC address table (dictionary)
mac_table = {}

def update_mac_table(source_mac, port):
    # Update the MAC address table with the source MAC address and associated port
    mac_table[source_mac] = port

def display_mac_table():
    # Print the contents of the MAC address table
    print("MAC Address Table:")
    for mac, port in mac_table.items():
        print(f"MAC: {mac}, Port: {port}")

# Simulate network traffic and MAC learning
update_mac_table("00:11:22:33:44:55", 1)  # Device with MAC 00:11:22:33:44:55 on port 1
display_mac_table()

update_mac_table("AA:BB:CC:DD:EE:FF", 2)  # Device with MAC AA:BB:CC:DD:EE:FF on port 2
display_mac_table()

update_mac_table("00:11:22:33:44:55", 3)  # Device with MAC 00:11:22:33:44:55 now on port 3
display_mac_table()
