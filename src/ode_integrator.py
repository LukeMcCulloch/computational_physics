#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 06:54:56 2019

@author: luke


Initially I thought I would use 
the 'generic' ode integrator will come from scipy.integrate.odeint
    Note that this is actually the lsoda integrator from LLNL.
    (FORTRAN odepack lib)
    It includes an Adams type integrator as well as 
    a generalized backward Euler method

odeint has been superceded by scipy.integrate.solve_ivp
    This includes the lsoda integrator as an option, and further 
    includes implicit and explicit Runge-Kutta integrators, 
    
"""


##############################################################
# import needed modules
##############################################################
import numpy as np
#from scipy.integrate import odeint #deprecated
from scipy.integrate import solve_ivp
