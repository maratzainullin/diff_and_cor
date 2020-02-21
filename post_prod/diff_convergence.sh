#!/bin/bash
for (( i=10; i <= 5000; i=i+50 ))
do
    python read_and_shift.py 2.8712 700 $i
done

gnuplot -persist <<-EOFMarker
  set terminal png size 800,600
  set output 'conv50.png'
  set datafile separator ';'
  plot 'data_diff' using 1:2
EOFMarker
