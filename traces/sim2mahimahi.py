import os
import numpy as np
import argparse


FILE_SIZE = 2000
MBPS_PER_PKTMS = 12.0


def main(args):
	files = os.listdir(args.in_dir)
	for trace_file in files:
		if os.stat(os.path.join(args.in_dir, trace_file)).st_size >= FILE_SIZE:
			print(os.path.join(args.in_dir, trace_file))			
			with open(os.path.join(args.in_dir, trace_file), 'rb') as f, open(os.path.join(args.out_dir, trace_file), 'wb') as mf:
				ms_cur = 0
				mf.write(bytes(str(ms_cur) + '\n', encoding='utf-8'))
				remain_pkt = 0
				for line in f:
					ms_last = ms_cur
					ms_cur = int(float(line.split()[0]) * 1000)
					throughput = float(line.split()[1])
					ms_pointer = ms_last
					remain_pkt += throughput / MBPS_PER_PKTMS
					while ms_pointer < ms_cur:
						while remain_pkt > 1:
							mf.write(bytes(str(ms_pointer) + '\n', encoding='utf-8'))
							remain_pkt -= 1
						ms_pointer += 1
						remain_pkt += throughput / MBPS_PER_PKTMS


if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('-i', '--in-dir')
	parser.add_argument('-o', '--out-dir')
	args = parser.parse_args()
	main(args)
