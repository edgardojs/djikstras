class Switch:
    def __init__(self, name, is_root=False):
        self.name = name
        self.is_root = is_root
        self.connected_ports = []
        self.root_distance = 0

    def add_port(self, port, distance):
        self.connected_ports.append((port, distance))

def spanning_tree(switches):
    # Find the switch with the smallest root distance (i.e., the root switch)
    root_switch = min(switches, key=lambda s: s.root_distance)

    # Determine the shortest path to the root switch for each switch
    for switch in switches:
        if switch != root_switch:
            shortest_path = min(
                (root_switch.root_distance + distance for _, distance in switch.connected_ports)
            )
            switch.root_distance = shortest_path

    # Identify the designated ports on each switch
    for switch in switches:
        for port, distance in switch.connected_ports:
            if root_switch.root_distance + distance == switch.root_distance:
                port.is_designated = True

    return root_switch, switches

# Create switches and define their connections and distances
switch_A = Switch("A", is_root=True)
switch_B = Switch("B")
switch_C = Switch("C")
switch_D = Switch("D")

switch_A.add_port(switch_B, 1)
switch_A.add_port(switch_C, 2)
switch_B.add_port(switch_A, 1)
switch_B.add_port(switch_D, 1)
switch_C.add_port(switch_A, 2)
switch_C.add_port(switch_D, 1)
switch_D.add_port(switch_B, 1)
switch_D.add_port(switch_C, 1)

# Perform the Spanning Tree Protocol
root_switch, switches = spanning_tree([switch_A, switch_B, switch_C, switch_D])

# Print the results
print(f"Root Switch: {root_switch.name}")
print("Switches in the Spanning Tree:")
for switch in switches:
    print(f"Switch {switch.name} (Root Distance: {switch.root_distance})")

print("Designated Ports:")
for switch in switches:
    for port, _ in switch.connected_ports:
        if port.is_designated:
            print(f"Switch {switch.name} -> {port.name}")
