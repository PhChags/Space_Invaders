from PPlay.window import *
from PPlay.gameimage import *
from save_name import name
from math import trunc

def gameover(points=0):
    janela = Window(500,700);
    janela.set_title("Space Invaders");
    screen = GameImage("Assets/bk.jpg");
    color = (188,0,0);
    text = "YOU LOSE";
    score_text = f"Score: {trunc(points)}";

    buttons = [GameImage("Assets/save.png"), GameImage("Assets/return.png"), GameImage("Assets/menu.png"), GameImage("Assets/leave.png")];

    for b in range(4):  
        buttons[b].set_position(180, 450+60*b);

    mouse = Window.get_mouse();

    while True:
        screen.draw();
        janela.draw_text(text,janela.width/2- len(text) * 25 , 20, size = 100, color = color);
        janela.draw_text(score_text,janela.width/2 - (len(score_text)-1) * 8, 150, size = 40, color = (255,255,255));
        
        for b in buttons:
            b.draw();

        if mouse.is_button_pressed(1):
            if mouse.is_over_object(buttons[0]):
                name(points, janela);
                return 0;
            if mouse.is_over_object(buttons[1]):
                return 1;
            if mouse.is_over_object(buttons[2]):
                return 0;
            if mouse.is_over_object(buttons[3]):
                exit();

        janela.update();