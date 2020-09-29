songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0])
print(songs[2])
print(songs[1:3])
songs[2] = "Sweater Weather"
songs.append("Star Shopping")
songs.extend("Lil Kennedy")
songs.insert(0,"I hate My Mom")
songs.remove("ROCKSTAR")
for song in songs:
    print(song)

animals = ["Cat", "Dog", "Bird"]
animals.append("Cow")
print(animals[2])
del animals[0]
for i in range(len(animals)):
    print(animals[i])