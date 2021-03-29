fav_games = ["Doom", "Golden Axe", "The Settlers"]

print(fav_games[0])

for game in fav_games:
  print(game)

fav_games.append("Monster Hunter World")

print(len(fav_games))

print(fav_games[3])

fav_games.insert(0, "Mario 64")

del(fav_games[2])

print(fav_games)