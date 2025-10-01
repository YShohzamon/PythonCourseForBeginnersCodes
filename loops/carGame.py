game_over = True
game_help = "help"
game_start = "start"
game_stop = "stop"
game_quit  = "quit"
started = False

while game_over:
    action = input(">")

    if action.lower() == game_help :
        print("start - to start the car!")
        print("stop - stop to stop the car!")
        print("quit - to exit the game!")
        print("Car are already on help menu")
    elif action.lower() == game_start :
        if started:
            print("Car already started!")
        else:
            started = True
            print("Car started ... Ready to go!")
    elif action.lower() == game_stop :
        if not started:
            print("Car already stopped!")
        else:
            started = False
            print("Car stopped!")
    elif action.lower() == "quit" :
        game_over = False
    else:
        print("I don't understand that ...")