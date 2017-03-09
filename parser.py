from display import *
from matrix import *
from draw import *

def parse_file( fname, points, transform, screen, color ):
    script = open(fname, "r")
    prompt = script.readline()
    while (len(prompt)>0):
        if(prompt=="line\n"):
            prompt = script.readline()
            prompt = prompt.split() 
            add_edge(points, int(prompt[0]), int(prompt[1]), int(prompt[2]), \
                     int(prompt[3]), int(prompt[4]), int(prompt[5]))
        elif(prompt== "ident\n"):
            ident(transform)
        elif(prompt=="scale\n"):
            prompt = script.readline()
            prompt = prompt.split()
            scale = make_scale(int(prompt[0]), int(prompt[1]), int(prompt[2]))
            matrix_mult(scale, transform)
        elif(prompt=="move\n"):
            prompt = script.readline()
            prompt = prompt.split()
            trans = make_translate(int(prompt[0]),int(prompt[1]),int(prompt[2]))
            matrix_mult(trans, transform)
        elif(prompt=="rotate\n"):
            prompt = script.readline()
            prompt = prompt.split()
            if (prompt[0]=="x"):
                rotX = make_rotX(int(prompt[1]))
                matrix_mult(rotX, transform)
            if (prompt[0]=="y"):
                rotY = make_rotY(int(prompt[1]))
                matrix_mult(rotY, transform)
            if (prompt[0]=="z"):
                rotZ = make_rotZ(int(prompt[1]))
                matrix_mult(rotZ, transform)
        elif(prompt=="apply\n"):
            matrix_mult(transform, points)
            int_matrix(points)
        elif(prompt=="display\n"):
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
        elif(prompt=="save\n"):
            prompt = script.readline()
            prompt = prompt.split()
            save_extension(screen, prompt[0])
        prompt = script.readline()
