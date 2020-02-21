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















pipeline.modifiers.append(InvertSelectionModifier())
pipeline.modifiers.append(DeleteSelectedModifier())

export_file(pipeline, "output/antisites.xyz", "xyz",
    columns = ['Position.X', 'Position.Y', 'Position.Z'],
    multiple_frames = True)
