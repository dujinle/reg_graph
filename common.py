#!/usr/bin/python
#-*- coding:utf-8 -*-
import os,sys,json
from collections import OrderedDict

def read_json(dfile):
	fid = open(dfile,'r');
	ondata = list();
	while True:
		line = fid.readline();
		if not line: break;
		line = line.replace('\r','').replace('\n','').replace('\t','');
		if len(line) <= 0 or line[0] == '#':
			continue;
		if line[0] == '>' or line[0] == '<':
			continue;
		ondata.append(line);
	all_test = ''.join(ondata);
	#print dfile,all_test
	try:
		ojson = json.loads(all_test,object_pairs_hook=OrderedDict);
		return ojson;
	except Exception as e:
		raise e;

def print_dic(struct):
	value = json.dumps(struct,indent = 4,ensure_ascii=False);
	print value;
