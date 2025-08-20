# Q11. Ask number of games played in a tournament. Ask the user number of games won and number of games loss. Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)

total_tournament = int(input("Enter total number of tounamnent="))
game_won = int(input("Enter a win count="))
game_loss = int(input("Enter a loss count="))
tie = total_tournament-game_won-game_loss
print("Number of tie", tie)
Total_points = (game_won*4)+(tie*2)
print("Total Points in the tournament=", Total_points)
