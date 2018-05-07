# Title: Model Study on "WeChat Lucky Money" with Monte Carlo Simulation

## Team Member(s): Yixin Zhou, Tongyang Yan, Weihao Li.

# Monte Carlo Simulation Scenario & Purpose:
Every year on New Year's Eve in China, accompanied by the festive atmosphere of the New Year, the enthusiasm of the public to send and receive "WeChat Red Envelops" also reached a climax.
According to statistics, on the eve of 2014, the total number of WeChat red envelops received and dispatched was 16 million; In 2015, it exceeded 1 billion on New Year's Eve; 8.08 million on 2016 New Year‘s Eve and 13.2 billion on 2017 New Year’s Eve.
In a WeChat group, one person send a certain amount of red envelope. Then the red envelope is divided into a certain number of small red envelopes. The amount of money in each small red envelope is randomly determined, and other member of the group can grab a small red envelope each time and receive the lucky money.
Our group's purpose is to implement Monte Carlo Simulation for the model of "Wechat lucky money relay" game. The rules of the game are: people who receive the highest amount of red envelopes in this round will need to issue red envelopes in the next round. Different relay methods and game environments will have different influences on the wealth distribution situation of the members in the group. There is an indicator that can reflect the result of the “red packet relay” in the group, that is, the gap between rich and poor. We will use Gini coefficient to represent the income distribution in a WeChat group.

## Simulation's variables of uncertainty
List and describe your simulation's variables of uncertainty (where you're using pseudo-random number generation). For each such variable, how did you decide the range and probability distribution to use?  Do you think it's a good representation of reality?
1. Total amount of red envelope
2. The packets number of Each envelope.
3. The number of group member
4. The initial amount of each person.

## Hypothesis or hypotheses before running the simulation:
1. We assume that there are certain number of people in a WeChat group.
2. At the beginning, each person has an equal amount of money. 
3. Once a people has no money in his/her pocket, he/she will quit the game and can no longer send and receive red envelop.
4. One game ends after 100 times of relays.
5. We play the game for 100 times.


## Analytical Summary of your findings: (e.g. Did you adjust the scenario based on previous simulation outcomes?  What are the management decisions one could make from your simulation's output, etc.)

## Instructions on how to use the program:

## All Sources Used:

