#!/bin/sh
#SBATCH --comment rec_time
#SBATCH -p RT_study
#SBATCH -N 2
#SBATCH -n 32
mpirun -np 32 python ex_time.py $1 $2
