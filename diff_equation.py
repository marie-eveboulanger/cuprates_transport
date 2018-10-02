# -*- coding: Latin-1 -*-

## Modules <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#
import numpy as np
from numpy import cos, sin
from numba import jit

from band_structure import *
##<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<#

## Constant //////
# hbar = 1.05e34
# e = 1.6e19
# m0 = 9.1e31
# kB = 1.38e23
# jtoev = 6.242e18
e = 1
hbar = 1
m = 1


## Functions for ODEINT ///////////////////////////////////////////////////////#
@jit(nopython=True)
def B_func(B_amp, B_theta, B_phi):
    B = B_amp * np.array([sin(B_theta)*cos(B_phi), sin(B_theta)*cos(B_phi), cos(B_theta)])
    return B

@jit("f8[:](f8[:], f8[:])", nopython=True)
def cross_product(u, v):
    product = np.empty(u.shape[0])
    product[0] = u[1] * v[2] - u[2] * v[1]
    product[1] = u[2] * v[0] - u[0] * v[2]
    product[2] = u[0] * v[1] - u[1] * v[0]
    return product

## Movement equation //#
@jit("f8[:](f8[:], f8, f8[:], f8[:])", nopython=True)
def diff_func(k, t, B, band_parameters):
    vx, vy, vz =  v_3D_func(k[0], k[1], k[2], band_parameters)
    v = np.array([vx, vy, vz]).transpose()
    dkdt = ( - e / hbar ) * cross_product(v, - B) # (-) represent -t in vz(-t, kt0) in the Chambers formula
                            # integrated from 0 to +infinity
    return dkdt

## Functions for Runge-Kutta //////////////////////////////////////////////////#
@jit("f8[:,:](f8[:], f8[:], f8[:], f8, f8, f8)", nopython=True)
def cross_product_vector(ux, uy, uz, vx, vy ,vz):
    product = np.empty((ux.shape[0], 3))
    product[:, 0] = uy[:] * vz - uz[:] * vy
    product[:, 1] = uz[:] * vx - ux[:] * vz
    product[:, 2] = ux[:] * vy - uy[:] * vx
    return product

@jit("f8[:,:](f8[:,:], f8, f8[:], f8[:])", nopython=True)
def diff_func_vector(k, t, B, band_parameters):
    vx, vy, vz =  v_3D_func(k[:,0], k[:,1], k[:,2], band_parameters)
    dkdt = ( - e / hbar ) * cross_product_vector(vx, vy, vz, -B[0], -B[1], -B[2]) # (-) represent -t in vz(-t, kt0) in the Chambers formula
                            # integrated from 0 to +infinity
    return dkdt

@jit("f8[:,:,:](f8[:,:], f8[:], f8[:], f8[:])", nopython=True, nogil = True)
def rgk4_algorithm(kft0, t, B, band_parameters):
    dt = t[1] - t[0]
    kft = np.empty( (kft0.shape[0], t.shape[0], 3))

    k = kft0
    for i in range(t.shape[0]):
        k1 = dt * diff_func_vector(k, t[i], B, band_parameters)
        k2 = dt * diff_func_vector(k + k1/2, t[i] + dt/2, B, band_parameters)
        k3 = dt * diff_func_vector(k + k2/2, t[i] + dt/2, B, band_parameters)
        k4 = dt * diff_func_vector(k + k3, t[i] + dt, B, band_parameters)
        k_next = k + (1/6)*k1 + (1/3)*k2 + (1/3)*k3 + (1/6)*k4
        kft[:, i, :] = k_next
        k = k_next

    return kft