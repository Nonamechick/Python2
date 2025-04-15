class ObjectCreator(object):
    pass
my_object = ObjectCreator()
print(my_object)

class Snake:
    name = "python"
    def change_name(self, new_name): 
        self.name = new_name
snake = Snake()
print(snake.name)