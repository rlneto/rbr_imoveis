#######################################################
# 
# ControladorGeraIdPlataforma.py
# Python implementation of the Class ControladorGeraIdPlataforma
# Generated by Enterprise Architect
# Created on:      16-Apr-2024 3:14:54 AM
# Original author: rlnet
# 
#######################################################
from DAOs.DAOContadorPlataforma import DAOContadorPlataforma
from controladores.ControladorGeradorId import ControladorGeradorId


class ControladorGeraIdPlataforma(ControladorGeradorId):

    def __init__(self):
        self.__dao = DAOContadorPlataforma('./contadorPlataforma.pkl')

    def gera_id(self) -> int:
        return self.__dao.update()
