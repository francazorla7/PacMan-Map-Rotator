#!/usr/bin/env python

__author__ = "francazorla7"

import numpy as np
import math

'''
@param modelName: Nombre del fichero que contiene el modelo generado en weka
@param x: La instancia que se pretende clasificar
@param arffName: El nombre del fichero arff que se ha utilizado para generar el modelo en Weka
@return pred: La clase que predice
'''
def trim_and_rotate(filename, filenameOutput, n=1):

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
	
	trim_and_rotate("test/map.lay", "test/map_rotated.lay", n=1)