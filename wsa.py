from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np

pipeline = import_file("./data_l10_t5e5ps/dumps_700/sia.dump")
ws = WignerSeitzAnalysisModifier(
    per_type_occupancies = False,
    affine_mapping = ReferenceConfigurationModifier.AffineMapping.Off)
ws.reference = FileSource()
ws.reference.load("./data_l10_t5e5ps/dumps_700/clear.dump")

pipeline.modifiers.append(ws)
pipeline.modifiers.append(ExpressionSelectionModifier(expression = 'Occupancy == 1'))
pipeline.modifiers.append(DeleteSelectedModifier())

with open('ws_700_coords', 'w') as file:
    for frame in range(pipeline.source.num_frames):
        data = pipeline.compute(frame)
        #print(data.particles.positions[...])
        string = str(str(data.particles.positions[0][0])) + ' ' + str(data.particles.positions[0][1]) + ' ' + str(data.particles.positions[0][2]) + '\n'
        file.write(str(frame) + ' ' + str(data.particles.count) + ' ' + string)

pipeline.modifiers.append(UnwrapTrajectoriesModifier())

with open('ws_700_coords_unwraped', 'w') as file:
    for frame in range(pipeline.source.num_frames):
        data = pipeline.compute(frame)
        #print(data.particles.positions[...])
        string = str(str(data.particles.positions[0][0])) + ' ' + str(data.particles.positions[0][1]) + ' ' + str(data.particles.positions[0][2]) + '\n'
        file.write(str(frame) + ' ' + str(data.particles.count) + ' ' + string)


# export_file(pipeline, "sia_prod.dump", "lammps/dump",
#     columns = ['Position.X', 'Position.Y', 'Position.Z', 'Occupancy'],
#     multiple_frames = True)

# for frame in range(pipeline.source.num_frames):
#     data = pipeline.compute(frame)
#     print(data.particles.positions[...])
