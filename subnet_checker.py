import ipaddress

# Input IP address in the format "192.168.1.0/24"
input_ip = input("Enter the IP address and subnet prefix (e.g., 192.168.1.0/24): ")

try:
    # Parse the input into an IPv4 network object
    network = ipaddress.IPv4Network(input_ip, strict=False)
    
    # Extract IP address, subnet mask, and default gateway
    ip_address = network.network_address
    subnet_mask = network.netmask
    default_gateway = network.network_address + 1  # Default gateway is usually the first IP in the subnet
    
    # Display in binary and decimal format
    print("IP Address (Decimal):", ip_address)
    print("IP Address (Binary):", bin(int(ip_address)))
    print("Subnet Mask (Decimal):", subnet_mask)
    print("Subnet Mask (Binary):", bin(int(subnet_mask)))
    print("Default Gateway (Decimal):", default_gateway)
    print("Default Gateway (Binary):", bin(int(default_gateway)))

except ValueError:
    print("Invalid input. Please provide an IP address and subnet prefix (e.g., 192.168.1.0/24).")