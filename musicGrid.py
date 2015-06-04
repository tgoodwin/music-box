"""
The Music Grid: A Vague Impression of the Key of A minor
Tim Goodwin
May 2013

All audio samples are copyrighted by Tim Goodwin - timg.goodwin@gmail.com.
"""

import pygame, sys, os, pygame.mixer, pygame.time

pygame.mixer.init(4100,8,1,2048) #sample rate=4100Khz, resolution=8bits, channels=1(mono), buffer rate = 2048

def drawGrid(board,game,size):
    game.fill((50,50,50)) #background color of window
    
    for i in range(0,16):
        for j in range(0,16):
            if board[i][j]:
                game.fill((150,150,150), pygame.Rect((i*20),(j*20),20,20)) #fill selected square
    
    for i in range(0,16): #drawing lines between squares
        pygame.draw.line(game,(60,60,60),((i * (size / 16),0)), ((i * (size / 16)),size))
        pygame.draw.line(game,(60,60,60),(0,(i * (size / 16))), (size ,(i * (size / 16))))
    pygame.display.flip() #update window
    pygame.display.set_caption("Music Grid in A minor", "Music Grid")
    
    
def musicGrid():

    """This part prepares the note samples by stating their locations and how they will be routed through the mixer channels"""
    
    a = os.path.join('samples','0c.wav') #the paths for mixer to locate audio files
    b = os.path.join('samples','1b.wav')
    c = os.path.join('samples','2a.wav')
    d = os.path.join('samples','3g.wav')
    e = os.path.join('samples','4f.wav')
    f = os.path.join('samples','5e.wav')
    g = os.path.join('samples','6d.wav')
    h = os.path.join('samples','7c.wav')
    i = os.path.join('samples','8b1.wav')
    j = os.path.join('samples','9a2.wav')
    k = os.path.join('samples','10g2.wav')
    l = os.path.join('samples','11f2.wav')
    m = os.path.join('samples','12e2.wav')
    n = os.path.join('samples','13d2.wav')
    o = os.path.join('samples','14c2.wav')
    p = os.path.join('samples','15b3.wav')
   
    aa = pygame.mixer.Sound(a) #commands to play each sound
    bb = pygame.mixer.Sound(b)
    cc = pygame.mixer.Sound(c)
    dd = pygame.mixer.Sound(d)
    ee = pygame.mixer.Sound(e)
    ff = pygame.mixer.Sound(f)
    gg = pygame.mixer.Sound(g)
    hh = pygame.mixer.Sound(h)
    ii = pygame.mixer.Sound(i)
    jj = pygame.mixer.Sound(j)
    kk = pygame.mixer.Sound(k)
    ll = pygame.mixer.Sound(l)
    mm = pygame.mixer.Sound(m)
    nn = pygame.mixer.Sound(n)
    oo = pygame.mixer.Sound(o)
    pp = pygame.mixer.Sound(p)
  
    aaa = pygame.mixer.Channel(0) #assigning a mixer channel to each sound command
    bbb = pygame.mixer.Channel(1)
    ccc = pygame.mixer.Channel(2)
    ddd = pygame.mixer.Channel(3)
    eee = pygame.mixer.Channel(4)
    fff = pygame.mixer.Channel(5)
    ggg = pygame.mixer.Channel(6)
    hhh = pygame.mixer.Channel(7)
    iii = pygame.mixer.Channel(0)
    jjj = pygame.mixer.Channel(1)
    kkk = pygame.mixer.Channel(2)
    lll = pygame.mixer.Channel(3)
    mmm = pygame.mixer.Channel(4)
    nnn = pygame.mixer.Channel(5)
    ooo = pygame.mixer.Channel(6)
    ppp = pygame.mixer.Channel(7)

#---------------------------------------------------------------------

    pygame.init()
    size = 320
    game = pygame.display.set_mode((size,size))
    
    
    board = [] #sets up what will be the x-y arrangement of selected squares
    for i in range(0,16):
        board.append([])
        for j in range(0,16):
            board[i].append(False) #sets note squares as initially unselected
    
    addingNotes = True
    while addingNotes:
        drawGrid(board,game,size) #create grid
        for event in pygame.event.get():
            if event.type==pygame.QUIT: #OK to use exit button in top left
                pygame.display.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
            
                mousePosition = pygame.mouse.get_pos()
                x = mousePosition[0] #separate mousePosition value into x&y
                y = mousePosition[1]
                x = int(x/20)
                y = int(y/20) #gets index by dividing by square width(pixels)
                board[x][y] = not board[x][y]
            elif event.type == pygame.KEYDOWN:
                print "Now playing arrangement. Press any key to clear the Grid: "
                addingNotes = False
                play = False
    makingNoise= True
    while makingNoise: #playbackloop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit(i)
        for i in range(0,16):
            for j in range(0,16):
                pygame.time.delay(10) #delays (10ms) iteration through each column to give space between notes during playback
                if board[i][j]:
                    hue = 40
                    game.fill((100,100,240),pygame.Rect((i*20),(j*20),20,20)) 
                    
                    pygame.display.flip()
                    if j==0: aaa.play(aa)
                    if j==2: bbb.play(bb)
                    if j==3: ccc.play(cc)
                    if j==4: ddd.play(dd)
                    if j==5: eee.play(ee)
                    if j==6: fff.play(ff)
                    if j==7: ggg.play(gg)
                    if j==8: hhh.play(hh)
                    if j==9: iii.play(ii)
                    if j==10: jjj.play(jj)
                    if j==11: kkk.play(kk)
                    if j==12: lll.play(ll)
                    if j==13: mmm.play(mm)
                    if j==14: nnn.play(nn)
                    if j==15: ooo.play(oo)
                    if j==16: ppp.play(pp)
                   
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                print "Grid refreshed."
                makingNoise = False
                play = True
                
def main():
    print ""
    print "The Music Grid creates ambient sound based on an x-y arrangement \n of user selected notes."
    print "Use mouse to select squares, then press any key to begin: "
    play = True
    while play:
        musicGrid()
    
if __name__ == '__main__':
    main()
