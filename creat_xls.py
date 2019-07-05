#!/usr/bin/python3
import argparse
import xlwt 
from xlwt import Workbook
 
style_head = xlwt.easyxf('font: bold 1; pattern: pattern solid, fore_colour 0x16; align: horiz centre')
style = xlwt.easyxf('pattern: pattern solid, fore_color red')
style = xlwt.easyxf('font: color red;')
head_names = ['NAME', 'SKILS', 'AGE'] 

def create_sheet_and_add_head_names():
	global sheet1
	global wb
	wb = Workbook(encoding='ascii')
	sheet1 = wb.add_sheet('Sheet 1')
	for p in range(0, len(head_names)):
		sheet1.write(0, p, head_names[p], style_head)
	return sheet1

def args_parser():
	global ap
	global args
	# construct the argument parse and parse the arguments
	ap = argparse.ArgumentParser()
	ap.add_argument("-f", "--file",  required=True,
		help="file from where are taken data")
	ap.add_argument("-m", "--mod_file",  required=True,
        	help="modified file")
	args = vars(ap.parse_args())
	return args


def main():
	args_parser()
	with open(args['file']) as line:
		create_sheet_and_add_head_names()
		c = 1
		for i in line:
			k = i.split()
			for j in range(0, len(k)):
				if int(k[2]) < 24 or k[1] == 'Developer':
					sheet1.write(c, j, k[j], style)
				else:
					sheet1.write(c, j, k[j])
			c += 1
		wb.save(args['mod_file'])

if __name__ == '__main__':
	main()
