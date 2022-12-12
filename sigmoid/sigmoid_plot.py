#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

with open('sigmoid\\sigmoid.out') as file:
  header = file.readline().split(' ')
  R=int(header[0])
  G=int(header[1])
  C=int(header[2])

d=np.loadtxt('sigmoid\\sigmoid.out', skiprows=1)

for r in range(R):
  rv = 
  ri = ; rf =
  for g in range(G):
    gv=d[g*C][0]
    gi=g*C; gf=(g+1)*C

    fig, ax = plt.subplots()
    ax.set_title('kernel sigmoidal con coef0' + str(rv) + 'con gamma=' + str(gv) +' en MNIST con tr 12k y dv 6k');
    ax.grid();
    ax.set_xscale('log');
    ax.set_xlim([1e-2,1.5e4]);
    ax.set_xlabel('C');
    ax.set_ylim([0,100]);
    ax.set_ylabel('error de clasificación');
    ax.plot(d[gi:gf,1], d[gi:gf,2], label='tr', lw=2, marker='o', markersize=10)
    ax.plot(d[gi:gf,1], d[gi:gf,3], label='dv', lw=2, marker='x', markersize=10)
    ax.legend();
    plt.savefig('sigmoid\\plots\\sigmoid' + '_r' + str(rv) + '_g' + str(gv) + '_C.pdf');
    #plt.show();
