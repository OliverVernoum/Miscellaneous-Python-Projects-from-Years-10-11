file = open ("shakespearequotes.txt", "w") #Opens the file in read mode

for i in range(4):
    player = input("Enter the name of Player {}: ".format(i+1) )
    file.write(player + "\n")
    

file.close() #Closes the file

