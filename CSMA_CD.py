import random

# Number of devices
num_devices = 5

# Shared Ethernet channel
shared_channel = []

# Simulate devices attempting to transmit
for i in range(num_devices):
    if random.random() < 0.5:
        shared_channel.append(f"Device {i} wants to transmit")

# Check for collisions
if len(shared_channel) > 1:
    print("Collision detected!")
    for device in shared_channel:
        print(device + " collided")

# If no collision, successful transmission
else:
    print("Data transmitted successfully")

# In a real simulation, you'd have backoff timers, retransmission, and more.