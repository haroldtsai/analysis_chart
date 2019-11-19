import re
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--raw_data_in')
args = parser.parse_args()

with open(args.raw_data_in, 'r') as f:
    for row in f.readlines():
        type_pattern = re.compile('pc:(?P<pc>0x[a-f0-9]+), type:(?P<type>[A-Z]+).*')
        r_type_pattern = type_pattern.match(row)

        if r_type_pattern:
            pc = r_type_pattern.group('pc')
            insn_type = r_type_pattern.group('type')
            print('pc = {} type = {}'.format(pc, insn_type))




