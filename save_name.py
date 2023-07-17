from PPlay.window import *
from PPlay.gameimage import *
from PPlay.keyboard import *
from math import trunc

def name(points, janela):
    background = GameImage('Assets/bk.jpg');

    key = Window.get_keyboard();
    string = [];
    a = ["_", "_", "_"];
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'];
    b = 0;
    c = 0;
    ct = 0;
    cc = 0;

    while True:
        background.draw();
        janela.draw_text("Digite o seu Nome", 100, 20, size = 50, color = (240,240,240), font_name="Computer_says_no");
        
        for i in range(3):
                if (key.key_pressed("UP") and ct == 0):
                    ct += 1;
                    if c == 26:
                        c = 0;
                    a[b] = alfabeto[c]
                    c = c + 1;

                if (key.key_pressed("DOWN") and ct == 0):
                    ct += 1;
                    c = c - 1;
                    if c == -1:
                        c = 25;
                    a[b] = alfabeto[c];

                if (key.key_pressed("ENTER") and cc == 0 and a[b] != "_"):
                    cc += 1;
                    c = 0;
                    b += 1;

                if ct != 0:
                    ct += 1;
                    if ct == 100:
                        ct = 0;

                if cc != 0:
                    cc += 1;
                    if cc == 100:
                        cc = 0;
                janela.draw_text(a[i], janela.width / 2 - 90 + 70 * i + 1, janela.height/2, size=100, color=(255, 255, 255));

        if b == 3:
            string.append(a[0] + a[1] + a[2]);
            break;
        janela.update();

 
    with open("ranking.txt", "a") as n:
        newString = ' '.join(string);
        newString += f"  -  {trunc(points)}\n";
        n.write(newString);
    