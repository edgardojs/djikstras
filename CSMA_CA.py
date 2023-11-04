import random

# Number of devices
num_devices = 5

# Simulate a shared network channel
shared_channel = []

# Simulate devices attempting to transmit
for i in range(num_devices):
    if random.random() < 0.5:
        shared_channel.append(f"Device {i} wants to transmit")

# Check if the channel is clear
if not shared_channel:
    print("Channel is clear; device can transmit")
else:
    print("Channel is busy; device must wait")

# In a real simulation, you'd have backoff timers, contention windows, and more.
