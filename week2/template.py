import matplotlib.pyplot as plt
import numpy as np

"""
Initialize parameters
discount_factor=1
value_estimates = np.zeros(101) 
value_estimates[100] = 1  # terminal state value
policy = np.ones(100, dtype=int)  # initial policy: bet 1, ensure integer type
policy[0] = 0  # state 0 is terminal, no bet
"""

def solve_gambler(p_h, goal=100, tol=1e-9):
    v = np.zeros(goal + 1)
    v[goal] = 1.0 
    
    sweeps = []
    while True:
        sweeps.append(v.copy())
        delta = 0
        old_v = v.copy()
        for s in range(1, goal):
            actions = np.arange(min(s, goal - s) + 1)
            v_s = [p_h * old_v[s+a] + (1-p_h) * old_v[s-a] for a in actions]
            best_v = np.max(v_s)
            delta = max(delta, np.abs(best_v - old_v[s]))
            v[s] = best_v
        if delta < tol:
            break
    policy = np.zeros(goal + 1)
    for s in range(1, goal):
        actions = np.arange(min(s, goal - s) + 1)
        v_s = [round(p_h * v[s+a] + (1-p_h) * v[s-a], 10) for a in actions]
        policy[s] = actions[np.argmax(v_s)]
        
    return sweeps, v, policy

probs = [0.2, 0.4, 0.5, 0.7, 0.9]
fig, axes = plt.subplots(len(probs), 2, figsize=(12, 20))

for i, p in enumerate(probs):
    sweeps, final_v, final_p = solve_gambler(p)
    
    for step, s_v in enumerate(sweeps):
        if step % (max(1, len(sweeps)//5)) == 0 or step == len(sweeps)-1:
            axes[i, 0].plot(s_v, label=f'Sweep {step}')
    axes[i, 0].set_title(f'Value Function (p_h={p})')
    axes[i, 0].set_xlabel('Capital')
    axes[i, 0].set_ylabel('Value')

    axes[i, 1].step(range(101), final_p, where='mid')
    axes[i, 1].set_title(f'Optimal Policy (p_h={p})')
    axes[i, 1].set_xlabel('Capital')
    axes[i, 1].set_ylabel('Stake')

plt.tight_layout()
plt.show()
