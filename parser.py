from display import *
from matrix import *
from draw import *

"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing
See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    script = open(fname, 'r')
    line_list = script.readlines()
    num_lines = len(line_list)
    current = 0

    while current < num_lines-1:
        line = line_list[current]
        if current + 1 != num_lines:
            next_row = line_list[current+1]
        #line
        if line == 'line\n':
            points_list = next_row.split()
            add_edge(points, int(points_list[0]), int(points_list[1]), int(points_list[2]), int(points_list[3]), int(points_list[4]), int(points_list[5]))
        #ident
        elif line == 'ident\n':
            ident(transform)
        #scale
        elif line == 'scale\n':
            scale = next_row.split()
            scales = make_scale(int(scale[0]), int(scale[1]), int(scale[2]))
            matrix_mult(scales, transform)
        #translate
        elif line == 'move\n':
            translation = next_row.split()
            matrix_mult(make_translate(int(translation[0]), int(translation[1]), int(translation[2])), transform)
        #rotate
        elif line == 'rotate\n':
            theta = next_row.split()
            var, rot = theta[0], float(theta[1])
            if var == 'x':
                rotate = make_rotX(rot)
            elif var == 'y':
                rotate = make_rotY(rot)
            elif var == 'z':
                rotate = make_rotZ(rot)
            matrix_mult(rotate, transform)
        #apply
        elif line == 'apply\n':
            matrix_mult(transform, points)
        #display
        elif line == 'display\n':
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        #save
        elif line == 'save\n':
            file_name = next_row.strip()
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, file_name)
        #quit
        elif line == 'quit\n':
            break
        current += 1
    script.close()
