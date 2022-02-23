#
# import another_module
# print(another_module.another_variable)
#
# # import turtle
# # timmy = turtle.Turtle()
#
# from turtle import Turtle, Screen
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")    #timmy의 모양을 turtle로 변경
# timmy.color("Orange")
#
# my_screen = Screen()
# print(my_screen.canvheight)
# timmy.forward(100)
# my_screen.exitonclick()

from prettytable import PrettyTable    # import class 'PrettyTable' from module 'prettytable'
table = PrettyTable()    # crate an object 'table' from class 'PrettyTable()'

table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander"])
table.add_column("Type",["Eletric","Water","Fire"])
print(table)
print(table.align)

table.align ="r"
print(table)
print(table.align)





