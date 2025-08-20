To create a Python program named "eco-routify" that optimizes delivery routes to minimize carbon emissions using real-time data analytics and machine learning, we would need to integrate several key components. These include data acquisition, real-time route optimization, and a machine learning model that can decide on the best routes based on various parameters like distance, traffic conditions, and emission data.

Here’s a simple outline of how such a program might look, with added comments and error handling:

```python
import random
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Dummy data for demonstration
DESTINATIONS = ["Location A", "Location B", "Location C", "Location D"]

# Sample function to get real-time data (e.g., traffic, emissions)
def fetch_real_time_data():
    try:
        # Simulating real-time data fetch with random values
        traffic_data = random.choice(["light", "moderate", "heavy"])
        emission_rates = random.uniform(0.2, 0.5)  # Dummy CO2 rates in kg/km
        logging.info("Real-time data fetched successfully")
        return traffic_data, emission_rates
    except Exception as e:
        logging.error(f"Error fetching real-time data: {str(e)}")
        return None, None

# Dummy function to calculate route score based on various factors
def calculate_route_score(destination, traffic_data, emission_rates):
    try:
        # Simple scoring model - lower is better
        traffic_weight = {"light": 1, "moderate": 1.5, "heavy": 2}
        score = DESTINATIONS.index(destination) * traffic_weight.get(traffic_data, 0) * emission_rates
        logging.info(f"Score for {destination}: {score}")
        return score
    except Exception as e:
        logging.error(f"Error calculating route score for {destination}: {str(e)}")
        return float('inf')


# Function to optimize routes
def optimize_routes():
    try:
        traffic_data, emission_rates = fetch_real_time_data()
        
        if traffic_data is None or emission_rates is None:
            logging.error("Failed to optimize routes due to lack of real-time data.")
            return

        scores = {}
        for destination in DESTINATIONS:
            score = calculate_route_score(destination, traffic_data, emission_rates)
            scores[destination] = score

        # Choose the route with the lowest score
        optimal_destination = min(scores, key=scores.get)
        logging.info(f"Optimal route selected: {optimal_destination} with score {scores[optimal_destination]}")
        return optimal_destination
    except Exception as e:
        logging.error(f"Error optimizing routes: {str(e)}")

# Main function
def main():
    try:
        logging.info("Eco-Routify Optimization Started")
        optimal_route = optimize_routes()
        if optimal_route:
            print(f"Optimal route chosen: {optimal_route}")
        else:
            print("Failed to determine the optimal route.")
    except Exception as e:
        logging.error(f"Error in main function: {str(e)}")

if __name__ == "__main__":
    main()
```

### Key Components and Considerations:

1. **Real-time Data Acquisition**: You would normally integrate with APIs to get real-time traffic and emissions data. Here, it is simulated with random choices.

2. **Route Optimization**: Based on a simple scoring function. In practice, using machine learning could involve more complex considerations, collecting historical data, training models, etc.

3. **Error Handling**: Introduced to manage unexpected exceptions, ensuring the program doesn’t crash and logs errors appropriately.

4. **Logging**: Helps trace execution flow and diagnose issues effectively.

This program is a prototype and would need enhancements such as actual data fetching, a robust machine learning model, more sophisticated optimization algorithms, and perhaps a user interface for scalability and production-level implementation.