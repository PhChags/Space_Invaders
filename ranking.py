from PPlay.window import *
from PPlay.gameimage import *

def ranking():
    janela = Window(500,700);
    janela.set_title("Space Lovers - Ranking");
    background = GameImage("Assets/bk.jpg");
    btn = GameImage("Assets/return.png");
    btn.set_position(180, 625);
    
    mouse = Window.get_mouse();
    click = 0;

    while True:
        background.draw();
        text = f"RANKING";
        janela.draw_text(text, janela.width/2 - len(text) * 23, 20, size = 100, color = (255,250,250), font_name="Computer_says_no");

        btn.draw();

        click += janela.delta_time();

        if mouse.is_button_pressed(1) and click > 1:
            click = 0;
            if mouse.is_over_object(btn):
                return 0;

        with open("ranking.txt", "r") as r:
            players = r.readlines();
            size = len(players);
            if size > 10: size = 10;

            for p in range(size):
                players[p] = players[p].split(" - ");
                players[p][1] = int(players[p][1][:-1]);
            
            players = sorted(players, key=lambda player: player[1], reverse=True);
            for p in range(size):
                janela.draw_text(f"{p+1}. {players[p][0]} - {players[p][1]}", 130, 100+60*p, size=40, color=(240,240,240), font_name="Computer_says_no");
            
        janela.update();