from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.collision import *
from random import randint


# Cria matriz de enemys
def cria_enemy():
    enemys = [];

    for i in range(5):
        line = [];
        for j in range(6):
            if i%2: #and j%2:
                blackenemy = Sprite("Assets/blackmonster.png", 1);
                blackenemy.set_position(blackenemy.width*1.5*j, blackenemy.height*1.5*i);
                line.append(blackenemy);  
            elif i == 2:
                whiteenemy = Sprite("Assets/whitemonster.png", 1);
                whiteenemy.set_position(whiteenemy.width*1.5*j, whiteenemy.height*1.5*i);
                line.append(whiteenemy); 
            else:
                grayenemy = Sprite("Assets/graymonster.png", 1);
                grayenemy.set_position(grayenemy.width*1.5*j, grayenemy.height*1.5*i);
                line.append(grayenemy);
        
        enemys.append(line);

    return enemys;

# Colisão dos tiros do player com os enemys
def collision(shoot, array):
    collided = False;

    for i in range(len(array)-1, -1, -1):
        line = array[i];
        if line:
            for enemy in line:
                if shoot.y <= enemy.y+72:
                    if Collision.collided(enemy, shoot):
                        line.pop(line.index(enemy));
                        collided = True;

    return array, collided;

# Colisão dos tiros dos monstros com o player
def lose(array, shoot, spaceship, lives):
    loser = False;

    if shoot.y + shoot.height >= spaceship.y:
        if spaceship.x < shoot.x < spaceship.x+spaceship.width or spaceship.x < shoot.x+15 < spaceship.x+spaceship.width:
            array.pop(array.index(shoot));
            lives -= 1;
            loser = True;
    return array, loser, lives;

# Cria lista de tiros enemys
def enemy_shoot(array, all_enemy_shoots):
    while True:
        linha = randint(0,len(array)-1);
        if len(array[linha]) > 0:
            try:
                coluna = randint(0,len(array[linha])-1);
            except:
                coluna = 0;
            break;

    h = Sprite("Assets/enemylaser.png", 1);
    h.set_position(array[linha][coluna].x, array[linha][coluna].y+array[linha][coluna].height), all_enemy_shoots.append(h);

    return all_enemy_shoots;