#!/bin/sh
C=20
ST=100000
for T in 700 900 1100 1300
do
	mkdir -p ./slurm_out
	mkdir -p ../Data/cell.${C}.time.${ST}/temp.${T}
	mkdir -p ../Results/cell.${C}.time.${ST}/temp.${T}
  sbatch -J ${T}.${C} -o slurm_out/${T}.${C}.o diff.sbatch ${C} ${T} ${ST}
done
