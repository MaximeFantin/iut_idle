import pygame

pygame.init()
screen = pygame.display.set_mode((1088, 720))
clock = pygame.time.Clock()
running = True

with open("noise", "r") as f:
    instr = f.read()
lines = instr.split("\n")
data = []
cols = []
for i in lines:
    data.append(i.split())
    for j, k in enumerate(data[-1]):
        data[-1][j] = float(k.strip())
        cols.append(data[-1][j])
maxcol = abs(max(cols, key=lambda x:(abs(x))))
mincol = abs(min(cols, key=lambda x:(abs(x))))
if data[-1] == []:
    data = data[:-1]


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(0, 0, 250))

    for x, _ in enumerate(data[0]):
        for y, _ in enumerate(data):
            col = int(((abs(data[y][x])+mincol)/maxcol)*255)
            pygame.draw.rect(screen, pygame.Color(col, col, col), pygame.Rect(x*16, y*16, 16, 16))


    pygame.display.flip()
    clock.tick(30)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(pygame.Color(0, 0, 250))

    for x, _ in enumerate(data[0]):
        for y, _ in enumerate(data):
            col = 255 if abs(data[y][x]) < 0.06 else 0
            pygame.draw.rect(screen, pygame.Color(col, col, col), pygame.Rect(x*16, y*16, 16, 16))


    pygame.display.flip()
    clock.tick(30)


pygame.quit()