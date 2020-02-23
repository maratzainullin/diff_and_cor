#!/bin/sh
#SBATCH -J diff700
#SBATCH --exclusive
#SBATCH --comment t700l12Time5*10e4ps
#SBATCH -p RT
#SBATCH -N 3
#SBATCH -n 48
#SBATCH
mpirun -np 46 ~/tools/lammps/src/lmp_mpi -in diff.lmp -var l 2.8712 -var t 700 &
mpirun -np 1 ~/tools/lammps/src/lmp_mpi -in diff.lmp -l none -var l 2.8712 -var t 700
