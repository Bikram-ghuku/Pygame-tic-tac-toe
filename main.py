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
        for elems_inp in range(self.len_inp):
            if self.list[elems_inp] == "O":
                self.o_occur.append(elems_inp)
            if self.list[elems_inp] == "X":
                self.x_occur.append(elems_inp)

        if len(self.o_occur)>=3:
            for elem in WINS:
                if all(x in self.x_occur for x in elem):
                    self.winner = "X"
                    
        if len(self.o_occur)>=3:
            for elem in WINS:
                if all(x in self.o_occur for x in elem):
                    self.winner = "O"

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
    try:
        for elems in data.keys():
            if data[elems] == "X" and elems<=8:
                cross_d = cross(POSS_POS[elems][0], POSS_POS[elems][1], 100, 100, 10 , CROSS_COLOR)
                cross_d.draw(window)
            elif data[elems] == "O" and elems<=8:
                circle_d = circle(POSS_POS[elems][0], POSS_POS[elems][1], 100, 10, CIRCLE_COLOR)
                circle_d.draw(window)
    except Exception:
        pass
    return collide_box_data


def main_loop():
    x_turn = True
    global mode
    mode = 0
    data[9]={}
    global pos
    clock = pygame.time.Clock()
    while True:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
             

        print(data)
        fill_window()
        box_data = game_manager()
        for rect in range(len(box_data)):
            rect_op = box_data[rect]
            if rect_op.collidepoint(pos):
                if rect not in data:
                    data[rect] = "X" if x_turn else "O"
                    x_turn = not x_turn                
        pygame.display.update()

if __name__ == "__main__":
    main_loop()