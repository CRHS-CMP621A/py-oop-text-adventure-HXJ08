items = {

}

class Items():
    def __init__ (self, item, descrtiption):
        self.name = item
        self.description = descrtiption
    def get_name(self):
        return self.name
    def get_description(self):  
        return self.description
    
    def set_name(self, item):
        self.name = item
    def set_description(self, description):
        self.description = description

    def set_location(self, location):
        items[self.name] = location