# ADVANCED ***************************************************************************
# content = assignment
#
# date    = 2022-01-07
# email   = contact@alexanderrichtertd.com
#************************************************************************************

"""
CUBE CLASS

1. CREATE an abstract class "Cube" with the functions:
   translate(x, y, z), rotate(x, y, z), scale(x, y, z) and color(R, G, B)
   All functions store and print out the data in the cube (translate, rotate, scale and color).

2. ADD an __init__(name) and create 3 cube objects.

3. ADD the function print_status() which prints all the variables nicely formatted.

4. ADD the function update_transform(ttype, value).
   "ttype" can be "translate", "rotate" and "scale" while "value" is a list of 3 floats.
   This function should trigger either the translate, rotate or scale function.

   BONUS: Can you do it without using ifs?

5. CREATE a parent class "Object" which has a name, translate, rotate and scale.
   Use Object as the parent for your Cube class.
   Update the Cube class to not repeat the content of Object.

"""

class Cube:
   def __init__(self, name):
        self.name = name
        self.x = 1
        self.y = 1
        self.z = 1
        self.r = 255
        self.g = 255
        self.b = 255

        print("Initiating Cube Object name '{}':\nx = {}, y = {}, z = {}\nr = {}, g = {}, b = {}\n".format(self.name, self.x, self.y, self.z, self.r, self.g, self.b))

   
   def translate(self, x, y, z):
        ''' Fake calculation for translating xyz
        '''
        self.x += x
        self.y += y
        self.z += z

        print("Translating Cube object named '{}' by x = {}, y = {}, z = {}.".format(self.name, x, y, z))
        print("New data for Cube object '{}': x = {}, y = {}, z = {}.".format(self.name, self.x, self.y, self.z))
   
   
   def rotate(self, x, y, z):
        ''' Fake calculation for rotating xyz
        '''
        self.x += x
        self.y += y
        self.z += z

        print("Rotating Cube object named '{}' by x = {}, y = {}, z = {}.".format(self.name, x, y, z))
        print("New data for Cube object '{}': x = {}, y = {}, z = {}.".format(self.name, self.x, self.y, self.z))
   
   
   def scale(self, x, y, z):
        ''' Fake calculation for scaling xyz
        '''
        self.x *= x
        self.y *= y
        self.z *= z

        print("Scaling Cube object named '{}' by x = {}, y = {}, z = {}.".format(self.name, x, y, z))
        print("New data for Cube object '{}': x = {}, y = {}, z = {}.".format(self.name, self.x, self.y, self.z))
    
   def color(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

        print("Changing color on Cube object named '{}' to r = {}, g = {}, b = {}.".format(self.name, r, g, b))
        
   
   def print_status(self):
        print("The variables of the Cube object named '{}' are the followings:".format(self.name))
        print("Position:\n\tx = {}\n\ty = {}\n\tz = {}".format(self.x, self.y, self.z))
        print("RGB color:\n\tr = {}\n\tg = {}\n\tb = {}\n".format(self.r, self.g, self.b))
   

   def update_transform(self, ttype, value=[0, 0, 0]):
        move_types = ['translate', 'rotate', 'scale']
        if ttype in move_types: eval("self.{}({}, {}, {})".format(ttype, value[0], value[1], value[2]))


    

#################################################################################################################
## EXECUTION ##

cube1 = Cube(name="Cube Object 01")
cube2 = Cube(name="Cube Object 02")
cube3 = Cube(name="Cube Object 03")

cube1.update_transform(ttype="translate", value=[2, 2, 2])
cube1.print_status()

cube2.update_transform(ttype="rotate", value=[3, 1, 2])
cube2.print_status()

cube3.update_transform(ttype="scale", value=[1, 2, 1])
cube3.print_status()



