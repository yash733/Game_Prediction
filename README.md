#### This was a very fun project, took a bit of time to covercome the troubles. 

#### Data set link - https://www.kaggle.com/datasets/ashishjangra27/pubg-games-dataset

## <font color='Orange'>⚠️ To be noted</font></br>
- Found there is some issue with the model, throwing wage results at random out of blue. WORKING ON IT
- UN-able to deploy over streamlit server due to package version clash. UNABLE TO RESOLVE
- <font color='green'>Working fine on local system</font>

## Setup.py
Use Setup.py to create a venv and instalation of required libraries Automatically. In order to create a venv with custom NAME and python version opne the file and pass value as you desired.</br>
- By defauly virtual environment name "venv" and available python version will chooses.


### <font color="Tan">Data Description</font><a class = 'anchor' id = 'desc'></a>
- <b>DBNOs -</b> Number of enemy players knocked.
- <b>assists -</b> Number of enemy players this player damaged that were killed by teammates.
- <b>boosts -</b> Number of boost items used.
- <b>damageDealt -</b> Total damage dealt. Note: Self inflicted damage is subtracted.
- <b>headshotKills -</b> Number of enemy players killed with headshots.
- <b>heals -</b> Number of healing items used.
- <b>Id -</b> Player’s Id.
- <b>killPlace -</b> Ranking in match of number of enemy players killed.
- <b>killPoints -</b> Kills-based external ranking of player. (Think of this as an Elo ranking where only kills matter.) If there is a value other than -1 in rankPoints, then any 0 in killPoints should be treated as a “None”.
- <b>killStreaks -</b> Max number of enemy players killed in a short amount of time.
- <b>kills -</b> Number of enemy players killed.
- <b>longestKill -</b> Longest distance between player and player killed at time of death. This may be misleading, as downing a player and driving away may lead to a large longestKill stat.
- <b>matchDuration -</b> Duration of match in seconds.
- <b>matchId -</b> ID to identify match. There are no matches that are in both the training and testing set.
- <b>matchType -</b> String identifying the game mode that the data comes from. The standard modes are “solo”, “duo”, “squad”, “solo-fpp”, “duo-fpp”, and “squad-fpp”; other modes are from events or custom matches.
- <b>rankPoints -</b> Elo-like ranking of player. This ranking is inconsistent and is being deprecated in the API’s next version, so use with caution. Value of -1 takes place of “None”.
- <b>revives -</b> Number of times this player revived teammates.
- <b>rideDistance -</b> Total distance traveled in vehicles measured in meters.
- <b>roadKills -</b> Number of kills while in a vehicle.
- <b>swimDistance -</b> Total distance traveled by swimming measured in meters.
- <b>teamKills -</b> Number of times this player killed a teammate.
- <b>vehicleDestroys -</b> Number of vehicles destroyed.
- <b>walkDistance -</b> Total distance traveled on foot measured in meters.
- <b>weaponsAcquired -</b> Number of weapons picked up.
- <b>winPoints -</b> Win-based external ranking of player. (Think of this as an Elo ranking where only winning matters.) If there is a value other than -1 in rankPoints, then any 0 in winPoints should be treated as a “None”.
- <b>groupId -</b> ID to identify a group within a match. If the same group of players plays in different matches, they will have a different groupId each time.
- <b>numGroups -</b> Number of groups we have data for in the match.
- <b>maxPlace -</b> Worst placement we have data for in the match. This may not match with numGroups, as sometimes the data skips over placements.
- <b>winPlacePerc -</b> The target of prediction. This is a percentile winning placement, where 1 corresponds to 1st place, and 0 corresponds to last place in the match. It is calculated off of maxPlace, not numGroups, so it is possible to have missing chunks in a match.


![image](https://github.com/user-attachments/assets/4b7db4b7-f6ce-4bd7-8895-d2d7e0069176)

![image](https://github.com/user-attachments/assets/408516a7-c2d5-4f60-803d-098fdd52b7a9)

![image](https://github.com/user-attachments/assets/379535ea-4b96-4a79-ac92-38dd20dcdc29)

![image](https://github.com/user-attachments/assets/3049fd03-375b-40a8-98b2-1993f35857e2)

![image](https://github.com/user-attachments/assets/b901c5cf-c73e-4d6f-9425-fb2adbec485b)
