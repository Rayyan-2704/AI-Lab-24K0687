import numpy as np

states = ["Sunny", "Cloudy", "Rainy"]
transition_matrix = np.array([
    [0.6, 0.3, 0.1],
    [0.3, 0.4, 0.3],
    [0.2, 0.3, 0.5]
])

def simulate_weather(days):
    current_state = 0
    sequence = [states[current_state]]

    for _ in range(days - 1):
        next_state = np.random.choice([0, 1, 2], p = transition_matrix[current_state])
        sequence.append(states[next_state])
        current_state = next_state

    return sequence


def count_rainy_days(sequence):
    return sequence.count("Rainy")


weather_sequence = simulate_weather(10)
print("Weather for 10 days:")
print(weather_sequence)

rainy_days = count_rainy_days(weather_sequence)
print("\nNumber of Rainy Days:", rainy_days)

simulations = 10000
count_atleast_3_rainy = 0

for _ in range(simulations):
    seq = simulate_weather(10)
    if count_rainy_days(seq) >= 3:
        count_atleast_3_rainy += 1

probability = count_atleast_3_rainy / simulations
print("\nProbability of at least 3 rainy days in 10 days:")
print(probability)
