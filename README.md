# Title: Model Study on "WeChat Lucky Money" with Monte Carlo Simulation

## Team Member(s): Yixin Zhou, Tongyang Yan, Weihao Li.

# Monte Carlo Simulation Scenario & Purpose:
Every year on New Year's Eve in China, accompanied by the festive atmosphere of the New Year, the enthusiasm of the public to send and receive "WeChat Red Envelops" also reached a climax.

According to statistics, on the eve of 2014, the total number of WeChat red envelops received and dispatched was 16 million; In 2015, it exceeded 1 billion on New Year's Eve; 8.08 million on 2016 New Year‘s Eve and 13.2 billion on 2017 New Year’s Eve.
In a WeChat group, one person send a certain amount of red envelope. Then the red envelope is divided into a certain number of small red envelopes. The amount of money in each small red envelope is randomly determined, and other member of the group can grab a small red envelope each time and receive the lucky money.

Our group's purpose is to implement Monte Carlo Simulation for the model of "Wechat lucky money relay" game. The rules of the game are: people who receive the highest amount of red envelopes in this round will need to issue red envelopes in the next round. Different relay methods and game environments will have different influences on the wealth distribution situation of the members in the group. There is an indicator that can reflect the result of the “red packet relay” in the group, that is, the gap between rich and poor. We will use Gini coefficient to represent the income distribution in a WeChat group.

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?
1. The amount of money in a red envelope.
Range:0 ~ n
Probability distribution: Normal distribution.
I think the normal distribution is the best distribution for The amount of money in a red envelope, but we can modify it to be more realistic. For instance, in fact the maximum of a red envelope in wechat is 200 RMB.

2. The n small red envelopes a red envelope can be divided into.
Range: 1 ~ the number of people particapated the game.
Probability distribution: Uniform distribution.
I think uniform distribution is not a good representation of reality because in fact many people like to divide one red envelope into multiple of 5 such as 5, 10, 20. Therefore the probability of these number will be larger than other numbers like 6, 7, 8, 9, 11, etc.  

3. The amount of money in each small envelope.
Range:0 ~ n 
Probability distribution: Dirichlet distribution.
I think this distribution is most fitted to this variable because it enpower a weight to each small envelope and seems like to be more realistic.

## Hypothesis or hypotheses before running the simulation:
1. We assume that simulated data can effectively reflect the actual situation and can be used to study the model.
2. We assume that there are certain number of people in a WeChat group.
3. At the beginning, each person has an equal amount of money. 
4. Once a people has no money in his/her pocket, he/she will quit the game and can no longer send and receive red envelop.
5. One game ends after 100 times of relays.
6. We play the game for 100 times.
7. We estimate the gini coefficient will be around 0.5.


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)
We first designed the scenario about Wechat Lucky Money. Based on the results of simulation we found the probability of gini coefficient located in 0.3-0.4 interval is the largest.

## Instructions on how to use the program:
We need to garantee the data file(.csv) and the program(.py) to exist in the same directory. Then just run the program, the program will return the probability of the value of Gini coefficient in several intervals.

## All Sources Used:
numpy.random
Walter Gautschi. Numerical Analysis [M] . New York: Bi rkhäuser rkhäuser , 2012 . 101 -110110
Gini Coefficient[E].http://en.wikipedia.org/wiki/Gini_coefficient /. 2015 -5-10
