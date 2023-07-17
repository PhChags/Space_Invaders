from PPlay.window import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.keyboard import *
from enemys import *
from winner import winner_screen
from game_over import gameover
import random

def moveMatriz(array, position):

    for line in array:
        for alien in line:
            alien.move_x(position), alien.move_y(10);

def game(level, points=0):
    # DIFICULDADE
    if level == 1: a = 0.8
    elif level == 2: a = 1
    else: a = 1.2
    
    screen = Window(500,700)
    screen.set_title("Space Invaders");
    background = GameImage("Assets/bk.jpg");
    
    ship = Sprite("Assets/ship.png", 1);
    all_shoots = [];
    cooldown = 0;
    speedShoot = -0.45/a;
    speedShip = 250/a;
    lives = 3;

    ship.set_position(screen.width/2 - ship.width/2, screen.height - ship.height);

    keyboard = Window.get_keyboard();

    all_enemys = cria_enemy();
    all_enemys_shoots = [];
    cooldown_enemy = 0;
    enemySpeed = a*0.5;

    start = screen.time_elapsed();
    time=2;
    cont=0;
    fps=0;
    atual=0;
    invulneravelTime=0;
    
    while True:
        background.draw();

        #FPS
        time += screen.delta_time();
        cont += screen.delta_time();
        cooldown_enemy += screen.delta_time();
        fps += 1;
        if cont>1:
            atual=fps;
            cont=0;
            fps=0;

        #CONTROLES
        if keyboard.key_pressed("ESC"):
            return 0;
            
        if keyboard.key_pressed("LEFT"):
            if ship.x > 0:
                ship.move_x(-speedShip * screen.delta_time());
            else:
                ship.set_position(screen.width - ship.width, screen.height - ship.height);
                ship.move_x(speedShip * screen.delta_time());
        if keyboard.key_pressed("RIGHT"):
            if ship.x < screen.width - ship.width:
                ship.move_x(speedShip * screen.delta_time());
            else:
                ship.set_position(0, screen.height - ship.height);
                ship.move_x(-speedShip * screen.delta_time());
        if keyboard.key_pressed("SPACE") and cooldown <= 0:
            shoot = Sprite("Assets/laser.png", 1);
            shoot.set_position(ship.x + ship.width/2 - shoot.width/2, ship.y - shoot.height);
            all_shoots.append(shoot);
            cooldown = 0.3 * a;
            

        #COOLDOWN
        cooldown += speedShoot * screen.delta_time();

        #COLISOES
        for shoot in all_shoots:
            if shoot.y > 0:
                shoot.move_y(speedShoot);

                if not all_enemys[-1]:
                    all_enemys.pop(-1);
                if not all_enemys: 
                    end = screen.time_elapsed();
                    points += (end-start)/1000;
                    level = winner_screen(level, points);
                    if level != 0:
                        game(level, points);
                    else:
                        return level;

                collided = False;
                if all_enemys[-1][0].y + all_enemys[-1][0].height >= shoot.y:
                    all_enemys, collided = collision(shoot, all_enemys);

                if not collided:
                    shoot.draw();
                else:
                    points += 25*level;
                    all_shoots.pop(all_shoots.index(shoot));
            else:
                all_shoots.pop(all_shoots.index(shoot));

        #DRAWS
        #TIROS PLAYER
        for shoot in all_shoots:
            shoot.move_y(speedShoot);
            if shoot.y + shoot.height < 0:
                del all_shoots[all_shoots.index(shoot)];
            shoot.draw();
        
        #TIROS ENEMYS
        for tiro in all_enemys_shoots:
            tiro.move_y(-speedShoot);
            if tiro.y < 0 or (tiro.collided(ship) and screen.time_elapsed() - invulneravelTime>2000):
                if tiro.collided(ship):
                    ship.x = (screen.width - ship.width)/2;
                    lives -= 1;
                    invulneravelTime = screen.time_elapsed();
                del all_enemys_shoots[all_enemys_shoots.index(tiro)];
            tiro.draw();
        
        #INIMIGOS
        for line in all_enemys:
            if line:

                # ALTERANDO ROTA AO ATINGIR LATERAIS
                if line[0].x < 0 or line[-1].x >= screen.width-line[-1].width:
                    enemySpeed *= -1;
                    moveMatriz(all_enemys, enemySpeed);
                
                # SETANDO ENEMY SHOOTS
                if cooldown_enemy > randint(1, 3//level):
                    cooldown_enemy = 0;
                    all_enemys_shoots = enemy_shoot(all_enemys, all_enemys_shoots);

                for monster in line:
                    if monster.y+monster.height >= screen.height - ship.height * 1.2 or lives == 0: 
                        end = screen.time_elapsed();
                        points += (end-start)/1000;
                        return gameover(points);
                        
                    monster.move_x(enemySpeed);
                    monster.draw();
            else:
                all_enemys.pop(all_enemys.index(line));
        
        if screen.time_elapsed() - invulneravelTime < 2000 and ship.drawable:
            ship.hide();
        else:
            ship.unhide();
        
        # GAMEOVER // WINNER
        if lives == 0: 
            end = screen.time_elapsed();
            points += (end-start)/1000;
            return gameover(points);
        elif not all_enemys:
            end = screen.time_elapsed();
            points += (end-start)/1000;
            level = winner_screen(level, points);
            if level != 0:
                game(level, points);
            else:
                return level;


        screen.draw_text(f"FPS: {atual}",0,5, size = 20, color = (255,255,255));
        screen.draw_text(f"Lives: {lives}",screen.width/2,5, size = 20, color = (255,255,255));

        ship.draw();
        screen.update();
