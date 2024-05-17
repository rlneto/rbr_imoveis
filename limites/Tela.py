#######################################################
# 
# Tela.py
# Python implementation of the Class Tela
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################

from abc import ABC, abstractmethod
import PySimpleGUI as sg
class Tela(ABC):

    def __init__(self):
        self.__window = None

    def mostra_popup(self, mensagem):
        sg.popup(mensagem)

    def close(self):
        self.__window.Close()
        self.__window = None
