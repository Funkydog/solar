#Main code

import settings as cst
from var_func import clearall
from importlib import reload
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

reload(cst)
cst.init()

c=cst.c

def op(file,func):
        """Ouvrir un fichier file.py et l'executer la fonction func definit."""
        with open(file) as f:
                f=f.read()
                func(f)

		
if __name__ == "__main__":
        import sys
        try:
                print (int(sys.argv[1]))
        except:
                print('Fichier ouvert sans arguments')
