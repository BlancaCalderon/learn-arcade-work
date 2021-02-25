"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.SAE)

# Get ready to draw
arcade.start_render()

#Draw a circle(sun)
arcade.draw_circle_filled(400,500, 100,[255, 191, 0],- 1)

#draw the grass(rectangle)
arcade.draw_lrtb_rectangle_filled(0, 800, 150, 0, arcade.color.AVOCADO)

#draw ellipse(lake)
arcade.draw_ellipse_filled(500,100,300, 50, [13, 152, 186],0,-1)

#draw a ellipse(rocks)
arcade.draw_ellipse_filled(670,100,30, 10, [143, 151, 121],0,-1)
arcade.draw_ellipse_filled(550,70,30, 10, [143, 151, 121],0,-1)
arcade.draw_ellipse_filled(500,40,30, 10, [143, 151, 121],0,-1)


#Draw a square(tree)
arcade.draw_rectangle_filled(150,200, 15,100, [210, 105, 30],0)
arcade.draw_rectangle_filled(300,100, 30,200, [210, 105, 30],0)
arcade.draw_rectangle_filled(600,150, 20,175, [210, 105, 30],0)
arcade.draw_rectangle_filled(20,0, 50,500, [210, 105, 30],0)
arcade.draw_rectangle_filled(700,200, 15,100, [210, 105, 30],0)
arcade.draw_rectangle_filled(450,190, 10,80, [210, 105, 30],0)


#draw line(birds)
arcade.create_line(200,400, 170, 470, [179, 27, 27], 1)

#draw circle(tree leaves)
arcade.draw_circle_filled(150,290, 40,[159, 169, 31],- 1)
arcade.draw_circle_filled(300,200, 70,[159, 169, 31],- 1)
arcade.draw_circle_filled(600,250, 60,[159, 169, 31],- 1)
arcade.draw_circle_filled(700,290, 40,[159, 169, 31],- 1)
arcade.draw_circle_filled(450,230, 30,[159, 169, 31],- 1)
arcade.draw_circle_filled(0,250, 100,[159, 169, 31],- 1)

arcade.draw_ellipse_filled(250,470,200,30,[155, 221, 255],0,-1)
arcade.draw_ellipse_filled(550,400,150,30,[155,221,255],0,-1)
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()