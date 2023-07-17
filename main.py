from PPlay.window import *
from menu import menu
from game import game
from dificuldade import dificuldade
from ranking import ranking

#inicializacoes 
screen = Window(500,700);
screen.set_title("Space Invaders");

STATE = 0;

#game loop
while True:
    if STATE == 0:
        STATE = menu();
    if STATE == 1:
        STATE = game(1);
    if STATE == 2:
        STATE = dificuldade(); 
    if STATE == 3:
        STATE = ranking();
    if STATE == 4:
        STATE = exit();