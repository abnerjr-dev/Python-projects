""" #extracting the colors from the sample painting
import colorgram

colors = colorgram.extract(
    "intermediate/Hirst_painting_dots/image_painting_dots.jpg", 38
)  # returns named Tuples

rgb_colors = []


for c in colors:
    rgb_tuple = c.rgb[0:3]
    rgb_colors.append(rgb_tuple)

print(rgb_colors)
"""
import turtle as t
import random as r

josias = t.Turtle()
screen = t.Screen()
josias.shape("turtle")
josias.color("magenta", "green")
josias.speed("fastest")
screen.colormode(255)

screen.canvheight = 600
screen.canvwidth = 800

color_list = [
    (198, 13, 32),
    (248, 236, 25),
    (40, 76, 188),
    (244, 247, 253),
    (39, 216, 69),
    (238, 227, 5),
    (227, 159, 49),
    (29, 40, 154),
    (212, 76, 15),
    (17, 153, 17),
    (241, 36, 161),
    (195, 16, 12),
    (223, 21, 120),
    (68, 10, 31),
    (61, 15, 8),
    (223, 141, 206),
    (11, 97, 62),
    (219, 159, 11),
    (54, 209, 229),
    (19, 21, 49),
    (238, 157, 216),
    (79, 74, 212),
    (10, 228, 238),
    (73, 212, 168),
    (93, 233, 198),
    (65, 231, 239),
    (217, 88, 51),
    (6, 68, 42),
    (176, 176, 233),
    (239, 168, 161),
    (249, 8, 48),
    (5, 246, 222),
    (15, 76, 110),
    (243, 15, 14),
    (38, 43, 221),
]

josias.ht()

josias.teleport(-450, -350)

for h in range(-350, 351, 30):
    josias.teleport(-450, h)
    for l in range(-450, 451, 30):
        josias.dot(30, r.choice(color_list))
        josias.teleport(x=l)


screen.exitonclick()
