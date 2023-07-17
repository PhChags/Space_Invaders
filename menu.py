from PPlay.window import *
from PPlay.gameimage import *
from PPlay.mouse import *

#funcao seta posicao botoes
def set_vetor(v,j):
    y = j.height/24;
    for i in v:
        i.set_position(j.width/2 - i.width/2, j.height/2 + y);
        y += i.height + 20;

#funcao ddesenha botoes
def draw_buttons(b):
    for i in b:
        i.draw();

#funcao menu
def menu():
    #inicializacoes
    screen = Window(500,700);
    screen.set_title("Space Invaders");
    mouse = Window.get_mouse();
    background = GameImage("Assets/background.jpg");
    buttons = [GameImage("Assets/play.png"), GameImage("Assets/levels.png"),GameImage("Assets/ranking.png"), GameImage("Assets/leave.png")];
    set_vetor(buttons,screen);
    click = 0;

#game loop
    while True:

        click += screen.delta_time();

        if mouse.is_button_pressed(1) and click > 2:
            click = 0;
            if mouse.is_over_object(buttons[0]):
                return 1;
            if mouse.is_over_object(buttons[1]):
                return 2;
            if mouse.is_over_object(buttons[2]):
                return 3;
            if mouse.is_over_object(buttons[3]):
                exit();

        background.draw();
        draw_buttons(buttons);
        screen.update();
