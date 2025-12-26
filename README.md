# SupplyChain-Location-Optimization
A strategic decision-support system for warehouse location selection, integrating the Analytic Hierarchy Process (AHP) for multi-criteria weighting and Monte Carlo simulations to model operational cost volatility.
# Strategic Warehouse Location Optimization

## Introduction
This project focuses on solving the multi-faceted problem of warehouse location selection. By integrating **Multi-Criteria Decision Analysis (MCDA)** for strategic alignment and **Monte Carlo Simulations** for financial risk assessment, this model provides a data-driven approach to logistics planning.

## Methodology

### 1. Analytic Hierarchy Process (AHP)
I applied AHP to weight three critical success factors for the facility:
- **Proximity to Suppliers (50%)**: Minimizing lead times is our top priority.
- **Labor Market Stability (30%)**: Evaluating the cost and availability of skilled workers.
- **Infrastructure Maturity (20%)**: Assessing road networks and utility reliability.

### 2. Probabilistic Modeling (Monte Carlo)
Static financial projections often fail to capture market volatility. I implemented a Monte Carlo simulation using a **Triangular Distribution** to model annual operating costs across 10,000 iterations. This allows us to visualize the "Value at Risk" (VaR) beyond simple averages.

## How to Run
1. Ensure you have `numpy` installed: `pip install numpy`
2. Run the script: `python optimizer.py`

## Conclusion
The simulation reveals that while City C offers the lowest theoretical cost, City B is the most resilient choice due to its lower variance and 95th-percentile risk exposure. 
