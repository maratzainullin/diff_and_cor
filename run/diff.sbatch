#!/bin/sh
#SBATCH --comment diff_coef_comp
#SBATCH --exclusive
#SBATCH -p RT_study
#SBATCH -N 2
#SBATCH -n 32
mpirun lmp_mpi -i ../source/diff.lmp -v cell $1 -v temp $2 -v simtime $3
