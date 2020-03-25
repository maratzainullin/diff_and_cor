#!/bin/sh
C=12
for T in 700 800 900 1000
do
	mkdir -p ./log
	mkdir -p ../Data/cell.${C}/temp.${T}/dumps
	mkdir -p ../Results/cell.${C}/temp.${T}
	sbatch -J ${T}.time -o log/${T}.sim run_single.sbatch ${C} ${T}
done
