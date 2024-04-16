#######################################################
# 
# ControladorGeraIdAporte.py
# Python implementation of the Class ControladorGeraIdAporte
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:53 PM
# Original author: rlnet
# 
#######################################################
from controladores.ControladorGeradorId import ControladorGeradorId
from DAOs.DAOContadorAporte import DAOContadorAporte

class ControladorGeraIdAporte(ControladorGeradorId):
    m_DAOContadorAporte= DAOContadorAporte()

    def gera_id():
        pass