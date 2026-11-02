text = "30"
filename = "highscore.txt"


def SaveError (text, filename):
    file = open(filename, "w")
    file.write(text) 
    file.close() 


    

    
