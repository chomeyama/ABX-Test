import os
import shutil

for x in range(8):
    with open(f'set{x+1}.lst', mode='w') as f:
        for i, dire in enumerate(['world', 'nsf', 'nsf-with-world', 'descF0-with-loss']):
            os.makedirs(f'wav/set{x+1}/method{i}', exist_ok=True)
            for j, scale in enumerate(['_x2', '_x0.5']):
                for k, spk in enumerate(['slt', 'bdl', 'clb', 'rms']):
                    file_path = f'{dire}/{spk}_arctic_b{x*8+j*4+k+474:0>4}{scale}.wav'
                    # f.write(file_path + '\n')
                    new_file_path = shutil.move(file_path, f'wav/set{x+1}/method{i}/')