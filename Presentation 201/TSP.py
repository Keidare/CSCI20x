"""
Swailem Neil Angelo G. Lumba
203094
November 14, 2024

I have not discussed the Python language code in my program
with anyone other than my instructor or the teaching assistants
assigned to this course.

I have not used Python language code obtained from another student,
or any other unauthorized source, either modified or unmodified.

If any Python language code or documentation used in my program
was obtained from another source, such as a textbook or website,
that has been clearly noted with a proper citation in the comments
of my program.

"""


import numpy as np
import matplotlib.pyplot as plt
import math
import time

'''
Generate n random points (x, y) within the specified area
Return the array of cities
'''

def generate_cities(n, width=100, height=100):
    return np.random.rand(n, 2) * [width, height]


'''
Compute the Euclidean distance between coordinates c1 and c2
Return the distance
'''
def distance(c1, c2):
    return np.sqrt(np.sum((c1 - c2) ** 2))

'''
Initialize total distance to 0
For each city in the path:
    Compute the distance to the next city
Add the distance to the starting city (for round trip)
Return the total distance
'''

def total_cost(path, cities):
    return sum(distance(cities[path[i]], cities[path[(i + 1) % len(path)]]) for i in range(len(path)))

'''
Initialize a random path and calculate its cost
Set temperature = initial_temp

While temperature > stop_temp:
    Randomly select two cities and swap them in the path
    Calculate the new path cost
    Calculate the cost difference between new and current paths
    
    If new cost is better:
        Accept new path
    Else:
        Accept with probability P = exp(-cost_diff / temperature)
    
    Update best path and cost if new path is better
    Reduce temperature by multiplying with cooling_rate

Return best path, best cost, and metrics for visualization
'''
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

    axs[0, 0].plot([cities[i][0] for i in path + [path[0]]],
                   [cities[i][1] for i in path + [path[0]]], marker='o')
    axs[0, 0].set_title("Best TSP Path")

    axs[0, 1].plot(costs, label="Total Cost")
    axs[0, 1].set_title("Total Cost per Iteration")
    axs[0, 1].set_xlabel("Iteration")
    axs[0, 1].set_ylabel("Total Cost")

    axs[1, 0].plot(times, costs, label="Time vs Cost")
    axs[1, 0].set_title("Total Cost Over Time")
    axs[1, 0].set_xlabel("Time (seconds)")
    axs[1, 0].set_ylabel("Total Cost")

    axs[1, 1].plot(probabilities, label="Acceptance Probability")
    axs[1, 1].set_title("Acceptance Probability per Iteration")
    axs[1, 1].set_xlabel("Iteration")
    axs[1, 1].set_ylabel("Probability")

    plt.tight_layout()
    plt.show()

# Number of cities
n_cities = 20
cities = generate_cities(n_cities)

best_path, best_cost, costs, times, probabilities, start_time = simulated_annealing(cities)

print(f"Best path cost: {best_cost}")
print(f"Time taken: {time.time() - start_time} seconds")

plot_results(cities, best_path, costs, times, probabilities)


