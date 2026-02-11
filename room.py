import items
class room():
    def __init__(self,room_name):
        self.name = room_name
        self.description = None
        self.link_rooms = {}
    def set_description(self, room_description):
        self.description = room_description
    
    def get_description(self):
        return self.description
    
    def get_name(self):
        return (self.name)

    def set_name(self, room_name):
        self.name = room_name

    def describe(self):
        print(self.description)

    def link_room(self, room_to_link, direction):
        self.link_rooms[direction] = room_to_link
        print( self.name + " linked rooms :" + repr(self.link_rooms) )

    def get_details(self):
        print(self.name)
        self.describe()
        for direction in self.link_rooms:
            room = self.link_rooms[direction]
            print( "The " + room.get_name() + " is " + direction)
        for item in items.items:
            if items.items[item] == self.name:
                print("You see a " + item)
        

    def move(self, direction):
        if direction in self.link_rooms:
            return self.link_rooms[direction]
        else:
            print("You can't go that way")
            return self