# -*- coding: utf-8 -*-
"""
used for
用于案由对应逻辑树的初始化：1、定义节点基本信息、2、节点逻辑属性树（节点ID、运算符、子节点父节点）
"""
PRIVATE_LENDING='PRIVATE_LENDING' #民间借贷纠纷

appeal_node_lending={
    # Level 0: root
    1: {'id':1,'name':u'appeal of principal','result_bool':False,'operation': 'and', 'child_nodes': [2, 3], 'father_node': None},# sub node：'loan agreement 2','delivery of money 3'

    # Level 1
    2: {'id':2,'name':u'loan agreement','result_bool':False,'operation': 'or', 'child_nodes': [4,5,6], 'father_node': 1},# sub node: 'written agreement 4','electronic contract 5','oral agreement 6'
    3: {'id':3,'name':u'delivery of money','result_bool':False,'operation': 'or', 'child_nodes': [7, 8], 'father_node': 1}, # sub node:'proof of delivery 7','cash(bill) delivery 8'

    # Level 2
    # sub node of 'loan agreement 2':
    4: {'id':4,'name':u'written agreement','result_bool':False,'operation': 'and', 'child_nodes': [9, 10], 'father_node': 2}, # sub node: 'expression of borrowing money 9',' signature of interested parties 10'
    5: {'id':5,'name':u'electronic contract','result_bool':False,'operation': 'and', 'child_nodes': None, 'father_node': 2},
    6: {'id':6,'name':u'oral agreement','result_bool':False,'operation': 'or', 'child_nodes': None, 'father_node': 2},
    #  sub node of 'delivery of money 3':
    7: {'id':7,'name':u'proof of delivery','result_bool':False,'operation': 'and', 'child_nodes':None, 'father_node': 3},
    8: {'id':8,'name':u'cash(bill) delivery','result_bool':False,'operation': 'or', 'child_nodes': [11, 12], 'father_node': 3}, # sub node:'recepit of cash(bill) 11','defendant confessed 12'

    # Level 3
    # sub node of 'written agreement'
    9: {'id':9,'name':u'expression of borrowing money','result_bool':False,'operation': None, 'child_nodes': None, 'father_node': 4},
    10: {'id':10,'name':u'signature of interested parites','result_bool':False,'operation': 'and', 'child_nodes': None, 'father_node': 4},
    # sub node of 'cash(bill) delivery'
    11: {'id':11,'name':u'receipt of cash(bill)','result_bool':False,'operation': 'and', 'child_nodes': None, 'father_node': 8},
    12: {'id':12,'name':u'the defendant confessed','result_bool':False,'operation': None, 'child_nodes': None, 'father_node': 8},
}


cause_log_tree={PRIVATE_LENDING:appeal_node_lending}