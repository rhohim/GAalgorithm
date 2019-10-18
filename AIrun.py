# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 04:44:48 2019

@author: dull-dekstop
"""

from random import randint
x1min = -3
x1max = 3
x2min= -2
x2max = 2
def human2(length):
    div = length / 2
    a = int(div)
    sel1 = [randint(x1min,x1max) for x in range(a)]
    sel2 = [randint(x2min,x2max) for x in range(a)]
    return sel1+sel2

def population(count, length):
    return [ human2(length) for x in range(count) ]
    

from operator import add
from functools import reduce
    
def gentophen(ab,human,a):
    y = (reduce(add, (10**-x for x in range(a+1)), 0 )) -1
    bagi = x1max - x1min / 9*y
    hasil1= []
    hasil2= []
    for i in range(human) :
        kali1 = (reduce(add,  (ab[i][x-1]*10**-x for x in range(1,a+1)), 0))
        kali2 = (reduce(add, (ab[i][x+(a-1)]*10**-x for x in range(1,a+1)), 0))
        x1 = x1min + bagi + kali1
        x2 = x2min + bagi + kali2
        hasil1.append(x1)
        hasil2.append(x2)
    return hasil1+hasil2

def f(q,human):
    b = len(q)/2
    a = int(b)
    fitness = []
    for i in range(human):
        first = (4-(2.1*q[i]**2) + (q[i]**4/3))*q[i]**2
        mid = q[i]*q[i+a]
        last = (-4 + (4*q[i+a]**2))*q[i+a]**2
        h = first+mid+last
        fit = 2**-h
        fitness.append(fit)
    return fitness

import random
def tournament(pop,fit,human):
    chromfit = []
    indv2 = []
    chromfit = random.sample(fit,5)
    chromfit.sort(reverse = True)
    for i in range(len(chromfit)):
        indv = fit.index(chromfit[i])
        indv2.append(indv)
    return [ pop[indv2[0]],pop[indv2[1]] ]

def crossover(parent,length):
    child1 = []
    child2 = []
    r = randint(1, length-1)
    for i in range(len(parent)):
        for x in range(r):
            if i == 0 :
                child1.append(parent[i][x])
            else:
                child2.append(parent[i][x])
    while (x < length) :
         child1.append(parent[1][x])
         child2.append(parent[0][x])
         x = x+1
    return [child1,child2]

def mutasi(ch,length):
    prob = 0.15
    for i in range(len(ch)):
        for x in range(length):
            a = random.random()
            if prob > a :
                mutan = randint(0,50)
                ch[i][x] = mutan
    return [ch[0],ch[1]]

def survive(phennew,fit,fitnew,mut,pop,cro,a,w):
    view1 = []
    bestpop = []
    for i in range(len(pop)):
        view1.append(fit[i])
        view1.append(pop[i])
    for i in range(len(mut)):
        view1.append(fitnew[i])
        view1.append(mut[i])
    fit.sort()
    for x in range(len(fitnew)):
        if fitnew[x] >= fit[x]:
            fit[x] = fitnew[x]
    fit.sort(reverse = True)
    for i in range(2):
        e = view1.index(fit[i])
        bestpop.append(view1[e+1])
        r = len(bestpop)
        bestphen = gentophen(bestpop,r,a)
    print(" ")
    print("======= Best Chromosome =======")
    print("Generation",w)
    for i in range(2):
        print(i+1,".", bestpop[i])
        print("x1=",bestphen[i],"x2=",bestphen[i+2])

def output(cro,length):
    div = length / 2
    a = int(div)
    q = input("Input how many generation ? ")
    gen = int(q)
    for i in range(gen):
        pop = population(cro,length)
        x1x2 = gentophen(pop,cro,a)
        fit = f(x1x2,cro)
        parent = tournament(pop,fit,cro)
        ch = crossover(parent,length)
        mut = mutasi(ch,length)
        t = len(mut)
        phennew = gentophen(mut,t,a)
        fitnew = f(phennew,t)
        qq=i+1
        survive(phennew,fit,fitnew,mut,pop,cro,a,qq)





    
