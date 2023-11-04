import matplotlib.pyplot as plt

# Number of subcarriers and users
num_subcarriers = 64
num_users = 8

# Create a figure
fig, ax = plt.subplots()

# Plot subcarriers
for i in range(num_subcarriers):
    ax.plot([i, i], [0, num_users], 'b-')

# Plot users
for j in range(num_users):
    ax.plot([0, num_subcarriers], [j, j], 'r--')

# Set labels
ax.set_xlabel('Subcarriers')
ax.set_ylabel('Users')

# Set title
ax.set_title('Simplified OFDMA Visualization')

plt.grid(True)
plt.show()
