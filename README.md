# AI Algorithms

Python implementations of classic artificial-intelligence algorithms from my AI coursework — state-space search, adversarial search, genetic algorithms and simple rational agents. Each file is self-contained with a small inline problem instance and prints its result when run.

## Contents

### Search — `search/`

| File | Algorithm |
|---|---|
| `a_star_search.py` | A* search with an admissible heuristic on a weighted graph |
| `greedy_best_first_search.ipynb` | Greedy best-first search over an adjacency matrix |
| `uninformed_search_example_1.py`, `uninformed_search_example_2.py` | Dijkstra's shortest path, BFS, DFS, cycle detection and greedy graph colouring |

### Adversarial search — `adversarial_search/`

| File | Algorithm |
|---|---|
| `minimax.py` | Minimax over a four-level game tree, with the optimal path |
| `minimax_memoized.py` | Minimax with memoisation of evaluated nodes |
| `alpha_beta_pruning.py`, `alpha_beta_pruning_example_2.py` | Minimax with alpha-beta pruning |

### Genetic algorithms — `genetic_algorithms/`

| File | Problem |
|---|---|
| `knapsack_ga.py` | 0/1 knapsack (binary chromosomes, single-point crossover, bit-flip mutation) |
| `string_evolution_ga.py` | Evolving a random string towards a target string |
| `bin_packing_ga.py` | Bin packing — minimise the number of bins |
| `job_scheduling_ga.py` | Assigning jobs to machines to minimise makespan |

### Agents — `agents/`

| File | Agent |
|---|---|
| `treatment_recommendation_agent.py` | Utility-based agent choosing the treatment with the best effectiveness/side-effect trade-off |
| `virtual_personal_assistant.py` | Simple reflex assistant for tasks and meetings |
| `stock_trading_bot.py` | Moving-average crossover signals (buy/sell/hold) on Yahoo Finance data |

## Running

```bash
python search/a_star_search.py
python genetic_algorithms/job_scheduling_ga.py
```

The scripts use only the standard library, except `greedy_best_first_search.ipynb` (NumPy) and `stock_trading_bot.py` (`pip install yfinance`).
