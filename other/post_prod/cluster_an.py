from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np

pipeline = import_file("./data_l10_t5e5ps/dumps_700/surr_sia.dump")

pipeline.modifiers.append(ClusterAnalysisModifier(cutoff=5.0, compute_com=True))
#pipeline.modifiers.append(UnwrapTrajectoriesModifier())

with open('ca_700_coords_unwraped', 'w') as file:
    for frame in range(pipeline.source.num_frames):
        data = pipeline.compute(frame)
        #print(data.particles.positions[...])
        com = data.tables['clusters']['Center of Mass']
        file.write(str(frame) + ' ' + str(data.particles.count) + ' ' + str(com))


# export_file(pipeline, "sia_prod.dump", "lammps/dump",
#     columns = ['Position.X', 'Position.Y', 'Position.Z', 'Occupancy'],
#     multiple_frames = True)

# for frame in range(pipeline.source.num_frames):
#     data = pipeline.compute(frame)
#     print(data.particles.positions[...])
