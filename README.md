# reg_graph
解码regix正则表达式，并生成nfa有向图，输出形式为dot形式。可以用Graphviz生成有向图片
比如正则:
	"自(从|打)*"
的有向图如下列内容,

digraph calc {
	node[fontname=FangSong]
	0->1[label=自]
	1->7[label=E]
	2->3[label=从]
	3->7[label=E]
	4->5[label=打]
	5->7[label=E]
	6->2[label=E]
	6->4[label=E]
	6->8[label=E]
	7->6[label=E]
	7->8[label=E]
}

