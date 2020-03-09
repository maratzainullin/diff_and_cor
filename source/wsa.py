from ovito.io import *
from ovito.data import *
from ovito.modifiers import *
from ovito.pipeline import *
import numpy as np
from progress.bar import IncrementalBar
import sys
import time


cell = 20
simtime = 100000
temp = sys.argv[1]


dumps_path = f'../Data/cell.{cell}.time.{simtime}/temp.{temp}'
output_path = f'../Results/cell.{cell}.time.{simtime}/temp.{temp}'


def import_dump(dumps_path):
    print('Importing dump file...')
    start = time.time()
    pipeline = import_file(f'{dumps_path}/sia.dump')
    finish = time.time()
    print(f'Importing time = {finish - start}')
    return pipeline


def do_wsa(dumps_path, pipeline):
    print('Loading WSA mod...')
    start = time.time()
    ws = WignerSeitzAnalysisModifier()
    ws.per_type_occupancies = False
    ws.affine_mapping = ReferenceConfigurationModifier.AffineMapping.ToReference
    ws.reference = FileSource()
    ws.reference.load(f'{dumps_path}/clear.dump')

    print('Applying WSA mod...')
    pipeline.modifiers.append(ws)

    print('Applying expression selection mod...')
    pipeline.modifiers.append(ExpressionSelectionModifier(expression = 'Occupancy == 1'))

    print('Applying delete selected mod...')
    pipeline.modifiers.append(DeleteSelectedModifier())

    print('Applying unwrap trajectories mod...')
    pipeline.modifiers.append(UnwrapTrajectoriesModifier())

    finish = time.time()
    print(f'Mods time = {finish - start}')


def write_results(output_path, pipeline):
    print('Computing and writing coordinates...')
    start = time.time()
    frames = pipeline.source.num_frames
    bar = IncrementalBar('zZzZz...', max = frames)
    with open(f'{output_path}/coords_unwraped.txt', 'w') as file:
        file.write('time;def_num;x;y;z\n')
        for frame in range(frames):
            data = pipeline.compute(frame)
            file.write(f'{frame};{data.particles.count};'
                       f'{data.particles.positions[0][0]};'
                       f'{data.particles.positions[0][1]};'
                       f'{data.particles.positions[0][2]}\n')
            bar.next()
    bar.finish()
    finish = time.time()
    print(f'Computing time = {finish - start}')


pipeline = import_dump(dumps_path)
do_wsa(dumps_path, pipeline)
write_results(output_path, pipeline)
print('All done!')
