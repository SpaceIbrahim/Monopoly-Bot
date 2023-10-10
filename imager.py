from PIL import Image
import numpy as np

jail =(50,1300)

positions = [(1350,1350), (1180,1350), (1050,1350), (920,1350), (800, 1350), (680,1350), (560,1350), (440, 1350), (320,1350), (200,1350), 
    (10,1350),
    (10,1180), (10,1050), (10,920), (10,800), (10,680), (10,560), (10,440), (10,320), (10,200), 
    (10,10),
    (200,10), (320,10), (440,10), (560,10), (680,10), (800,10), (920,10), (1050,10), (1180,10),
    (1350,10), (1350,200), (1350,320), (1350,440), (1350,560), (1350,680), (1350,800), (1350,920), (1350,1050), (1350,1180)
]

class Imager:
    def __init__(self, num_players, names, symbols) -> None:
        
        peng = Image.open('images/penguin.webp', 'r')
        peng = peng.resize((120,120))
        pe = np.array(peng)
        redp = np.all(pe==[0,0,0,0], axis=-1)

        unicorn = Image.open('images/unicorn.png', 'r')
        unicorn = unicorn.resize((180,180))
        uni = np.array(unicorn)
        redu = np.all(uni==[0,0,0,0], axis=-1)

        robot = Image.open('images/robot.png', 'r')
        robot = robot.resize((120,120))
        ro = np.array(robot)
        redr = np.all(ro==[0,0,0,0], axis=-1)

        alien = Image.open('images/alien.jpg', 'r')
        alien = alien.resize((120,120))
        al = np.array(alien)
        reda = np.all(al==[255,255,255], axis=-1)


        # for i in range(num_players):
        #     self.players
        # Convert reds back into PIL Image to use as alpha mask
        pen_alpha = Image.fromarray(~redp)
        uni_alpha = Image.fromarray(~redu)
        rob_alpha = Image.fromarray(~redr)
        trex_alpha = Image.fromarray(~reda)

        # Paste "rm" over "formation" with alpha as transparency mask

        background = Image.open('images/monopoly.jpg', 'r')


        background.paste(peng, positions[0], pen_alpha)
        background.paste(unicorn, positions[4], uni_alpha)
        background.paste(robot, positions[8], rob_alpha)
        background.paste(alien, positions[18], trex_alpha)

        # background.show()
        # background.save('out.png')
    
    def creatBoard(self, symbols, pos):
        for i in range(len(symbols)):
            self.createPlayer(symbols[i], pos[i])

# imager = Imager(3, [], [])
