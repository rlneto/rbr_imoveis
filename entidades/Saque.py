#######################################################
# 
# Saque.py
# Python implementation of the Class Saque
# Generated by Enterprise Architect
# Created on:      15-Apr-2024 9:30:54 PM
# Original author: rlnet
# 
#######################################################
from entidades.Fluxo import Fluxo

class Saque(Fluxo):
    def __init__(self, ident: int, obs: str, valor: float, data: str):
        super().__init__(ident, obs, valor, data)