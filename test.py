#!/usr/bin/python
#-*- coding:utf-8 -*-
from graph import Graph
from graph_node import GraphNode
from trans_model import TransModel
import common,sys
reload(sys)
sys.setdefaultencoding('utf-8');

if len(sys.argv) <= 1:
	print 'Usage:%s jsonfile' %sys.argv[0];
	sys.exit(-1);
jdata = common.read_json(sys.argv[1]);

tm = TransModel();

for key in jdata:
	item = jdata[key];
	for ni in item:
		if ni.has_key('reg'):
			tm.creat_graph(ni['reg']);
			tm.graph.print_path();
'''
tm.creat_graph(u'自(从|打)*');
tm.graph.print_dot('calc');
tm.graph.print_path();
'''
