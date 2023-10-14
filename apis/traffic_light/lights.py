class colors:
    def __init__(self, color):
        self.color = color

    def change_light(self):
        if self.color == 'red':
            self.color = 'green'
        elif self.color == 'green':
            self.color = 'yellow'
        else:
            self.color = 'red'


