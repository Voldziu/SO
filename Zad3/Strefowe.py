import numpy as np
import pandas as pd

from Algorythm import Algorythm
from RAM import RAM
from Zad4Alg import Alg4
from Generator import *
import copy
andrzej ="""⣿⣿⣿⣿⣿⣿⣿⣿⠉⠉⠀⠀⠀⠀⠀⠀⣸⣿⣿⡟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡟⡆⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⣿⣿⢁⡀⠀⠀⠀⠀⠀⢀⣿⡿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⢃⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣿⡟⠋⠈⠀⠀⠀⠀⠀⠀⢸⣟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⢁⣾⢸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⣿⣟⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⣠⡖⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢤⣼⡟⢸⣿⢸⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⣿⡟⠉⠁⠀⠀⠀⢠⣤⣶⣶⣤⣘⣿⡴⠃⠀⠀⠀⣼⠟⠀⣠⣤⣠⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⠘⠹⢸⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⡛⢉⣁⢈⣟⠀⠀⠀⠀⢠⣟⣽⣿⣟⣿⣯⣿⣝⠰⠀⠀⠀⢿⣾⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠀⠀⣀⣤⣤⣤⣷⣾⣿⣿⣾⣧⠀⢘⣗⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣥⡄⠁⠀⠀⠀⠀⢸⣽⡏⣿⠈⣷⡉⢻⣿⠀⠀⣰⠏⠈⢡⣾⣷⣿⣿⣿⠿⣿⣿⣿⣿⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣭⣭⠛⣿⡄⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠃⠀⠀⠀⠀⠀⠚⣏⣷⡏⣠⣼⣷⢶⣿⠀⠀⢿⠀⠰⠿⠋⣛⠿⠿⡿⣖⠿⣿⣿⡏⠀⠀⠀⠈⠛⣿⣿⣿⣿⣿⣏⣿⣿⣿⡇⢿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⡿⠂⠀⠀⠀⠀⠀⠀⣿⣾⡇⣿⡿⣿⣿⡿⢺⣷⡏⠀⠀⠀⠀⠉⠉⠉⠀⠈⠀⠻⠋⠁⢠⡄⡄⠀⠀⢻⠻⠿⢯⡥⠄⠅⠙⠛⣣⢸⡟⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⣷⡿⣷⣿⣿⣇⠰⣇⢠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠶⡄⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡞⣸⠡⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣽⣿⠛⢻⣗⣿⣤⣹⡎⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⡇⡿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣾⣶⡄⠀⠀⠀⠀⠀⠀⠀⠀⠻⡿⣦⣀⣿⣿⣿⣇⣅⠀⠀⠀⠀⠀⠀⠀⠀⢀⢠⡾⠇⣀⠀⠄⣀⢀⡀⢠⠀⠀⠀⠀⠀⠀⠀⣿⢳⠁⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠉⢸⣿⣹⣿⣶⣄⡀⠀⠀⠀⠀⠀⠀⣠⣼⣯⣿⣿⣶⣶⣶⣾⣷⡄⠀⠀⠀⠀⠀⠀⣴⡿⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢈⣼⣿⣿⢿⡿⣧⡀⠀⠀⠀⠀⢠⣾⣯⣤⣿⣿⣿⣿⣯⣥⣿⡉⠀⠀⠀⠀⠀⠀⠀⣿⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣿⣿⣿⠀⠀⠄⠀⠀⠀⡀⣀⣀⠀⠀⠀⢸⣾⢻⣧⣟⢱⡿⣿⠏⠀⠀⣶⣿⣿⣿⣿⣿⣿⠿⢿⡿⣿⣿⣷⣦⣄⡀⠀⠀⢀⣼⡟⡞⠀⠀⠀⠀⠀⠀⠀⠀⠀⠐⠠⠀⠀
⣿⣿⠿⠀⠀⠀⠀⠀⠸⣿⡉⠻⣇⠀⠀⢸⣿⠀⣻⣿⡾⢷⣿⠗⢀⣼⣿⣿⣿⣯⣽⣶⣾⣷⣮⣷⣦⣽⡻⣿⣿⣷⠠⣦⣾⡿⠃⠁⠀⠑⠆⠀⠂⠀⠀⠀⠀⠀⠀⠧⡄
⣻⣟⣀⠀⠀⣀⣀⣀⡀⠈⠻⣿⣯⣤⣀⣀⣿⡀⢿⣿⣿⣿⣿⣿⣈⠈⣿⠇⠉⢻⣿⣛⠛⠻⡿⠛⠛⢛⡿⠻⠿⠟⣼⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠿⠏⢙⣷⣾⠏⠁⠈⢷⡶⡟⡇⣀⣀⠉⢩⣿⣠⢻⣿⣿⣿⣿⣿⣿⣿⣿⠤⠄⠄⣙⣿⣿⣟⣐⣾⣿⡟⠁⠀⣠⣤⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⣽⡿⡿⠏⠉⣹⠶⣆⡤⡉⡿⣿⣿⠛⣯⣻⣿⠋⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠙⣿⣿⣿⣿⠿⠟⠑⣶⣿⣿⣿⠟⡁⠀⠀⠀⠀⠐⠂⠀"""

piwo ="""⠀⠀⣰⣾⣿⣷⣶⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣷⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠙⣿⣧⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣏⠹⣷⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠈⢿⣧⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠘⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣧⡀⠙⣿⣿⣿⣿⣿⣿⣿⡇⠀⠘⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⠈⠻⣿⣿⣿⣿⡟⠀⠀⠀⢸⣷⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⡤⠴⠶⠶⠖⠒⠒⠶⣄⡀⠀⢀⣠⠶⠚⠲⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢀⣤⣾⣿⣦⡀⠈⠻⣿⣏⠀⠀⠀⠀⢸⣿⠀⠀⠀⣀⣤⠶⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠓⠛⠁⠀⠀⠀⠈⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣦⡀⠈⠛⢷⣄⡀⢀⣼⡏⢀⣴⠿⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠛⠲⣤⡀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢘⣿⣷⠈⠹⣿⣿⣿⣷⣦⣄⣉⣿⣿⣿⡾⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⡀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣴⣿⡿⠋⠀⠀⣹⣿⣿⣿⠀⠀⣿⣿⣿⠁⠀⠀⢀⣠⣤⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⢦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀
⠀⠀⠀⣠⡾⠿⢿⣿⣤⣴⣶⣿⣿⣥⣈⠙⢷⣿⣿⠛⠛⠿⠿⠿⢿⣿⣿⣿⣷⣦⣀⣀⣠⣤⣤⣴⣶⣶⣤⣤⣤⣤⣾⠿⠶⠆⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀
⠀⠀⣴⡟⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⣦⣤⣄⡀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀
⠀⣼⡏⠀⢀⣾⣿⣿⡿⠟⠛⠋⠉⠉⠛⢿⣿⣿⡇⠀⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⡆⠀⢸⣿⣷⣶⣶⡆⠀⢰⣶⣶⣶⣿⡿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⠀
⢸⡟⠀⠀⣾⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡇⢰⣿⣿⣿⠇⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠑⢄⠀
⣿⠃⠀⢰⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠁⢸⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆
⣿⠀⠀⢸⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⢸⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⡟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇
⣿⡀⠀⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡿⠀⣿⣿⣿⣿⠀⢀⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣇⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠁
⢹⡇⠀⢻⣿⣿⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠇⠀
⠸⣿⡀⠘⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⣿⣿⣿⡟⠀⢸⣿⣿⣿⣿⣿⠀⠀⣾⣿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⢸⠀⠀
⠀⢻⣧⠀⠹⣿⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⣿⠃⢸⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣧⣀⣀⣴⣾⣿⣿⣧⠀⠀⠀⠀⢸⠀⠀
⠀⠈⣿⣆⠀⠹⣿⣿⣷⡄⠀⠀⠀⠀⠀⢠⣿⠀⢸⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣧⠀⠀⣿⣿⣿⣿⣿⣿⠉⢸⣿⣿⣿⣿⠈⢧⠀⠀⠀⣾⠀⠀
⠀⠀⠘⣿⣆⠀⠘⣿⣿⣿⡄⠀⠀⠀⠀⢸⣿⠀⢸⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠸⣿⣿⣿⣿⡆⠸⣧⣄⣠⡇⠀⠀
⠀⠀⠀⠘⣿⣆⠀⠈⢿⣿⣿⣆⠀⠀⠀⢸⡏⠀⣿⣿⣿⣿⠇⠀⢸⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⡇⠀⣿⠀⠉⠀⠀⠀
⠀⠀⠀⠀⠈⢿⣧⡀⠀⢻⣿⣿⣧⠀⠀⣿⡇⠀⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡆⠀⣿⣿⣿⣿⣇⠀⣿⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠻⣷⡄⠀⠹⣿⣿⣷⣀⣿⠇⢠⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⠀⢻⡆⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠈⢿⣦⠀⠙⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢿⣿⣿⣿⣿⠀⢸⡇⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣷⡀⠸⣿⣿⣿⠀⢸⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡿⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⡆⢸⣧⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣹⡟⠀⢹⣿⡟⠀⣼⣿⣿⣿⡟⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣧⠀⢸⣿⣿⣿⣿⡇⠘⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⡿⠃⠀⣼⣿⡇⠀⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⡇⠀⣿⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣾⣿⠋⠀⠀⣴⣿⣿⡇⠀⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⣿⣿⣿⣿⠀⣿⡆⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣶⣿⣿⡿⣿⠁⢠⣿⣿⣿⣿⡇⠀⢰⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⠀⢻⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠉⠉⠀⠀⣿⠀⢸⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⡄⢸⡇⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡿⠀⢸⣿⣿⣿⣿⠃⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⣿⣿⣿⣿⣿⣿⠀⠀⣿⣿⣿⣿⣿⣿⣿⡀⠀⣿⣿⣿⣿⣿⡇⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠀⠾⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⢀⣿⣿⣿⣿⣿⣿⠀⠀⢿⣿⣿⣿⣿⣿⣿⡇⠀⣿⣿⣿⣿⣿⡇⠀⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣇⡀⠀⠀⠉⠙⠛⠀⠀⠸⠿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⣿⣿⣿⠀⠀⢸⣿⣿⣿⣿⣿⣿⡇⠀⢻⡿⠿⠛⠛⠃⠀⣿⡄⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠻⠿⣶⣶⣤⣤⣀⣀⣀⠀⠀⠀⠀⠈⠁⠀⠈⠉⠉⠉⠉⠉⠉⠀⠀⠈⠉⠉⠉⠉⠁⠀⠀⣀⣀⣀⣤⣤⣶⣶⠾⠿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠙⠛⠛⠻⠿⠿⠿⠿⠿⠶⢶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⠶⠾⠿⠿⠿⠛⠛⠛⠉⠉⠁⠀⠀⠀⠀"""
class Strefowe(Alg4):
    # szamotuly - badanie

    def __init__(self,ram:RAM,szam,MaxProcesowNaraz:int):
        super().__init__(ram,name="Strefa",szamutuly=szam,)
        self.DlugosciKwantowychList=[]
        self.MaxProcesowNaraz=MaxProcesowNaraz

        self.WolneRamki = 0


    def process(self, alg: Algorythm):
        dflist = []
        bledylist = []
        ListaBitowa = []
        Szamotuly = []

        data = self.ram.Data
        array = self.ram.Array
        ramki = self.ram.Ramki
        procesy = len(data)

        zwrotlista = [1 for i in range(len(array[:self.MaxProcesowNaraz, 0]))]
        pozostale = ramki - len(array[:self.MaxProcesowNaraz, 0])
        suma = 0
        klucze = array[:self.MaxProcesowNaraz, 1]
        for i in range(len(klucze)):
            suma += klucze[i]

        suma1 = 0
        for i in range(len(zwrotlista)):
            rozpietosc = klucze[i]
            procent = rozpietosc / suma
            przydzial = pozostale * procent
            suma1 += round(przydzial + 1)

            zwrotlista[i] = round(zwrotlista[i] + przydzial)
        sortlista = sorted(zwrotlista, reverse=True)

        # zabierz najbogatszym
        print(sortlista)
        for i in range(suma1 - ramki):
            zwrotlista[zwrotlista.index(sortlista[i])] = sortlista[i] - 1

        print(zwrotlista)

        Alglist = [copy.deepcopy(alg) for i in range(len(zwrotlista))]




        # lista algorytmow dla kazdego procesu

        SposobOdwolania=distribute_elements(self.szamotuly,len(zwrotlista))

        #zaladowanie poczatkowe
        #k - przesuniecie zeby brac kolejne procesy
        k=0
        for i in range(len(zwrotlista)):
            Alglist[i].Queue=data[i]
            Alglist[i].Ramki=zwrotlista[i]
            Alglist[i].ListaRamek=[None for x in range(Alglist[i].Ramki)]
            Alglist[i].HistoriaRamek= np.zeros(shape=(1, Alglist[i].Ramki), dtype=int)

        flag=True
        while(flag):
            print("lol")
            self.DlugosciKwantowychList=[]



            for i in range(len(zwrotlista)):
                print("status----------------------------")
                print(Alglist[i].IsShutDown)
                if(Alglist[i].Swiezak):
                    Alglist[i].Swiezak=False


                if(not Alglist[i].IsShutDown and flag):
                    for j in range(SposobOdwolania[i]): # wykonaj sie tyle razy, ile zostalo przydzielone losowo (permutacje)
                        if Alglist[i].Queue !=[]:
                            Alglist[i].process()
                        else:
                            k+=1

                            if k<= (len(data)-len(zwrotlista)):
                                self.WolneRamki+=Alglist[i].Ramki
                                df = pd.DataFrame(Alglist[i].HistoriaRamek[1:])
                                print("kkkkkkkkkkkkkkkkk----------------------------")
                                dflist.append(df)
                                bledylist.append(Alglist[i].LiczbaBledowStron)
                                ListaBitowa.append(Alglist[i].ListaBitowa)

                                Alglist[i] = copy.deepcopy(alg)
                                Alglist[i].Queue = data[len(zwrotlista)+k-1]
                                Alglist[i].Ramki = self.WolneRamki
                                self.WolneRamki=0
                                Alglist[i].ListaRamek = [None for x in range(Alglist[i].Ramki)]
                                Alglist[i].Swiezak=True
                                Alglist[i].HistoriaRamek = np.zeros(shape=(1, Alglist[i].Ramki), dtype=int)
                                break

                            else:
                                flag=False


                                for i in range(len(zwrotlista)):
                                    if(Alglist[i].Queue!=[]):
                                        flag=True
                                if(not flag):
                                    print("KONIEC")
                                    print(andrzej)
                                    for i in range(len(zwrotlista)):
                                        df = pd.DataFrame(Alglist[i].HistoriaRamek[1:])
                                        dflist.append(df)
                                        bledylist.append(Alglist[i].LiczbaBledowStron)
                                        ListaBitowa.append(Alglist[i].ListaBitowa)
                                    for i in range(len(Alglist)):
                                        print(Alglist[i].Queue)
                                    break

                dlugosc = len(set([x.position for x in Alglist[i].KwantowaLista]))
                self.DlugosciKwantowychList.append(dlugosc)
                Alglist[i].KwantowaLista=[]




            # SposobOdwolania = distribute_elements(self.szamotuly, len(zwrotlista))
            print(f'LOOOOOOOOOOOOOOOOOOOOL{self.DlugosciKwantowychList}')
            calkdlug=0
            for i in range(len(self.DlugosciKwantowychList)):
                calkdlug+=self.DlugosciKwantowychList[i]
            if(calkdlug<=self.ram.Ramki):
                for j in range(len(self.DlugosciKwantowychList)):

                    print(Alglist[j].ListaRamek)


                    if (not Alglist[j].IsShutDown and not Alglist[j].Swiezak):
                        dlugosc = self.DlugosciKwantowychList[j]



                        roznica = dlugosc-Alglist[j].Ramki
                        Alglist[j].Ramki=dlugosc
                        if(roznica>0): #WSS > liczba ramek
                            for _ in range(roznica):
                                Alglist[j].ListaRamek.append(None)
                            Alglist[j].Rozszerzenie+=roznica
                            Alglist[j].balans+=roznica
                            self.WolneRamki-=roznica

                        elif roznica<0: #WSS <liczba ramek
                            print(Alglist[j].ListaRamek)
                            print(roznica)
                            print(self.DlugosciKwantowychList[j])
                            print(Alglist[j].IsShutDown)



                            Alglist[j].ListaRamek=Alglist[j].ListaRamek[:roznica]
                            print(andrzej)
                            print(piwo)




                            Alglist[j].balans+=roznica
                            self.WolneRamki-=roznica
            else:
                while(calkdlug>self.ram.Ramki):
                    maxim = max(self.DlugosciKwantowychList)
                    print(maxim)
                    index = self.DlugosciKwantowychList.index(maxim)
                    print(self.DlugosciKwantowychList[index])
                    print(len(self.DlugosciKwantowychList))
                    print(self.DlugosciKwantowychList)
                    print(len(Alglist))
                    print(Alglist)
                    Alglist[index].IsShutDown=True
                    print("""""")


                    self.DlugosciKwantowychList[index]=0


                    self.WolneRamki+=Alglist[index].Ramki
                    stareramki=self.WolneRamki
                    for k in range(len(self.DlugosciKwantowychList)):
                        obecnadlugosc =self.DlugosciKwantowychList[k]
                        if(calkdlug!=maxim):
                            stosunek =obecnadlugosc/(calkdlug-maxim)
                            ilewiecej = int((stareramki *stosunek))
                            self.DlugosciKwantowychList[k]+=ilewiecej



                    calkdlug=calkdlug-maxim

                for j in range(len(self.DlugosciKwantowychList)):
                    if(not Alglist[j].IsShutDown):
                        dlugosc = self.DlugosciKwantowychList[j]
                        roznica = dlugosc-Alglist[j].Ramki
                        Alglist[j].Ramki=dlugosc
                        print(roznica)
                        if(roznica>0): #WSS > liczba ramek
                            for _ in range(roznica):
                                Alglist[j].ListaRamek.append(None)
                            Alglist[j].Rozszerzenie+=roznica
                            Alglist[j].balans+=roznica
                            self.WolneRamki-=roznica

                        elif roznica<0: #WSS <liczba ramek
                            Alglist[j].ListaRamek=Alglist[j].ListaRamek[:roznica]
                            Alglist[j].balans+=roznica #dodanie ujemne
                            self.WolneRamki-=roznica
            for i in range(len(zwrotlista)):
                if(self.WolneRamki>Alglist[i].Ramki and Alglist[i].IsShutDown):
                    Alglist[i].IsShutDown=False
                    self.WolneRamki-=Alglist[i].Ramki+1













                # alg1 = Alglist[i]
                #
                # if(alg1.MozeDacRamke):
                #     alg1.Ramki-=1
                #     self.WolneRamki+=1
                #     alg1.MozeDacRamke=False
                #     alg1.balans-=1
                #     alg1.ListaRamek=alg1.ListaRamek[:-1]
                # elif(alg1.ChceRamke and self.WolneRamki>0):
                #     alg1.Ramki+=1
                #     self.WolneRamki-=1
                #     alg1.ChceRamke=False
                #     alg1.ListaRamek.append(None)
                #     alg1.balans+=1
                #     alg1.Rozszerzenie+=1
                # # if(alg1.IsShutDown):
                # #

        return [dflist,bledylist,ListaBitowa]


















        # for i in range(len(zwrotlista)):
        #     alg.Ramki = zwrotlista[i]
        #     alg.Queue = data[i]
        #     alg.ListaRamek = [None for x in range(alg.Ramki)]
        #     alg.HistoriaRamek = np.zeros(shape=(1, alg.Ramki), dtype=int)
        #     while (alg.Queue != []):
        #         alg.process()
        #
        #     df = pd.DataFrame(alg.HistoriaRamek[1:])
        #     dflist.append(df)
        #     bledylist.append(alg.LiczbaBledowStron)
        #     ListaBitowa.append(alg.ListaBitowa)
        #     dlugosc = len(alg.ListaBitowa)
        #     suma = 0
        #     szams = []
        #
        #     #cum sum
        #
        #     for i in range(dlugosc):
        #         if (i % self.szamotuly == 0):
        #             szams.append(suma / self.szamotuly)
        #             suma = alg.ListaBitowa[i]
        #
        #
        #         else:
        #             suma = suma + alg.ListaBitowa[i]
        #
        #     Szamotuly.append(szams[1:])
        #     # dflist.append(dflist)
        #     ListaBitowa.append(ListaBitowa)
        #     bledylist.append(bledylist)
        #     Szamotuly.append(Szamotuly)
        #
        # return [dflist, bledylist, ListaBitowa, Szamotuly]

