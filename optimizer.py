import numpy as np

# Part 1: MCDA / AHP Weights
# These weights represent the importance of each criterion
weights = {
    "proximity": 0.50,
    "labor_cost": 0.30,
    "infrastructure": 0.20
}

# Part 2: Monte Carlo Simulation
def run_simulation(city_name, min_val, likely_val, max_val, iterations=10000):
    """
    Simulates annual operating costs over 10,000 scenarios.
    """
    # Using triangular distribution to account for uncertainty in logistics and labor
    simulated_costs = np.random.triangular(min_val, likely_val, max_val, iterations)
    
    avg_cost = np.mean(simulated_costs)
    risk_95 = np.percentile(simulated_costs, 95)
    
    return avg_cost, risk_95

# Scenario Data (Estimated Operating Costs)
cities = {
    "City_A": [450000, 500000, 750000], # Proximity-focused
    "City_B": [480000, 520000, 600000], # Infrastructure-focused
    "City_C": [400000, 550000, 900000]  # High volatility (Labor)
}

print("Simulation Results (Annual Operating Costs):")
for city, values in cities.items():
    avg, risk = run_simulation(city, values[0], values[1], values[2])
    print(f"{city}: Average: ${avg:,.0f} | 95th Percentile (Risk): ${risk:,.0f}")
