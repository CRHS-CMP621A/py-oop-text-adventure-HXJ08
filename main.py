from room import room
from items import Items

kitchen = room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = room("Dining Hall")
dining_hall.set_description("A large room with ornate golden decorations on each wall.")

ballroom = room("Ballroom")
ballroom.set_description("A vast room with a shiny wooden floor. Huge candlesticks guard the entrance.")

knife = Items("Knife", "A sharp looking knife, it looks like it has been used recently.")
knife.set_location("Kitchen")
controller = Items("Controller", "A game controller, it looks like it has been used recently.")
controller.set_location("Dining Hall")
ball = Items("Ball", "A small ball, it looks like it has been used recently.")
ball.set_location("Ballroom")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

current_room = kitchen          

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)
