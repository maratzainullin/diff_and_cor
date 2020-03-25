from mpi4py import MPI
import random
import os
import sys

cell = int(sys.argv[1])
temp = sys.argv[2]
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
n_proc = comm.Get_size()

n_atoms = 2*(cell**3)
n_runs = 20
s_proc_range = range(rank*(n_atoms//n_proc)+1, (rank+1)*(n_atoms//n_proc)+1)
ids = random.sample(s_proc_range, n_runs//n_proc)
for id in ids:
    cmd = f'lmp_serial -i time.lmp -v cell {cell} -v temp {temp} -v id {id}'
    os.system(cmd)
