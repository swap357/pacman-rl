# Pacman RL agent


Code files edited:
./search/search.py
./multiagent/multiAgents.py
./reinforcement/qlearningAgents.py


Search algorithms:
[requires python2 environment to run following commands]


### DFS


Tiny - python pacman.py -l tinyMaze -p SearchAgent
Medium - python pacman.py -l mediumMaze -p SearchAgent --frameTime=0.01
Big - python pacman.py -l bigMaze -z .5 -p SearchAgent --frameTime=0.01


### BFS


Tiny - python pacman.py -l tinyMaze -p SearchAgent -a fn=bfs
Medium - python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs --frameTime=0.01
Big - python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=bfs --frameTime=0.01


### Uniform cost search


Tiny - python pacman.py -l tinyMaze -p SearchAgent -a fn=ucs
Medium - python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs --frameTime=0.01
Big - python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=ucs --frameTime=0.01
Medium Dotted - python pacman.py -l mediumDottedMaze -p StayEastSearchAgent
Medium Scary - python pacman.py -l mediumScaryMaze -p StayWestSearchAgent


### A-star - Heuristic


Tiny - python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
Medium - python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime=0.01
Big - python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic --frameTime=0.01


### A-star - Without Heuristic


Tiny - python pacman.py -l tinyMaze -p SearchAgent -a fn=astar,heuristic=nullHeuristic
Medium - python pacman.py -l mediumMaze -p SearchAgent -a fn=astar,heuristic=nullHeuristic --frameTime=0.01
Big - python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=nullHeuristic --frameTime=0.01


Multi-agent search algorithms:
[Pacman will play looking ahead depth=3 steps.]

### Minimax search
small - python pacman.py -p MinimaxAgent -a depth=4 -l smallClassic
medium - python pacman.py -p MinimaxAgent -a depth=4 -l mediumClassic


### Alpha-beta pruning
small - python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
medium - python pacman.py -p AlphaBetaAgent -a depth=3 -l mediumClassic


## Reinforcement learning:
[requires python3 environment to run following commands]

### Q-learning
small -
python pacman.py -p PacmanQAgent -x 1400 -n 1410 -l smallGrid --frameTime=0.1 -a epsilon=0.05
medium - python pacman.py -p PacmanQAgent -x 2000 -n 2010 -l mediumClassic --frameTime=0.1 -a epsilon=0.05


### Approximate Q-learning
small - python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l smallGrid
medium - python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 50 -n 60 -l mediumGrid
mediumClassic - python pacman.py -p ApproximateQAgent -a extractor=SimpleExtractor -x 0 -n 10 -l mediumClassic --frameTime=0.01
