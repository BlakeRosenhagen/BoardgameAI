# Table of Contents


# Go Board Game
rules of game go here

## Scoring
Territory scoring: Most common method. Easier for casual play.
player_score += 1 for every point on the board that is completely surrounded by your own stones
player_score += 1 for each opponent's stone captured

Area Scoring: Alternate method. more convienent for computers.
player_score += 1 for every point on the board that is completely surrounded by your own stones
player_score += 1 for every stone you have on the board

Except in rare cases where youll get the same winner by either method

In this program the Ai assumes Area Scoring is used as winning method.

## Handicap
White player gets extra points as compensation for playing second. "Komi"
Komi = 6.5 with territory scoring.
Komi = 7.5 with area scoring. This is assumed for this program.

Weaker player takes black and place a few stones on the board before the game starts. When this is used komi is reduced to .5. Then the experienced player takes the first turn as white.
Usually the handicap stones are place on the star points, but is allowed anywhere.

## Restrictions
states every stone remaining on the board must have at least on open point. "Liberty"
It's illegal to play a move that will return the board to a previous state. "Ko"

# Game Theory
https://en.wikipedia.org/wiki/Game_theory
## Game Complexity
For example, chess has a average branching factor about 30. The initial state of the game has 20 options. This number increases as the game progresses. For the game of Go, there is a mcuh larger branching factor, as its initial state is 261


              
Board Size:              Number of positions on game board
*State-Space Complexity:  Number of legal game positions from the inital position of game
*Game Tree Size:          Total number of games that can be played ie number of leaf nodes in game tree at game's inital position    
*Decision Complexity: number of leaf nodes in the smallest decision tree that establishyes the value of the inital position
Game-Tree Complexity:    number of leaf nodes in the smallest full-width decision tree that establishes the value of the initial position. A full-width tree includes all nodes at each depth. Estimate of number of positions one would have to evaluate in a minimax search to determine value of initial position. Hard to estimate, but some games an apporximation can be used by the game's average branching factor b to the power of the number of piles d in an average game: GTC >= b^d
*Computational Complexity: the asymptotic difficulty of game as it grows arbitralily large. Aka big O notation or a member of complexity class

Average Game Length (piles) 
Branching Factor
Complexity Class

Games List:                                 Tic-Tac-Toe,     Chess,            Go
Board Size (Positions)                      9,               64,               361,
State-Space Complexity (as log to base10)   3,               47,               170,
Game-Tree Complexity (as log to base10)     5,               123,              360,
Average Game Length (piles)                 9,               70,               150,
Branching Factor                            4,               35,               250,
Complexity Class                            PSPACE-complete, EXPTIME-complete, EXPTIME-complete

**Look at this to get more info https://www.chessprogramming.org/Branching_Factor or https://en.wikipedia.org/wiki/Game_complexity or https://en.wikipedia.org/wiki/Complexity_class** 

The reason why their is a such a great disparity of branching factor for Chess when compared to go is the movement ruleset for each piece that restricts movement, as well as making pieces move from where they are present in the prior turn. These two apects reduce the amount of possible moves and thus reduces the branching factor. 

With the branching factor being much lower than Go, as  well as the average game lenth being less than half of Go, Game-Tree Complexity as derived by the function of GTC >= branching_factor ^ average_game_lenth monumentall reduces the GTC by 10^237.

As a step by step comparison. this chart shows the approximate number of possible board states given the first six moves

                        1st move,   2nd move,   3rd move,   4th move,   5th move,   6th move      nth move
Tic-Tac-Toe(w/illegal)  9,          72,         504,        3024,       15120,      60480         290,000
Chess(AVG BF of 35)     35,         *,          900,        27000,      810000,     24 million    10^64
Go (Avg BF of 250)      250,        *,          62500,      15 million, 4 billion,  1 trillion    10^359



"Finding the best move with minmax algorithm"
"pruning minimax tree to speed up algorithm"
"applying Monete Carlo tree search to games"

## Taxonomy of Games: ADD MORE TO THIS SECTION

# Core Functionality
point = Point(row, col)
move = Move.play(point)
boolean = gamestate.is_valid_move(move)

if boolean:
    game.apply_move(move)


# Artificial Intelligence
## Why AI
Artificial intellenge.....
## Man vs. Machine
This paragraph from Deepmind's website describing the types of neural networks they used to produce the AlphaGo, the strongest Go AI that beat a professional level Go player. I used this information to drive and guide my selection process of neural architecture.

"One neural network, the “policy network”, selects the next move to play. The other neural network, the “value network”, predicts the winner of the game. We introduced AlphaGo to numerous amateur games to help it develop an understanding of reasonable human play. Then we had it play against different versions of itself thousands of times, each time learning from its mistakes."

Mr Fan Hui., the three time raining European Champian of Go, was beaten 5-0 in 2015, which marked a point in history in which machine surpassed the cognition and ability of humans.

While I don't expect to construct an AI that stands up to AlphaGo, I would like to test my capabilites and gain a much deeper understanding about the field of machine learning, game theory and how different types of bots perceive, compute, predict, and execute different game strategies that emulate and perhaps surpass the ability of an average Go player.

https://deepmind.com/research/case-studies/alphago-the-story-so-far



## Approches to AI strategy





 Even when you can’t articulate the rules that you want the neural network to learn, you can encode your inputs in a way that emphasizes the situations you want it to pay attention to.

Early in the game, it’s difficult to evaluate a particular move because of the huge number of variations in the rest of the game. Both chess and Go AIs often use an opening book: a database of opening sequences taken from expert human games. To build this, you need a collection of game records from strong players. You analyze the game records, looking for common positions. In any common position, if a strong consensus exists about the next move—say, one or two moves account for 80% of the follow­ups—you add those moves to the opening book. The bot can then consult the book when playing a game. If any early game position appears in the opening book, the bot just looks up the expert move.

To predict how a human might move in their next turn, a bot will be used that will work against the main AI

Two areas where deep learning can be applied in a Go AI is move slection and position evaluation.
Move selection is the process of narrowing down the moves in a board position.
Position Evaluation is how a bot will know who is winning, how he is winning, and how much of a lead.

Try building a bot that is playing agaisnt another bot.


### FROM https://www.quora.com/Why-is-Go-board-game-so-difficult-for-AI-programs-to-master  STRATEGIES FOR AI ARE 









**As a fun fact, in a training or evaluation structure where 2 bots are playing against each other, their is a total of 4 AI you count the auxillary bots that help each one in move selection**



## Tree Search Algorythms
A commmon way for humans to play the game is first to consider the possible moves for our next turn , then think about how our oppponent might respond, then plan according to that. We look at the variation as far as we are able to, then back track to look for a different variation. I personally asssign semi-abstract values for each decision chain of me and my opponents so that I dont half to rethink of whether a certain decision path is worth exploring more or not. I might be able to empliment this strategy into the AI.

We are only human can think of only a certain moves ahead in certain decision chains depending on how many variations are possible in each step in the chain, and of course the mental capabilites of the human. Computer are able to greatly outperform humans in this computational environment...

https://www.cs.cmu.edu/~adamchik/15-121/lectures/Game%20Trees/Game%20Trees.html
The "branching factor" is the number of possible moves available on a given turn. 
The "solution depth" is the length of the shortest path from the initial node to a goal node.


Some brute force searches are breadth-first search, depth-first search, and depth first iterative-deepening

Minimax: Trying to maximize your points while minimizing your oppenents points

Heuristic Search: When searching the entire tree is not reasonable then instead of searching all paths, we look at the paths that seem to get closer to the desired state or goal.

https://www.cs.cmu.edu/~adamchik/15-121/lectures/Game%20Trees/Game%20Trees.html

##
The only hard-coded strategy in the Go Ai is that a group of stones with two "eyes" cant be captured. The rest is inferred by machine learning

Dead stones are stones whihc have no chance of making two eyes or connecting to friendly stones. They are treated the same as captures.
## Bot Collection
### Naive
The only hard-coded strategy in the Go Ai is that a group of stones with two "eyes" cant be captured. The rest is inferred by machine learning

Dead stones are stones whihc have no chance of making two eyes or connecting to friendly stones. They are treated the same as captures.
### Alpha Beta



# Deployment

# Technologies Used
Python
    Numpy
    enum
    random
    time
Environments
    Jupyter Notebook
    Visual Studio Code

# Concepts Explored
Decision Trees
    Tree traversal
        In-order(LNR)
    Min-Max Algorithm
    Pruning
        Depth Limited
        Alpha-Beta
        Depth Limited + Alpha Beta
    Object-Oriented Methodoly of Game Trees
        States
        Recursion
    







# Online Resources
http://online-go.com
http://gokgs.com
www.tygembaduk.com

https://en.wikipedia.org/wiki/Tree_traversal
https://www.clear.rice.edu/comp212/07-spring/lectures/39/

https://www.wikihow.com/Score-a-Game-of-Go

https://machinelearningmastery.com/how-to-score-probability-predictions-in-python/



https://senseis.xmp.net







# Repo
https://github.com/maxpumperla/deep_learning_and_the_game_of_go
https://mng.bz/gYPe
give credit: https://github.com/mattiadg/BoardGames