import pygame, sys, os
from sprites import *
pygame.init()
background = (50,65,194)
WIDTH = 600
HEIGHT = 600
CROSS_COLOR = (0,0,84)
CIRCLE_COLOR = (1,40,144)
FPS=60
x_turn = True
mode=0
data={}
pos =(0,0)
POSS_POS = [(50, 50), (250, 50), (450, 50), (50, 250), (250, 250), (450, 250), (50, 450), (250, 450), (450, 450)]
WINS = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
ICON = './assests/doge.jpg'
programIcon = pygame.image.load(ICON)
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(programIcon)
pygame.display.set_caption("CROSS AND NAUGHTS")

class win_checker():
    def __init__(self, list_inp):
        occur_x = []
        occur_o = []
        self.o_occur = occur_o
        self.x_occur = occur_x
        self.list = list_inp
        self.len_inp = len(list_inp)

    def run_checker(self):
        winner = ""
        type_win = []
        for elems_inp in self.list.keys():
            if self.list[elems_inp] == "O":
                self.o_occur.append(elems_inp)
            if self.list[elems_inp] == "X":
                self.x_occur.append(elems_inp)

        if len(self.o_occur)>=3:
            for elem in WINS:
                if all(x in self.x_occur for x in elem):
                    winner = "X"
                    type_win = elem
                    
        if len(self.o_occur)>=3:
            for elem in WINS:
                if all(x in self.o_occur for x in elem):
                    winner = "O"
                    type_win = elem
        
        if len(self.list)>=9:
            winner="tie"
            
        return winner

def draw_board(color:tuple, WIDTH_LINE):
    pygame.draw.line(window, color, (0, 200), (600, 200), WIDTH_LINE)
    pygame.draw.line(window, color, (0, 400), (600, 400), WIDTH_LINE)
    pygame.draw.line(window, color, (200, 0), (200, 600), WIDTH_LINE)
    pygame.draw.line(window, color, (400, 0), (400, 600), WIDTH_LINE)
    
def fill_window():
    data={}
    window.fill(background)
    draw_board((21,32,166), 5)

def show_menu():
    window.fill(background)   
    menu_start = menu_item(200, 400, 250, 50, 10, (0,0,255), "bold", 32, (0,255,0))
    text_rect = menu_start.draw(window, "MULTIPLAYER") 
    return text_rect

def game_manager():
    collide_box_data = []
    collision_box = [(0,0,200,200), (205, 0 ,195, 200), (405, 0, 195, 200), (0, 205, 200, 195), (205, 205, 195, 195), (405, 205, 195, 195), (0, 405, 200, 205), (205, 405, 195, 195), (405, 405, 195, 195)]
    for elem_colide_box in collision_box:
        s = pygame.Surface((elem_colide_box[2], elem_colide_box[3]))
        s.set_alpha(0)
        s.fill((255, 255, 255))
        window.blit(s ,(elem_colide_box[0], elem_colide_box[1]))
        rect = s.get_rect()
        rect.topleft=(elem_colide_box[0], elem_colide_box[1])
        collide_box_data.append(rect)
    return collide_box_data

def data_filler(data, windowd):
    for elems in data.keys():
        if data[elems] == "X":
            cross_d = cross(POSS_POS[elems][0], POSS_POS[elems][1], 100, 100, 10 , CROSS_COLOR)
            cross_d.draw(windowd)
        elif data[elems] == "O":
            circle_d = circle(POSS_POS[elems][0], POSS_POS[elems][1], 100, 10, CIRCLE_COLOR)
            circle_d.draw(windowd)
    pygame.display.update()

def show_winner(winner):
    window.fill((53,130,194))
    font = pygame.font.SysFont(pygame.font.get_fonts()[1], 64)
    if winner!="tie":
        fon_op = font.render(f"{winner} won!!", True, (4,57,105))
    else:
        fon_op = font.render("Match Tie!!", True, (4,57,105))
    font_rect = fon_op.get_rect()
    font_rect.topleft = (150, 250)
    window.blit(fon_op, font_rect)
    pygame.display.update()

def main_loop():
    global data
    data={}
    checker = win_checker(data)
    x_turn = True
    mode = 1
    global pos
    clock = pygame.time.Clock()
    while True:
        data_filler(data, window)
        winner = checker.run_checker()
        if mode==1:
            fill_window()
        elif mode==2:
            show_winner(winner)
            data={}
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if mode==1:
                    box_data = game_manager()
                    for rect in range(len(box_data)):
                        rect_op = box_data[rect]
                        if rect_op.collidepoint(pos):
                            if rect not in data:
                                data[rect] = "X" if x_turn else "O"
                                x_turn = not x_turn
                    
            #Handle Winners
            if winner=="O" or winner=="X":
                mode=2
            elif len(data)==9:
                mode=2

if __name__ == "__main__":
    main_loop()