import random


class GridWorld1D:
    """
    1D GridWorld environment with hidden goal and shaped rewards.

    - States: 0, 1, ..., N-1
    - Actions: 0 = left, 1 = right
    - On each episode:
        * goal_state is chosen randomly in [0, N-1]
        * start_state is chosen randomly != goal_state
    - Rewards:
        * +10.0 when agent reaches goal -> episode terminates
        * otherwise:
            - -0.1 if distance to goal decreases
            - -0.2 if distance to goal stays same or increases
        * if step_limit reached without goal:
            - additional -100.0 on that last step, then terminates
    """

    def __init__(self, N=10, step_limit=100, seed=None):
        self.N = N
        self.step_limit = step_limit
        self.rng = random.Random(seed)

        self.state = None
        self.goal_state = None
        self.steps_taken = 0

    def reset(self):
        """Reset the environment for a new episode and return initial state."""
        self.goal_state = self.rng.randrange(self.N)
        start_state = self.rng.randrange(self.N)
        # Ensure start_state != goal_state
        while start_state == self.goal_state:
            start_state = self.rng.randrange(self.N)

        self.state = start_state
        self.steps_taken = 0
        return self.state

    def step(self, action):
        """
        Take an action (0=left, 1=right) and return (next_state, reward, done).

        The agent does NOT observe goal_state or how rewards are computed.
        """
        assert action in (0, 1), "Invalid action, must be 0 (left) or 1 (right)."

        old_state = self.state

        # Move
        if action == 0:  # left
            self.state = max(self.state - 1, 0)
        else:  # right
            self.state = min(self.state + 1, self.N - 1)

        self.steps_taken += 1

        # Check goal
        if self.state == self.goal_state:
            reward = 10.0
            done = True
            return self.state, reward, done

        # Not at goal: shaped step penalty
        old_dist = abs(old_state - self.goal_state)
        new_dist = abs(self.state - self.goal_state)

        if new_dist < old_dist:
            reward = -0.1  # moved closer
        else:
            reward = -0.2  # moved away or same distance

        # Step limit check
        done = False
        if self.steps_taken >= self.step_limit:
            reward += -100.0
            done = True

        return self.state, reward, done


# ========================
# Policies
# ========================

def random_policy(state, env):
    """
    Random policy:
    Returns 0 (left) or 1 (right) with equal probability.
    """
    




def monotonous_policy(state, env):
    """
    Monotonous policy:
    - Move in one direction until hitting a wall.
    - When at a wall, reverse direction.
    Uses a global variable to track current direction.
    """
    
def wildcard_policy(state, env):
    """
    Your own policy.

    Example implementation:
    - Prefer moving toward the *center* of the line.
    - If in the left half, move right.
    - If in the right half, move left.
    This does NOT use the hidden goal_state.
    """
    

# ========================
# Episode runner
# ========================

def run_episode(env, policy_fn, max_steps=100):
    """
    Run a single episode using the given policy function.

    Returns:
        total_return (float),
        steps (int)
    """
    state = env.reset()
    total_return = 0.0

    for t in range(max_steps):
        action = policy_fn(state, env)
        next_state, reward, done = env.step(action)
        total_return += reward
        state = next_state
        if done:
            return total_return, t + 1

    # If we exit the loop without done=True, the environment
    # should already have applied the timeout penalty.
    return total_return, max_steps


# ========================
# Experiments
# ========================

def run_experiments():
    env = GridWorld1D(N=10, step_limit=100, seed=42)

    policies = [
        ("random_policy", random_policy),
        ("monotonous_policy", monotonous_policy),
        ("wildcard_policy", wildcard_policy),
    ]

    episodes_per_policy = 50

    for name, policy_fn in policies:
        returns = []
        steps_list = []

        for _ in range(episodes_per_policy):
            G, steps = run_episode(env, policy_fn, max_steps=env.step_limit)
            returns.append(G)
            steps_list.append(steps)

        avg_return = sum(returns) / len(returns)
        avg_steps = sum(steps_list) / len(steps_list)
        print(
            f"Policy: {name:17s} | "
            f"Avg Return: {avg_return:8.3f} | "
            f"Avg Steps: {avg_steps:6.2f}"
        )


if __name__ == "__main__":
    run_experiments()

    # Optional COMMENT for students:
    # After running, briefly describe:
    # - Which policy had the highest average return?
    # - Why that might be the case, using the language of state, action,
    #   reward, return, and goal.
