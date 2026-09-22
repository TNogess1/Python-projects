# Tyrese Nogess
# NBA Player Stats Program
# This program calculates a player's points per game and gives a simple description of their performance.

print("================================")
print("       NBA PLAYER STATS")
print("================================")

Player = input("Enter the player's name: ")

Games = int(input("Enter games played: "))
Points = float(input("Enter total points: "))
Rebounds = float(input("Enter total rebounds: "))
Assists = float(input("Enter total assists: "))

PointsPerGame = Points / Games
ReboundsPerGame = Rebounds / Games
AssistsPerGame = Assists / Games

print()
print("Player:", Player)
print("-------------------------------")
print("Points Per Game:", PointsPerGame)
print("Rebounds Per Game:", ReboundsPerGame)
print("Assists Per Game:", AssistsPerGame)

print()
print("Player Performance")
print("-------------------------------")

if PointsPerGame >= 25:
    print("Scoring: Elite")

elif PointsPerGame >= 20:
    print("Scoring: Very Good")

elif PointsPerGame >= 15:
    print("Scoring: Good")

else:
    print("Scoring: Developing")

if ReboundsPerGame >= 10:
    print("Rebounding: Excellent")

elif ReboundsPerGame >= 7:
    print("Rebounding: Good")

else:
    print("Rebounding: Developing")

if AssistsPerGame >= 8:
    print("Playmaking: Excellent")

elif AssistsPerGame >= 5:
    print("Playmaking: Good")

else:
    print("Playmaking: Developing")

print("-------------------------------")
print("NBA Stats Program Complete!")
