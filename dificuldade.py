from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from PPlay.mouse import *
from game import game

#funcao seta posicao botoes
def set_vetor(v,j):
    y = j.height/6;
    for i in v:
        i.set_position(j.width/2 - i.width/2, j.height/2 + y);
        y += i.height + 20;

#funcao desenha botoes
def draw_difs(b):
    for i in b:
        i.draw();

#funcao tela dificuldade
def dificuldade():
    #inicializacoes
    screen = Window(500,700);
    screen.set_title("Space Invaders");
    background = GameImage("Assets/bk.jpg");

    difs = [GameImage("Assets/level1.png"), GameImage("Assets/level2.png"), GameImage("Assets/level3.png")];
    mouse = Window.get_mouse();
    teclado = Window.get_keyboard();

    click = 0;

    set_vetor(difs,screen);

    #game loop
    while True:

        click += screen.delta_time();

        if teclado.key_pressed("ESC"):
            return 0;

        if mouse.is_button_pressed(1) and click > 2:
            click = 0;
            if mouse.is_over_object(difs[0]):
                return game(1);
            if mouse.is_over_object(difs[1]):
                return game(2);
            if mouse.is_over_object(difs[2]):
                return game(3);

        background.draw();
        draw_difs(difs);
        screen.update();