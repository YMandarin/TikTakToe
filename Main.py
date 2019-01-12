import pygame

size = 200
alter = int(size * 0.2)

pygame.init()
pygame.display.set_caption("TikTakToe")
canvas = pygame.display.set_mode((size, size + alter))
clock = pygame.time.Clock()

blockSize = int(size / 3)

Ways = {
    (0, 0): [[(1, 0), (2, 0)], [(0, 1), (0, 2)], [(1, 1), (2, 2)]],
    (1, 0): [[(0, 0), (2, 0)], [(1, 1), (1, 2)]],
    (2, 0): [[(0, 0), (1, 0)], [(2, 1), (2, 2)], [(1, 1), (0, 2)]],
    (0, 1): [[(1, 1), (1, 2)], [(0, 0), (0, 2)]],
    (1, 1): [[(0, 0), (2, 2)], [(2, 0), (0, 2)], [(1, 0), (1, 2)], [(0, 1), (2, 1)]],
    (2, 1): [[(0, 1), (1, 1)], [(2, 0), (2, 2)]],
    (0, 2): [[(0, 0), (0, 1)], [(1, 2), (2, 2)], [(1, 1), (2, 0)]],
    (1, 2): [[(0, 2), (2, 2)], [(1, 0), (1, 1)]],
    (2, 2): [[(2, 0), (2, 1)], [(0, 2), (1, 2)], [(0, 0), (1, 1)]],
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
            pygame.draw.circle(canvas, (0, 0, 0),
                               (self.x * blockSize + int(blockSize / 2), self.y * blockSize + int(blockSize / 2),),
                               int(blockSize / 2))
        else:
            pygame.draw.rect(canvas, (0, 0, 0), (self.x * blockSize, self.y * blockSize, blockSize, blockSize))


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
run = True


def draw():
    canvas.fill((255, 255, 255))
    pygame.draw.rect(canvas, (200, 200, 200), (0, size, size, alter))

    width = int(alter * 0.4)
    if Type == 1:
        pygame.draw.circle(canvas, (0, 0, 0), (int(size * 0.8) - width//2, size + int(alter / 2) - width), int(width/2))
    else:
        pygame.draw.rect(canvas, (0, 0, 0), (int(size * 0.8) - width//2, size + int(alter / 2) - width,width,width))

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
            if not isinstance( Map[mouse[0]][mouse[1]],Block):
                Map[mouse[0]][mouse[1]] = Block(Type, mouse[0], mouse[1])

                if check(mouse[0], mouse[1], Type):
                    won = True

                if Type == 0:
                    Type = 1
                else:
                    Type = 0

    draw()


pygame.quit()
