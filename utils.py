from pydoc import importfile
import sys
from textwrap import wrap

import time
        


a = 1.5
b = 0.2
c = 0.04
d = 0.09
e = 0.005

#print, print, delay function
def dprint_del():
    print("\n\n")
    print()
    time.sleep(a)


#sprawling text function
def sprawl_txt(x):
    for charecters in x:
        sys.stdout.write(charecters)
        sys.stdout.flush()
        time.sleep(c)

#three lines - 3 description
def three_lines(x,y,z):
    dprint_del()
    print(x)
    dprint_del()
    print(y)
    dprint_del()
    print(z)

#three lines - description, dialogue, description
def threelines__desdiades(x,y,z):
    dprint_del()
    print(x)
    dprint_del()
    line = y
    sprawl_txt(y)
    dprint_del()
    print()
    print(z)

#four lines - description, dialogue, dialouge, dialogue
def four_lines_1des3dia(x,y,z,a):
    dprint_del()
    print(x)
    dprint_del()
    line = y
    sprawl_txt(y)
    print()
    dprint_del()
    line = z 
    sprawl_txt(z)
    print()
    dprint_del()
    line = a 
    sprawl_txt(a)

#non response
def non_response():
    print("The man doesn't seem to understand you're question, return again")

#four lines: dialogue, description, description, dialogue
def fourlines_2des2dia(x,y,z,a):
    dprint_del()
    line = x
    sprawl_txt(x)
    print()
    dprint_del()
    print(y)
    dprint_del()
    print(z) 
    dprint_del()
    line = a 
    sprawl_txt(a)
    print()

    
#dialogue, dialogue, description
def threelines_1des2dia(x,y,z):
    dprint_del()
    line = x
    sprawl_txt(x)
    print()
    dprint_del()
    line = y
    sprawl_txt(y)
    print()
    dprint_del()
    print(z) 
    
#quick info - description, description
def twolines(x,y):
    dprint_del()
    line = x 
    sprawl_txt(x)
    print()
    dprint_del()
    line = y 
    sprawl_txt(y)
    print()
    

#info dump - dialogue 8x
def infodump_dia8(a,b,c,d,e,f,g,h):
    dprint_del()
    line = a 
    sprawl_txt(a)
    print()
    dprint_del()
    line = b 
    sprawl_txt(b)
    print()
    dprint_del()
    line = c 
    sprawl_txt(c)
    print()
    dprint_del()
    line = d 
    sprawl_txt(d)
    print()
    dprint_del()
    line = e 
    sprawl_txt(e)
    print()
    dprint_del()
    line = f 
    sprawl_txt(f)
    print()
    dprint_del()
    line = g
    sprawl_txt(g)
    print()
    dprint_del()
    line = h 
    sprawl_txt(h)
    print()
    
#three lines: description, description, dialogue
def threelines_2des1dia(x,y,z):
    dprint_del()
    print(x)
    dprint_del()
    print(y)
    dprint_del()
    line = z
    sprawl_txt(z)
    print()
    

#four lines: dialogue, description, description, description
def fourlines_3des1dia(a,b,c,d):
    dprint_del()
    line = a 
    sprawl_txt(a)
    print()
    dprint_del()
    print(b)
    dprint_del()
    print(c)
    dprint_del()
    print(d)


# actiondump_6des2dia(a,b,c,d,e,f,g,h)
    
def actiondump_6des2dia(a,b,c,d,e,f,g,h):   
    dprint_del()
    line = a 
    sprawl_txt(a)
    print() 
    dprint_del()
    print(b) 
    dprint_del()
    print(c) 
    dprint_del()
    print(d) 
    dprint_del()
    line = e 
    sprawl_txt(e)
    print()  
    dprint_del()
    print(f)  
    dprint_del()
    print(g)
    dprint_del()
    print(h)
    
# def game_over():
#     print("GAME OVER!")
#     dprint_del()
#     print("Returning to where it all began...")
#     question_hub_intro()

# four lines all dialogue
def fourlines_4dia(a,b,c,d):
    dprint_del()
    line = a
    sprawl_txt(a)
    print()
    dprint_del()
    line = b
    sprawl_txt(b)
    print()
    dprint_del()
    line = c
    sprawl_txt(c)
    print()
    dprint_del()
    line = d
    sprawl_txt(d)
    print()

  