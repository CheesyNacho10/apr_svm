#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

with open('polynomial\\polynomial.out') as file:
  header = file.readline().split(' ')
  D=int(header[0])
  R=int(header[1])
  G=int(header[2])
  C=int(header[3])

d=np.loadtxt('polynomial\\polynomial.out', skiprows=1)

# TODO
for d in range(D):
  dv=d[][0]
  di= ; df= 
  for r in range(R):
    rv=[][1]
    ri ; rf=
    for g in range(G):
      gv=d[g*C][2]
      gi=g*C; gf=(g+1)*C

      fig, ax = plt.subplots()
      ax.set_title('Kernel polinómico con degree=' + str(dv) + ', coef0=' + str(rv) + ' y gamma=' + str(gv) +' en MNIST con tr 12k y dv 6k');
      ax.grid();
      ax.set_xscale('log');
      ax.set_xlim([1e-2,1.5e4]);
      ax.set_xlabel('C');
      ax.set_ylim([0,100]);
      ax.set_ylabel('error de clasificación');
      ax.plot(d[gi:gf,1], d[gi:gf,2], label='tr', lw=2, marker='o', markersize=10)
      ax.plot(d[gi:gf,1], d[gi:gf,3], label='dv', lw=2, marker='x', markersize=10)
      ax.legend();
      plt.savefig('polynomial\\plots\\polynomial' + '_d' + str(dv) + '_r' + str(rv) + '_g' + str(gv) + '_C.pdf');
      #plt.show();
