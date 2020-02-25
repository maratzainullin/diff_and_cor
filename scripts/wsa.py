# -var cell 10 -var lattice 2.9151 -var temp 1700 -var simtime 50000 (ps)
#python3.7 wsa.py 10 2.9151 1700 50000
from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np
#from progress.bar import IncrementalBar
import sys
import os
cell = sys.argv[1]
lattice = sys.argv[2]
temp = sys.argv[3]
simtime = sys.argv[4]
dumps_path = f'../data_cell{cell}_time{simtime}/data_{temp}/dumps'
# bar = IncrementalBar('Wait a minute', max = 50001)
pipeline = import_file(f'{dumps_path}/sia.dump')
ws = WignerSeitzAnalysisModifier(
    per_type_occupancies = False,
    affine_mapping = ReferenceConfigurationModifier.AffineMapping.Off)
ws.reference = FileSource()
ws.reference.load(f'{dumps_path}/clear.dump')

pipeline.modifiers.append(ws)
pipeline.modifiers.append(ExpressionSelectionModifier(expression = 'Occupancy == 1'))
pipeline.modifiers.append(DeleteSelectedModifier())
pipeline.modifiers.append(UnwrapTrajectoriesModifier())

output_path = f'../data_cell{cell}_time{simtime}/data_{temp}'
with open(f'{output_path}/ws_coords_unwraped', 'w') as file:
    for frame in range(pipeline.source.num_frames):
        data = pipeline.compute(frame)
        string = f'{data.particles.positions[0][0]} {data.particles.positions[0][1]} {data.particles.positions[0][2]} \n'
        file.write(f'{frame} {data.particles.count} {string}')
        #bar.next()

#bar.finish()
os.system(f'python3.7 diff_coef_comp.py {cell} {lattice} {temp} {simtime}')
