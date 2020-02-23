from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np

pipeline = import_file("/diff_and_cor/dump/sia_1700.dump")
ws = WignerSeitzAnalysisModifier(
    per_type_occupancies = False,
    affine_mapping = ReferenceConfigurationModifier.AffineMapping.Off)
ws.reference = FileSource()
ws.reference.load('/diff_and_cor/dump/clear_1700.dump')

pipeline.modifiers.append(ws)

# def modify(frame, data):
#     occupancies = data.particles['Occupancy']
#     selection = data.particles_.create_property('Selection')


pipeline.modifiers.append(ExpressionSelectionModifier(expression = 'Occupancy == 1'))
pipeline.modifiers.append(InvertSelectionModifier())
pipeline.modifiers.append(DeleteSelectedModifier())

export_file(pipeline, "sia.xyz", "xyz",
    columns = ['Position.X', 'Position.Y', 'Position.Z'],
    multiple_frames = True)
