import random
import matplotlib.pyplot as plt

# Define the states and generate random transition probabilities
states = ['Sunny', 'Cloudy', 'Rainy']

def generate_random_transition_matrix():
    transition_matrix = {}
    for state in states:
        remaining_prob = 1.0
        transition_matrix[state] = {}
        for next_state in states:
            if next_state == state:
                # If next_state is the same as the current state, set the probability to 1.
                transition_matrix[state][next_state] = 1.0
            else:
                # Generate a random probability between 0 and the remaining_prob.
                transition_matrix[state][next_state] = random.uniform(0, remaining_prob)
                remaining_prob -= transition_matrix[state][next_state]
        # Normalize the probabilities so they add up to 1.
        normalization_factor = 1 / sum(transition_matrix[state].values())
        for next_state in states:
            transition_matrix[state][next_state] *= normalization_factor
    return transition_matrix

# Function to generate a random Markov chain with random transition probabilities
def generate_random_markov_chain(num_steps):
    transition_matrix = generate_random_transition_matrix()
    chain = [random.choice(states)]

    print("Transition Probabilities:")
    for _ in range(num_steps - 1):
        current_state = chain[-1]
        print(f"Step {_ + 1} - From {current_state} to:")
        for next_state in states:
            print(f"  {next_state}: {transition_matrix[current_state][next_state]}")
        next_state = random.choices(states, 
            weights=[transition_matrix[current_state][s] for s in states])[0]
        chain.append(next_state)
        print(f"Selected State: {next_state}\n")

    return chain

# Generate a random Markov chain for 10 steps
num_steps = 10
random_markov_chain = generate_random_markov_chain(num_steps)

# Create a visualization of the random Markov chain
x = list(range(num_steps))
y = [states.index(state) for state in random_markov_chain]

plt.figure(figsize=(10, 3))
plt.plot(x, y, marker='o', linestyle='-', markersize=8, markerfacecolor='blue', color='blue')
plt.yticks(range(len(states)), states)
plt.xlabel('Time Steps')
plt.ylabel('States')
plt.title('Random Markov Chain Simulation with Random Transition Probabilities')
plt.grid(True)

plt.show()
