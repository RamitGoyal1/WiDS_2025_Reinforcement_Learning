# README (Week 1)

This project implements a minimal Reinforcement Learning (RL) environment called **GridWorld1D** and compares three different agent policies.
## Optional COMMENT for students:
1. Which policy had the highest average return?
  The monotonous_policy had the highest average return (9.306).
2. Why that might be the case?
  In this environment, every 'action' that does not reach the 'goal' results in a negative 'reward'. Therefore, to maximize the total 'return', the agent must find the goal in the fewest steps possible. The monotonous policy systematically searches the 'state' space without retracing its steps, minimizing the accumulated negative rewards. In contrast, the wildcard policy biased actions toward the center; if the goal was at the edge, the agent never reached it, triggering the large timeout penalty and destroying the average return.

## How would your apprach towards designing the wildcard policy change if the agent was allowed to loop around. That is to say , taking a right step on the righ most cell will transport you to the left most cell
## If the environment allowed the agent to loop around, my design for the wildcard policy would shift to a simple "Always Move Right" strategy. In the current bounded grid, hitting a wall forces the agent to reverse and step back onto a cell it has already visited, which incurs a penalty without providing new information. However, in a looping world, moving consistently in one direction eliminates this backtracking completely; it ensures the agent visits a new, unvisited state at every single time step, guaranteeing the goal is found with maximum efficiency.
