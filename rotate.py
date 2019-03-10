#!/usr/bin/env python

__author__ = "francazorla7"
__license__ = "GPL"
__version__ = "1.0"

import numpy as np

'''
@param filename: Nombre del fichero de entrada del mapa
@param filenameOutput: Nombre del fichero de salida del mapa rotado
@param n: Numero de veces que se quiere aplicar la rotacion
'''
def rotate(filename, filenameOutput, n=1):

	buff = ""

	with open(filename, "r") as f:

		lines = f.readlines()
		lines_ = [list(l.replace("\n", "")) for l in lines[:-2] if len(l) > 0]

		nlines = len(lines_)
		lengthLine = len(lines_[0])

		oldMap = np.reshape(lines_, (nlines, lengthLine))

		nlines_after_rotate = nlines if n%2 == 1 else lengthLine

		homes = "% "*4+"%"*(nlines_after_rotate-8)+"\n"+"%"*nlines_after_rotate

		for l in list(np.rot90(oldMap, k=n)):
			buff += "".join(l)+"\n"

		buff += homes

	with open(filenameOutput, "w") as f:

		f.write(buff)

if __name__ == '__main__':
	
	rotate("test/map.lay", "test/map_rotated.lay", n=1)