import grid


print("battle ship is the name")
print(" want to play, 'y' or 'n' ")


choice = True
while choice == True: 
    YesOrNo = input("> ")
    
    if YesOrNo == 'y':
        choice = False
        EnterShip()
        
    else if YesOrNo == 'n':
        choice = False
        EndGame()
        
    else:
        choice = True
        
        
        
def EnterShip():
    print("good choice friend")
    print("i am going to be your guide")
    print("""
    
    you are in ship a play
    there is a thick foag that sperates you from your opponent
    lucky for you, on senver was able to map out the area that your enemy is in
    it is shown to as a grid 
    on the a x-axis '0' to '9'
    on the y-axis 'A' to 'J'
    +---+---+--+--+--+--+--+--+--+--+
    
    
    """)
    input(">>> ")
    
    print("choose your locations")
    
    print("the omly thing is that you can only choose cordinates with either one set of numbers or one set of alphabets in your cordiantes")
    
    print("and withen those cordinates the none constant (alphabets or numbers) will increase or decrease in order")
    
    print("also you enter cordinates that are more than or less then the given cordinate systems")
    
    print("Example: input>>> a1, a2, a3, a4, a5 ") 
    input(">> ")
    print("lastly you have omly five enteries")
    input(">>> ")
    
    player_grid = GameGrid()
    Player_statis_grid = GameGrid()
    AI_grid = GameGrid()
    
    Enter_CommandCenter()
    
def Enter_CommandCenter():
    
    print("enter you cordnates")
    
    for i in range(0, 5):
        try:
            playerx = ord(input("enter x: "))
            playery = ord(input("enter y: "))
        
            player_grid.place_point(playerx, playery)
        except ValueError:
            Enter_CommandCenter():
        
    
    Enter_Batlle()
    
def AI_Enter_Battle(c):
    



    ss = randint(0, 1)
     
    if ss == 0: 
         num_x = randint(0, 9)
         num_y = randint(0, 5)
     
         for i in range(0,5):
             num_y+=1
        
             AI.place_point(num_x, num_y)
     else:
         num_y = randint(0,9)
         num_x = randint(0, 4)
     
         for i in range(0,5):
             num_x+=1
        
             AI_grid.place_point(num_x, num_y)
             
    c = False 
     return c 
       

def Enter_Battle():
    c = True
    while ( c == True):
        
        c = AI_Enter_Battle(c)
    
