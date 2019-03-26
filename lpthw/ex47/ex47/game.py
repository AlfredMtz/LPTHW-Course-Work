class Room(object):
    # Class attributes/ passed parameters
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
    # Get value from key given
    def go(self, direction):
        return self.paths.get(direction, None)
    # Update/add new key-values to diccionaries
    def add_paths(self, paths):
        self.paths.update(paths) 

    