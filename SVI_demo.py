class SVI:
    def __init__(self, vlan_id, ip_address):
        self.vlan_id = vlan_id
        self.ip_address = ip_address
        self.routing_table = {}

    def add_route(self, destination_subnet, next_hop):
        self.routing_table[destination_subnet] = next_hop

    def route_traffic(self, source_ip, destination_ip):
        source_subnet = self.get_subnet(source_ip)
        destination_subnet = self.get_subnet(destination_ip)

        if destination_subnet in self.routing_table:
            next_hop = self.routing_table[destination_subnet]
            print(f"Routing from {source_ip} to {destination_ip} via {next_hop}")
        else:
            print(f"No route found for {destination_ip}")

    def get_subnet(self, ip_address):
        parts = ip_address.split('.')
        return f"{parts[0]}.{parts[1]}.{parts[2]}.0/24"


# Create SVIs for VLANs
s1 = SVI(10, "192.168.10.1")
s2 = SVI(20, "192.168.20.1")
s3 = SVI(30, "192.168.30.1")

# Add routes to the routing tables
s1.add_route("192.168.20.0/24", "192.168.10.2")
s1.add_route("192.168.30.0/24", "192.168.10.3")
s2.add_route("192.168.10.0/24", "192.168.20.2")
s2.add_route("192.168.30.0/24", "192.168.20.3")
s3.add_route("192.168.10.0/24", "192.168.30.2")
s3.add_route("192.168.20.0/24", "192.168.30.3")

# Simulate traffic routing
s1.route_traffic("192.168.10.10", "192.168.20.20")
s2.route_traffic("192.168.20.20", "192.168.30.30")
s3.route_traffic("192.168.30.30", "192.168.10.10")
s1.route_traffic("192.168.10.10", "192.168.40.40")  # No route found

