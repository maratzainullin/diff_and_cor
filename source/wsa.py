# -var cell 10 -var lattice 2.9151 -var temp 1700 -var simtime 50000 (ps)
# python3.7 wsa.py 10 2.9151 1700 50000
from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np
import sys
import os


cell = sys.argv[1]
temp = sys.argv[2]
simtime = sys.argv[3]
dumps_path = f'../Data/cell.{cell}.time.{simtime}/temp.{temp}'
output_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}'

pipeline = import_file(f'{dumps_path}/sia.dump')
ws = WignerSeitzAnalysisModifier(
    per_type_occupancies = False,
    affine_mapping = ReferenceConfigurationModifier.AffineMapping.ToReference)
ws.reference = FileSource()
ws.reference.load(f'{dumps_path}/clear.dump')

pipeline.modifiers.append(ws)
pipeline.modifiers.append(ExpressionSelectionModifier(expression = 'Occupancy == 1'))
pipeline.modifiers.append(DeleteSelectedModifier())
pipeline.modifiers.append(UnwrapTrajectoriesModifier())

with open(f'{output_path}/coords_unwraped.txt', 'w') as file:
    file.write('time;def_num;x;y;z\n')
    for frame in range(pipeline.source.num_frames):
        data = pipeline.compute(frame)
        string = f'{data.particles.positions[0][0]};{data.particles.positions[0][1]};{data.particles.positions[0][2]}\n'
        file.write(f'{frame};{data.particles.count};{string}')


# os.system(f'python3.7 diff_coef_comp.py {cell} {lattice} {temp} {simtime}')
