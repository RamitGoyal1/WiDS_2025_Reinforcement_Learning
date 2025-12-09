# README.md

## Week 1 Coding Assignment – 1D GridWorld and Fixed Policies

### Objective

Implement a minimal reinforcement learning setup in Python:

- A 1D GridWorld environment with **hidden goal** and **internal reward computation**.  
- Three **fixed policies** (no learning):  
  1. `random_policy`  
  2. `monotonous_policy`  
  3. `wildcard_policy` (your own design)  
- Run each policy for multiple episodes and compare **average returns**.

Your code should focus on the **agent–environment interaction loop**:  
on each time step the agent chooses an action, and the environment returns `(next_state, reward, done)`.

---

### Environment specification

We work with a 1D grid of `N` cells:

- States: integers `0, 1, ..., N-1`.  
- At the start of every episode:
  - The **goal** is placed at a random cell.  
  - The **agent** is placed at a random *different* cell.  
- Actions:  
  - `0` = move left  
  - `1` = move right  
- Dynamics:
  - Left: `state = max(state - 1, 0)`  
  - Right: `state = min(state + 1, N - 1)`  

#### Rewards (computed internally by the environment)

The environment knows the goal position and uses it to compute rewards:

- If the agent reaches the goal:
  - Reward: `+10.0`  
  - Episode ends (`done = True`).  
- Otherwise:
  - If the agent’s move **reduces** the distance to the goal: reward `-0.1`.  
  - If the agent’s move **increases or keeps** the same distance to the goal: reward `-0.2`.  
- There is also a **step limit** (e.g., 100 steps):
  - If this limit is reached without hitting the goal:
    - Additional penalty: `-100.0` (on that last step).  
    - Episode ends.

**Important:**  
The *agent* does **not** know the goal position or how rewards are computed.  
It only observes:

- Current state (its position index).  
- Reward returned by `env.step(action)`.

---

### What you must implement

You will work in `main.py`. Your tasks:

1. **Understand the provided `GridWorld1D` environment class**.  
   - Read how `reset()` and `step()` work.  
   - Do not change its interface.

2. Implement three policy functions:

### Question for reflection:
How would your apprach towards designing the wildcard policy change if the agent was allowed to loop around. 
That is to say , taking a right step on the righ most cell will transport you to the left most cell