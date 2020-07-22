#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

Description
----------
This module gives functions coded on lectures

Informations
----------
    Author: Eduardo M.  de Morais
    Maintainer:
    Email: emdemor415@gmail.com
    Copyright:
    Credits:
    License:
    Version:
    Status: in development
    
"""


from math import ceil
from statistics import mean,stdev
from numpy import sort

def percentil(lis,k):
	'''
	Description
	----------
		Gives the k-th percentile of the sample lis

	Arguments
	----------
		list: numpy.array
		k 	: int

	Return
	----------
		float
	'''
	list_sort = sort(lis)
	L = ceil(k*len(list_sort)/100)
	return mean([list_sort[L-1],list_sort[L]]) if k*len(lis)%100==0 else list_sort[L-1]


def z_score(lista,index: int = 0):
	'''
	Description
	----------
		Gives the z-score of a list

	Arguments
	----------
		list: numpy.array
		k 	: int

	Return
	----------
		float
	'''
	med = mean(lista)
	s   = stdev(lista)
	return (lista[index]-med)/s

def pos_from_score(lista,z=0):
	'''
	Description
	----------
		Gives the k-th percentile of the sample lis

	Arguments
	----------
		list: numpy.array
		k 	: int

	Return
	----------
		float
	'''
	med = mean(lista)
	s   = stdev(lista)
	return med+s*z