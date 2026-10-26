command = ""
started = False
while True:
    command = input("> "). lower()
    if command == "start":
     if started:
      print("car already started")
     else:
      started = True
      print("car started...")

    elif command == "stop":
        if not started:
         print("car already stopped")
        else:
         started = False 
         print("car stopped")
    
    elif command == "quit":
       break

    elif command == "help":
       print("""
 start - To start the car
 stop - To stopped the car
 quit - To quit
            
""")
    else:
     print("sorry i don't understand that")


    
