import numpy as np
import matplotlib.pyplot as plt
import math
import time

def generate_cities(n, width=100, height=100):
    return np.random.rand(n, 2) * [width, height]

def distance(c1, c2):
    return np.sqrt(np.sum((c1 - c2) ** 2))

def total_cost(path, cities):
    return sum(distance(cities[path[i]], cities[path[(i + 1) % len(path)]]) for i in range(len(path)))

def simulated_annealing(cities, initial_temp=10000, cooling_rate=0.9995, stop_temp=1e-8):
    n = len(cities)
    current_path = list(range(n))
    np.random.shuffle(current_path)
    current_cost = total_cost(current_path, cities)
    best_path, best_cost = current_path[:], current_cost
    temperature = initial_temp
    costs, times, probabilities = [], [], []
    
    start_time = time.time()
    while temperature > stop_temp:
        i, j = np.random.randint(0, n, 2)
        new_path = current_path[:]
        new_path[i], new_path[j] = new_path[j], new_path[i]
        new_cost = total_cost(new_path, cities)
        cost_diff = new_cost - current_cost
        
        # Acceptance Probability
        if cost_diff < 0 or np.random.rand() < math.exp(-cost_diff / temperature):
            current_path, current_cost = new_path, new_cost
            probabilities.append(math.exp(-cost_diff / temperature) if cost_diff > 0 else 1)
            
            if new_cost < best_cost:
                best_path, best_cost = new_path[:], new_cost
        
        costs.append(current_cost)
        times.append(time.time() - start_time)
        temperature *= cooling_rate
    
    return best_path, best_cost, costs, times, probabilities, start_time

def plot_results(cities, path, costs, times, probabilities):
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))

    # Final path visualization
    axs[0, 0].plot([cities[i][0] for i in path + [path[0]]],
                   [cities[i][1] for i in path + [path[0]]], marker='o')
    axs[0, 0].set_title("Best TSP Path")

    # Cost over iterations
    axs[0, 1].plot(costs, label="Total Cost")
    axs[0, 1].set_title("Total Cost per Iteration")
    axs[0, 1].set_xlabel("Iteration")
    axs[0, 1].set_ylabel("Total Cost")

    # Time per iteration
    axs[1, 0].plot(times, costs, label="Time vs Cost")
    axs[1, 0].set_title("Total Cost Over Time")
    axs[1, 0].set_xlabel("Time (seconds)")
    axs[1, 0].set_ylabel("Total Cost")

    # Acceptance Probability over iterations
    axs[1, 1].plot(probabilities, label="Acceptance Probability")
    axs[1, 1].set_title("Acceptance Probability per Iteration")
    axs[1, 1].set_xlabel("Iteration")
    axs[1, 1].set_ylabel("Probability")

    plt.tight_layout()
    plt.show()

# Number of cities
n_cities = 20
cities = generate_cities(n_cities)

# Run Simulated Annealing
best_path, best_cost, costs, times, probabilities, start_time = simulated_annealing(cities)

print(f"Best path cost: {best_cost}")
print(f"Time taken: {time.time() - start_time} seconds")

# Plot results
plot_results(cities, best_path, costs, times, probabilities)


