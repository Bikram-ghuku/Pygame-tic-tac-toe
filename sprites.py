import pygame

green = (0, 255, 0)
blue = (0, 0, 128)
# class line():
#     def __init__(self, x, y, length, width, color):
#         self.x = x
#         self.y = y
#         self.length = length
#         self.width = width
#         self.color = color

#     def draw(self, window, border=None):
#         if border:
#             pygame.draw.rect(window, border,(self.x-2, self.y-2, self.width+4, self.length+4), 0)
#         pygame.draw.rect(window, self.color,(self.x, self.y, self.width, self.length), 0)

class circle():
    def __init__(self, x, y, height, line_width, color:tuple):
        self.x = x
        self.y = y
        self.height = height
        self.line_width = line_width
        self.color = color

    def draw(self, window, border=None):
        pygame.draw.circle(window, self.color, (self.x+(self.height//2), self.y+(self.height//2)), self.height//2)
        pygame.draw.circle(window, (50,65,194), (self.x+(self.height//2), self.y+(self.height//2)), (self.height//2)-(self.line_width))


class cross():
    def __init__(self, x, y, height, width, line_width, color:tuple):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.line_width = line_width
        self.color = color
    
    def draw(self, window, border=None):
        pygame.draw.line(window, self.color, (self.x, self.y), (self.x+self.width, self.y+self.width), self.line_width)
        pygame.draw.line(window, self.color, (self.x+self.width, self.y), (self.x, self.y+self.width), self.line_width)


class menu_item():
    def __init__(self, x, y, width, height, border, color, type_font, size, font_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.border = border
        self.color = color
        self.font_color = font_color
        if type_font.lower()=="bold":
            font = pygame.font.Font("freesansbold.ttf", size)
        elif type_font.lower()=="italic":
            font = pygame.font.Font("./assests/fonts/Roboto-Italic.ttf", size)
        elif type_font.lower()=="italicbold" or type_font.lower()=="bolditallic":
            font = pygame.font.Font("./assests/fonts/Roboto-BoldItalic.ttf", size)
        elif type_font.lower()=="black":
            font = pygame.font.Font("./assests/fonts/Roboto-Black.ttf", size)
        self.font = font
        

    def draw(self, window, text):
        if self.border:
            pygame.draw.rect(window, self.color, (self.x-2, self.y-2, self.width+4, self.height+4))
        rect_op = pygame.draw.ellipse(window, self.color, (self.x, self.y, self.width, self.height))
        text = self.font.render(text, True, self.font_color, self.color)
        text_rect = text.get_rect()
        text_rect.center = (self.x+(self.width//2), self.y+(self.height//2))
        window.blit(text, text_rect)
        return rect_op