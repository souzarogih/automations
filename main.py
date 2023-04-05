import argparse
import sys
import tkinter as tk
from tkinter import filedialog
import webbrowser, os


# x = range(7).__reversed__()
# soma = 0
# text = list()
# for n in x:
#     print(n)
#     if n + soma < 21:
#         soma = n + soma
#         text.append(n)
#     elif n + soma == 21:
#         print("Resultado")
#         print("sum", soma)
#         print("text", text)
#
#     print("Parcial: ", soma, "-", text)
#     print("\n")
#


def read_file_command_line():
    # $ python test.py "D:\\Meus arquivos\\Documents\\Desenvolvimento\\MyComandos.txt"
    parser = argparse.ArgumentParser(description='Ler arquivo arrastando para o terminal')
    parser.add_argument('file_path', help='Caminho do arquivo')

    args = parser.parse_args()

    if args.file_path:
        with open(args.file_path, 'r') as file:
            content = file.read()
            print(content)


def read_file_open_folder():
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()

    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            print(content)


def open_folder():
    # caminho = "C:/Users"
    caminho = "D:/Meus arquivos/Documents/Desenvolvimento"
    webbrowser.open(os.path.realpath(caminho))



# read_file_open_folder()
# open_folder()
read_file_command_line()


# https://phylos.net/2021-03-24/python-arquivos-e-pastas
