from PPlay.window import *
from PPlay.gameimage import *
from save_name import name
from math import trunc


def winner_screen(level, points):
    janela = Window(500,700);
    janela.set_title("Space Invaders");
    fundo = GameImage("Assets/bk.jpg");
    color = (0,0,188);
    text = "YOU WIN";
    score_text = f"Score: {trunc(points)}";

    buttons = [GameImage("Assets/next.png"), GameImage("Assets/menu.png"), GameImage("Assets/leave.png")];
    save = GameImage("Assets/save.png");

    if level == 3: 
        buttons.pop(0);
        buttons.append(save);

    for b in range(len(buttons)):  
        buttons[b].set_position(180, 500+70*b);

    mouse = Window.get_mouse();
    click = 0;

    while True:
        fundo.draw();
        janela.draw_text(text,janela.width/2- len(text) * 25 , 20, size = 100, color = color);
        janela.draw_text(score_text,janela.width/2 - (len(score_text)-1) * 8, 150, size = 40, color = (255,255,255));

        click += janela.delta_time();

        for b in buttons:
            b.draw();

        if mouse.is_button_pressed(1) and click > 1:
            click = 0;
            if level != 3:
                if mouse.is_over_object(buttons[0]):
                    return level+1;
                if mouse.is_over_object(buttons[1]):
                    return 0;
                if mouse.is_over_object(buttons[2]):
                    exit();
            else:
                if mouse.is_over_object(buttons[0]):
                    return 0;
                if mouse.is_over_object(buttons[1]):
                    exit();
                if mouse.is_over_object(buttons[2]):
                    name(points, janela); 
                    return 0;

        janela.update();