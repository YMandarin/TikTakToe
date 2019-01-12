import pygame

size = 600
alter = int(size * 0.2)

pygame.init()
pygame.font.init()
pygame.display.set_caption("TikTakToe")
canvas = pygame.display.set_mode((size, size + alter))
clock = pygame.time.Clock()

blockSize = int(size / 3)

cross = pygame.image.load("Cross.png")
circle = pygame.image.load("Circle.png")

firstCross = pygame.transform.scale(cross, (blockSize, blockSize))
firstCircle = pygame.transform.scale(circle, (blockSize, blockSize))

Ways = {
    (0, 0): [[(1, 0), (2, 0)], [(0, 1), (0, 2)], [(1, 1), (2, 2)]],
    (1, 0): [[(0, 0), (2, 0)], [(1, 1), (1, 2)]],
    (2, 0): [[(0, 0), (1, 0)], [(2, 1), (2, 2)], [(1, 1), (0, 2)]],
    (0, 1): [[(1, 1), (2, 1)], [(0, 0), (0, 2)]],
    (1, 1): [[(0, 0), (2, 2)], [(2, 0), (0, 2)], [(1, 0), (1, 2)], [(0, 1), (2, 1)]],
    (2, 1): [[(0, 1), (1, 1)], [(2, 0), (2, 2)]],
    (0, 2): [[(0, 0), (0, 1)], [(1, 2), (2, 2)], [(1, 1), (2, 0)]],
    (1, 2): [[(0, 2), (2, 2)], [(1, 0), (1, 1)]],
    (2, 2): [[(2, 0), (2, 1)], [(0, 2), (1, 2)], [(0, 0), (1, 1)]],
}

Colors = {
    "Black": (0, 0, 0),
    "White": (255, 255, 255),
    "LightGray": (200, 200, 200),
    "DarkGray": (100, 100, 100)
}


def setMax(item, maxVal):
    if item > maxVal:
        item = maxVal

    return item


def setTupleMax(Tuple, maxVal1, maxVal2="Null"):
    item1 = Tuple[0]
    item2 = Tuple[1]

    if maxVal2 == "Null":
        maxVal2 = maxVal1

    if item1 > maxVal1:
        item1 = maxVal1
    if item2 > maxVal2:
        item2 = maxVal2

    Tuple = (item1, item2)

    return Tuple


class Block:

    def __init__(self, type, x, y):
        self.x = x
        self.y = y
        self.type = type

    def draw(self):
        if self.type == 1:
            canvas.blit(firstCircle, (self.x * blockSize, self.y * blockSize))
        else:
            canvas.blit(firstCross, (self.x * blockSize, self.y * blockSize))


class Text:

    def __init__(self, Text, pos, size = 50,color = Colors["Black"], Font="tahoma", bold = False, italic = False):
        self.text = Text
        self.pos = pos
        self.font = Font
        self.size = size
        self.bold = bold
        self.italic = italic
        self.color = color
        self.Font = pygame.font.SysFont(self.font, self.size, self.bold, self.italic)
        self.Text = self.Font.render(self.text, True, self.color)
        self.surface = self.Text.get_rect()



    def getSize(self):
        return self.surface

    def setText(self,Text,size = -1,color = -1,Font = -1):

        self.text = Text
        if not size == -1:
            self.size = size
        if not color == -1:
            self.color = color
        if not Font == -1:
            self.font = Font


        self.render()

    def setPos(self,pos):
        self.pos = pos
        self.render()

    def draw(self,surface = canvas):
        x = self.pos[0]
        y = self.pos[1]
        w = self.surface[0]
        h = self.surface[1]

        surface.blit(self.Text,(x - w//2,y-h//2))

    def render(self):
        self.Font = pygame.font.SysFont(self.font, self.size, self.bold, self.italic)
        self.Text = self.Font.render(self.text, True, self.color)
        self.surface = self.Text.get_rect()


Map = []

for x in range(0, 3):
    Map.append([])
    for i in range(0, 3):
        Map[x].append(0)


def check(x, y, type):
    isFinish = False
    List = Ways[(x, y)]

    for x in List:
        Finishing = True

        for i in x:
            if isinstance(Map[i[0]][i[1]], Block):
                if Map[i[0]][i[1]].type == type:
                    pass
                else:
                    Finishing = False

            else:
                Finishing = False

        if Finishing:
            isFinish = True

    return isFinish


Type = 0
won = False
reset = False

run = True

width = int(alter * 0.5)
secondCross = pygame.transform.scale(cross, (width, width))
secondCircle = pygame.transform.scale(circle, (width, width))


def draw():
    canvas.fill(Colors["White"])
    pygame.draw.rect(canvas, Colors["DarkGray"], (0, size, size, alter))

    if Type == 1:
        canvas.blit(secondCircle, (int(size * 0.85) - width // 2, size + alter // 2 - width // 2))
    else:
        canvas.blit(secondCross, (int(size * 0.85) - width // 2, size + alter // 2 - width // 2))

    for x in Map:
        for i in x:
            if isinstance(i, Block):
                i.draw()

    pygame.display.update()


while run:

    clock.tick(30)

    if won:
        pygame.time.delay(50)
        for x2 in range(0, 3):
            for i2 in range(0, 3):
                Map[x2][i2] = 0
        won = False

    elif reset:
        pygame.time.delay(50)
        for x2 in range(0, 3):
            for i2 in range(0, 3):
                Map[x2][i2] = 0
        reset = False

    e = pygame.event.get()
    for event in e:
        if event.type == pygame.QUIT:
            run = False

    mouse = pygame.mouse.get_pos()
    mouse = (int(mouse[0] / blockSize), int(mouse[1] / blockSize))

    mouse = setTupleMax(mouse, 2)

    leftcl, wheel, rightcl = pygame.mouse.get_pressed()

    for event in e:
        if event.type == pygame.QUIT:
            run = False

        if leftcl and event.type == pygame.MOUSEBUTTONDOWN:
            if not isinstance(Map[mouse[0]][mouse[1]], Block):
                Map[mouse[0]][mouse[1]] = Block(Type, mouse[0], mouse[1])

                if check(mouse[0], mouse[1], Type):
                    won = True

                if Type == 0:
                    Type = 1
                else:
                    Type = 0

                if not won:
                    reset = True
                    for x in Map:
                        for i in x:
                            if i == 0:
                                reset = False

    draw()

pygame.quit()
