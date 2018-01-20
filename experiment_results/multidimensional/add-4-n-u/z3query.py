import sys
import os
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/setuptools/")
currentdirectory = os.path.dirname(os.path.realpath(__file__))
sys.path.append(currentdirectory+"/packages/z3/python/")
from z3 import *
init(currentdirectory+"/packages/z3")
set_param(proof=True)

try:
	_p1=Int('_p1')
	_p2=Int('_p2')
	_n=Int('_n')
	_bool=Int('_bool')
	arraySort = DeclareSort('arraySort')
	_f=Function('_f',IntSort(),IntSort())
	_ToReal=Function('_ToReal',RealSort(),IntSort())
	_ToInt=Function('_ToInt',IntSort(),RealSort())
	_n6=Int('_n6')
	_N8=Const('_N8',IntSort())
	_N7=Function('_N7',IntSort(),IntSort())
	d4array16=Function('d4array16',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_x4=Int('_x4')
	_x5=Int('_x5')
	_n5=Int('_n5')
	_x1=Const('_x1',arraySort)
	_x2=Int('_x2')
	_x3=Int('_x3')
	q1=Int('q1')
	d4array=Function('d4array',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	l19=Function('l19',IntSort(),IntSort(),IntSort(),IntSort())
	k14=Function('k14',IntSort(),IntSort())
	l14=Function('l14',IntSort(),IntSort())
	k23=Function('k23',IntSort(),IntSort(),IntSort())
	_N6=Function('_N6',IntSort(),IntSort(),IntSort())
	A1=Const('A1',arraySort)
	_N2=Function('_N2',IntSort(),IntSort(),IntSort())
	k1=Int('k1')
	m1=Int('m1')
	C1=Const('C1',arraySort)
	j28=Function('j28',IntSort(),IntSort())
	A=Const('A',arraySort)
	d4array14=Function('d4array14',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	C=Const('C',arraySort)
	B=Const('B',arraySort)
	i1=Int('i1')
	_N3=Function('_N3',IntSort(),IntSort())
	_N1=Function('_N1',IntSort(),IntSort(),IntSort(),IntSort())
	d4array19=Function('d4array19',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	_n8=Int('_n8')
	_N4=Const('_N4',IntSort())
	j1=Int('j1')
	l23=Function('l23',IntSort(),IntSort(),IntSort())
	d4array9=Function('d4array9',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	d4array5=Function('d4array5',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	l28=Function('l28',IntSort(),IntSort())
	j14=Function('j14',IntSort(),IntSort())
	_N5=Function('_N5',IntSort(),IntSort(),IntSort(),IntSort())
	d4array1=Function('d4array1',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	k9=Function('k9',IntSort(),IntSort(),IntSort())
	d4array2=Function('d4array2',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	k28=Function('k28',IntSort(),IntSort())
	p1=Int('p1')
	_n2=Int('_n2')
	_n3=Int('_n3')
	_n1=Int('_n1')
	m=Int('m')
	_n7=Int('_n7')
	_n4=Int('_n4')
	n=Int('n')
	q=Int('q')
	p=Int('p')
	l5=Function('l5',IntSort(),IntSort(),IntSort(),IntSort())
	d4array28=Function('d4array28',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	B1=Const('B1',arraySort)
	l1=Int('l1')
	n1=Int('n1')
	d4array23=Function('d4array23',arraySort,IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort(),IntSort())
	l9=Function('l9',IntSort(),IntSort(),IntSort())
	main=Int('main')
	_k1=Int('_k1')
	_k2=Int('_k2')
	_k3=Int('_k3')
	_k4=Int('_k4')
	_k5=Int('_k5')
	_k8=Int('_k8')
	_k6=Int('_k6')
	_k7=Int('_k7')
	_s=Solver()
	_s.add(ForAll([_n],Implies(_n>=0, _f(_n)==_n)))
	_s.set("timeout",50000)
	_s.add(A1 == A)
	_s.add(C1 == C)
	_s.add(B1 == B)
	_s.add(m1 == m)
	_s.add(n1 == n)
	_s.add(q1 == q)
	_s.add(p1 == p)
	_s.add(i1 == _N8)
	_s.add(k1 == k28(_N8))
	_s.add(j1 == j28(_N8))
	_s.add(l1 == l28(_N8))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array1(B,_x2,_x3,_x4,_x5) == d4array28(B,_x2,_x3,_x4,_x5,_N8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array1(C,_x2,_x3,_x4,_x5) == d4array28(C,_x2,_x3,_x4,_x5,_N8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array1(A,_x2,_x3,_x4,_x5) == d4array28(A,_x2,_x3,_x4,_x5,_N8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n1,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))))))),d4array2(A,_x2,_x3,_x4,_x5,_n1 + 1,_n2,_n3,_n4) == d4array2(A,_x2,_x3,_x4,_x5,_n1,_n2,_n3,_n4))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array2(C,_n4,_n3,_n2,_n1,_n1 + 1,_n2,_n3,_n4) == ((d4array2(A,_n4,_n3,_n2,_n1,_n1,_n2,_n3,_n4))+(d4array2(B,_n4,_n3,_n2,_n1,_n1,_n2,_n3,_n4))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n1,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))))))),d4array2(B,_x2,_x3,_x4,_x5,_n1 + 1,_n2,_n3,_n4) == d4array2(B,_x2,_x3,_x4,_x5,_n1,_n2,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(A,_x2,_x3,_x4,_x5,0,_n2,_n3,_n4) == d4array5(A,_x2,_x3,_x4,_x5,_n2,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(C,_x2,_x3,_x4,_x5,0,_n2,_n3,_n4) == d4array5(C,_x2,_x3,_x4,_x5,_n2,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(B,_x2,_x3,_x4,_x5,0,_n2,_n3,_n4) == d4array5(B,_x2,_x3,_x4,_x5,_n2,_n3,_n4))))
	_s.add(ForAll([_n4,_n3,_n2],Implies(And(_n4>=0,And(_n3>=0,_n2>=0)),_N1(_n2, _n3, _n4) >= q)))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n1 < _N1(_n2, _n3, _n4),And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0)))),_f(_n1) < q)))
	_s.add(ForAll([_n4,_n3,_n2],Implies(And(_n4>=0,And(_n3>=0,_n2>=0)),Or(_N1(_n2, _n3, _n4)==0,_N1(_n2, _n3, _n4) - 1 < q))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array5(A,_x2,_x3,_x4,_x5,_n2 + 1,_n3,_n4) == d4array2(A,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array5(C,_x2,_x3,_x4,_x5,_n2 + 1,_n3,_n4) == d4array2(C,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array5(B,_x2,_x3,_x4,_x5,_n2 + 1,_n3,_n4) == d4array2(B,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4))))
	_s.add(ForAll([_n4,_n3,_n2],Implies(And(_n4>=0,And(_n3>=0,_n2>=0)),l5(_n2 + 1, _n3, _n4) == _N1(_n2, _n3, _n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(A,_x2,_x3,_x4,_x5,0,_n3,_n4) == d4array9(A,_x2,_x3,_x4,_x5,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(C,_x2,_x3,_x4,_x5,0,_n3,_n4) == d4array9(C,_x2,_x3,_x4,_x5,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(B,_x2,_x3,_x4,_x5,0,_n3,_n4) == d4array9(B,_x2,_x3,_x4,_x5,_n3,_n4))))
	_s.add(ForAll([_n4,_n3],l5(0, _n3, _n4) == 0))
	_s.add(ForAll([_n4,_n3],Implies(And(_n4>=0,_n3>=0),_N2(_n3, _n4) >= p)))
	_s.add(ForAll([_n4,_n3,_n2],Implies(And(_n2 < _N2(_n3, _n4),And(_n4>=0,And(_n3>=0,_n2>=0))),_f(_n2) < p)))
	_s.add(ForAll([_n4,_n3],Implies(And(_n4>=0,_n3>=0),Or(_N2(_n3, _n4)==0,_N2(_n3, _n4) - 1 < p))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array9(A,_x2,_x3,_x4,_x5,_n3 + 1,_n4) == d4array5(A,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array9(C,_x2,_x3,_x4,_x5,_n3 + 1,_n4) == d4array5(C,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array9(B,_x2,_x3,_x4,_x5,_n3 + 1,_n4) == d4array5(B,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4))))
	_s.add(ForAll([_n4,_n3],Implies(And(_n4>=0,_n3>=0),k9(_n3 + 1, _n4) == _N2(_n3, _n4))))
	_s.add(ForAll([_n4,_n3],Implies(And(_n4>=0,_n3>=0),l9(_n3 + 1, _n4) == l5(_N2(_n3, _n4), _n3, _n4))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(A,_x2,_x3,_x4,_x5,0,_n4) == d4array14(A,_x2,_x3,_x4,_x5,_n4))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(C,_x2,_x3,_x4,_x5,0,_n4) == d4array14(C,_x2,_x3,_x4,_x5,_n4))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(B,_x2,_x3,_x4,_x5,0,_n4) == d4array14(B,_x2,_x3,_x4,_x5,_n4))))
	_s.add(ForAll([_n4],k9(0, _n4) == 0))
	_s.add(ForAll([_n4],l9(0, _n4) == 0))
	_s.add(ForAll([_n4],Implies(_n4>=0,_N3(_n4) >= n)))
	_s.add(ForAll([_n4,_n3],Implies(And(_n3 < _N3(_n4),And(_n4>=0,_n3>=0)),_f(_n3) < n)))
	_s.add(ForAll([_n4],Implies(_n4>=0,Or(_N3(_n4)==0,_N3(_n4) - 1 < n))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array14(A,_x2,_x3,_x4,_x5,_n4 + 1) == d4array9(A,_x2,_x3,_x4,_x5,_N3(_n4),_n4))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array14(C,_x2,_x3,_x4,_x5,_n4 + 1) == d4array9(C,_x2,_x3,_x4,_x5,_N3(_n4),_n4))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array14(B,_x2,_x3,_x4,_x5,_n4 + 1) == d4array9(B,_x2,_x3,_x4,_x5,_N3(_n4),_n4))))
	_s.add(ForAll([_n4],Implies(_n4>=0,k14(_n4 + 1) == k9(_N3(_n4), _n4))))
	_s.add(ForAll([_n4],Implies(_n4>=0,j14(_n4 + 1) == _N3(_n4))))
	_s.add(ForAll([_n4],Implies(_n4>=0,l14(_n4 + 1) == l9(_N3(_n4), _n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(A,_x2,_x3,_x4,_x5,0) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(C,_x2,_x3,_x4,_x5,0) == d4array(C,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(B,_x2,_x3,_x4,_x5,0) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(k14(0) == 0)
	_s.add(j14(0) == 0)
	_s.add(l14(0) == 0)
	_s.add(_N4 >= m)
	_s.add(ForAll([_n4],Implies(And(_n4 < _N4,_n4>=0),_f(_n4) < m)))
	_s.add(Or(_N4==0,_N4 - 1 < m))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n5,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n5>=0,And(_n7>=0,And(_n6>=0,_n8>=0))))))),d4array16(A,_x2,_x3,_x4,_x5,_n5 + 1,_n6,_n7,_n8) == d4array16(A,_x2,_x3,_x4,_x5,_n5,_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n5,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n5>=0,And(_n7>=0,And(_n6>=0,_n8>=0))))))),d4array16(C,_x2,_x3,_x4,_x5,_n5 + 1,_n6,_n7,_n8) == d4array16(C,_x2,_x3,_x4,_x5,_n5,_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n5,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n5>=0,And(_n7>=0,And(_n6>=0,_n8>=0))))))),d4array16(B,_x2,_x3,_x4,_x5,_n5 + 1,_n6,_n7,_n8) == d4array16(B,_x2,_x3,_x4,_x5,_n5,_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(A,_x2,_x3,_x4,_x5,0,_n6,_n7,_n8) == d4array19(A,_x2,_x3,_x4,_x5,_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(C,_x2,_x3,_x4,_x5,0,_n6,_n7,_n8) == d4array19(C,_x2,_x3,_x4,_x5,_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(B,_x2,_x3,_x4,_x5,0,_n6,_n7,_n8) == d4array19(B,_x2,_x3,_x4,_x5,_n6,_n7,_n8))))
	_s.add(ForAll([_n7,_n6,_n8],Implies(And(_n7>=0,And(_n6>=0,_n8>=0)),_N5(_n6, _n7, _n8) >= q)))
	_s.add(ForAll([_n5,_n7,_n6,_n8],Implies(And(_n5 < _N5(_n6, _n7, _n8),And(_n5>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))),_f(_n5) < q)))
	_s.add(ForAll([_n7,_n6,_n8],Implies(And(_n7>=0,And(_n6>=0,_n8>=0)),Or(_N5(_n6, _n7, _n8)==0,_N5(_n6, _n7, _n8) - 1 < q))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array19(A,_x2,_x3,_x4,_x5,_n6 + 1,_n7,_n8) == d4array16(A,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array19(C,_x2,_x3,_x4,_x5,_n6 + 1,_n7,_n8) == d4array16(C,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array19(B,_x2,_x3,_x4,_x5,_n6 + 1,_n7,_n8) == d4array16(B,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8))))
	_s.add(ForAll([_n7,_n6,_n8],Implies(And(_n7>=0,And(_n6>=0,_n8>=0)),l19(_n6 + 1, _n7, _n8) == _N5(_n6, _n7, _n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(A,_x2,_x3,_x4,_x5,0,_n7,_n8) == d4array23(A,_x2,_x3,_x4,_x5,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(C,_x2,_x3,_x4,_x5,0,_n7,_n8) == d4array23(C,_x2,_x3,_x4,_x5,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(B,_x2,_x3,_x4,_x5,0,_n7,_n8) == d4array23(B,_x2,_x3,_x4,_x5,_n7,_n8))))
	_s.add(ForAll([_n7,_n8],l19(0, _n7, _n8) == 0))
	_s.add(ForAll([_n7,_n8],Implies(And(_n7>=0,_n8>=0),_N6(_n7, _n8) >= p)))
	_s.add(ForAll([_n7,_n6,_n8],Implies(And(_n6 < _N6(_n7, _n8),And(_n7>=0,And(_n6>=0,_n8>=0))),_f(_n6) < p)))
	_s.add(ForAll([_n7,_n8],Implies(And(_n7>=0,_n8>=0),Or(_N6(_n7, _n8)==0,_N6(_n7, _n8) - 1 < p))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array23(A,_x2,_x3,_x4,_x5,_n7 + 1,_n8) == d4array19(A,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array23(C,_x2,_x3,_x4,_x5,_n7 + 1,_n8) == d4array19(C,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array23(B,_x2,_x3,_x4,_x5,_n7 + 1,_n8) == d4array19(B,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8))))
	_s.add(ForAll([_n7,_n8],Implies(And(_n7>=0,_n8>=0),k23(_n7 + 1, _n8) == _N6(_n7, _n8))))
	_s.add(ForAll([_n7,_n8],Implies(And(_n7>=0,_n8>=0),l23(_n7 + 1, _n8) == l19(_N6(_n7, _n8), _n7, _n8))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(A,_x2,_x3,_x4,_x5,0,_n8) == d4array28(A,_x2,_x3,_x4,_x5,_n8))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(C,_x2,_x3,_x4,_x5,0,_n8) == d4array28(C,_x2,_x3,_x4,_x5,_n8))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(B,_x2,_x3,_x4,_x5,0,_n8) == d4array28(B,_x2,_x3,_x4,_x5,_n8))))
	_s.add(ForAll([_n8],k23(0, _n8) == 0))
	_s.add(ForAll([_n8],l23(0, _n8) == 0))
	_s.add(ForAll([_n8],Implies(_n8>=0,_N7(_n8) >= n)))
	_s.add(ForAll([_n7,_n8],Implies(And(_n7 < _N7(_n8),And(_n7>=0,_n8>=0)),_f(_n7) < n)))
	_s.add(ForAll([_n8],Implies(_n8>=0,Or(_N7(_n8)==0,_N7(_n8) - 1 < n))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array28(A,_x2,_x3,_x4,_x5,_n8 + 1) == d4array23(A,_x2,_x3,_x4,_x5,_N7(_n8),_n8))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array28(C,_x2,_x3,_x4,_x5,_n8 + 1) == d4array23(C,_x2,_x3,_x4,_x5,_N7(_n8),_n8))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array28(B,_x2,_x3,_x4,_x5,_n8 + 1) == d4array23(B,_x2,_x3,_x4,_x5,_N7(_n8),_n8))))
	_s.add(ForAll([_n8],Implies(_n8>=0,k28(_n8 + 1) == k23(_N7(_n8), _n8))))
	_s.add(ForAll([_n8],Implies(_n8>=0,j28(_n8 + 1) == _N7(_n8))))
	_s.add(ForAll([_n8],Implies(_n8>=0,l28(_n8 + 1) == l23(_N7(_n8), _n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(A,_x2,_x3,_x4,_x5,0) == d4array14(A,_x2,_x3,_x4,_x5,_N4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(C,_x2,_x3,_x4,_x5,0) == d4array14(C,_x2,_x3,_x4,_x5,_N4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(B,_x2,_x3,_x4,_x5,0) == d4array14(B,_x2,_x3,_x4,_x5,_N4))))
	_s.add(k28(0) == 0)
	_s.add(j28(0) == 0)
	_s.add(l28(0) == 0)
	_s.add(_N8 >= m)
	_s.add(ForAll([_n8],Implies(And(_n8 < _N8,_n8>=0),_f(_n8) < m)))
	_s.add(Or(_N8==0,_N8 - 1 < m))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(A,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array2(C,_n4,_n3,_n2,_n1,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(B,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(A,_x2,_x3,_x4,_x5,_N4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array14(C,_n4,_n3,_n2,_n1,_N4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(B,_x2,_x3,_x4,_x5,_N4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(A,_x2,_x3,_x4,_x5,_N3(_n4),_n4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array9(C,_n4,_n3,_n2,_n1,_N3(_n4),_n4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(B,_x2,_x3,_x4,_x5,_N3(_n4),_n4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(A,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array5(C,_n4,_n3,_n2,_n1,_N2(_n3,_n4),_n3,_n4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(B,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(A,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n7,_n6,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0)))))),d4array16(C,_n4,_n3,_n2,_n1,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(B,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(A,_x2,_x3,_x4,_x5,_N8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array28(C,_n4,_n3,_n2,_n1,_N8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(B,_x2,_x3,_x4,_x5,_N8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(A,_x2,_x3,_x4,_x5,_N7(_n8),_n8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n1,_n8,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n8>=0,And(_n3>=0,_n2>=0)))),d4array23(C,_n4,_n3,_n2,_n1,_N7(_n8),_n8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(B,_x2,_x3,_x4,_x5,_N7(_n8),_n8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(A,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_n4,_n7,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0))))),d4array19(C,_n4,_n3,_n2,_n1,_N6(_n7,_n8),_n7,_n8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(B,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(A,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(A,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == d4array2(A,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array2(C,_n4,_n3,_n2,_n1,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array2(C,_n4,_n3,_n2,_n1,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == ((d4array2(A,_n4,_n3,_n2,_n1,_N1(_n2,_n3,_n4),_n2,_n3,_n4))+(d4array2(B,_n4,_n3,_n2,_n1,_N1(_n2,_n3,_n4),_n2,_n3,_n4))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(B,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array2(B,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4) == d4array2(B,_x2,_x3,_x4,_x5,_N1(_n2,_n3,_n4),_n2,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(A,_x2,_x3,_x4,_x5,_N4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array14(A,_x2,_x3,_x4,_x5,_N4) == d4array14(A,_x2,_x3,_x4,_x5,_n4 + 1))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array14(C,_n4,_n3,_n2,_n1,_N4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array14(C,_n4,_n3,_n2,_n1,_N4) == ((d4array14(C,_n4,_n3,_n2,_n1,_n4 + 1))+(d4array14(C,_n4,_n3,_n2,_n1,_n4 + 1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array14(B,_x2,_x3,_x4,_x5,_N4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array14(B,_x2,_x3,_x4,_x5,_N4) == d4array14(B,_x2,_x3,_x4,_x5,_n4 + 1))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(A,_x2,_x3,_x4,_x5,_N3(_n4),_n4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array9(A,_x2,_x3,_x4,_x5,_N3(_n4),_n4) == d4array9(A,_x2,_x3,_x4,_x5,_n3 + 1,_n4))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array9(C,_n4,_n3,_n2,_n1,_N3(_n4),_n4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array9(C,_n4,_n3,_n2,_n1,_N3(_n4),_n4) == ((d4array9(C,_n4,_n3,_n2,_n1,_n3 + 1,_n4))+(d4array9(C,_n4,_n3,_n2,_n1,_n3 + 1,_n4))))))
	_s.add(ForAll([_x3,_x2,_n4,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n4>=0,And(_x5>=0,_x4>=0)))),d4array9(B,_x2,_x3,_x4,_x5,_N3(_n4),_n4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array9(B,_x2,_x3,_x4,_x5,_N3(_n4),_n4) == d4array9(B,_x2,_x3,_x4,_x5,_n3 + 1,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(A,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array5(A,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4) == d4array5(A,_x2,_x3,_x4,_x5,_n2 + 1,_n3,_n4))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array5(C,_n4,_n3,_n2,_n1,_N2(_n3,_n4),_n3,_n4) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array5(C,_n4,_n3,_n2,_n1,_N2(_n3,_n4),_n3,_n4) == ((d4array5(C,_n4,_n3,_n2,_n1,_n2 + 1,_n3,_n4))+(d4array5(C,_n4,_n3,_n2,_n1,_n2 + 1,_n3,_n4))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,_n3>=0))))),d4array5(B,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n4,_n3,_n2],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n4>=0,And(_n3>=0,_n2>=0)))))),d4array5(B,_x2,_x3,_x4,_x5,_N2(_n3,_n4),_n3,_n4) == d4array5(B,_x2,_x3,_x4,_x5,_n2 + 1,_n3,_n4))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(A,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(A,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == d4array16(A,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8))))
	_s.add(ForAll([_n4,_n7,_n6,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0)))))),d4array16(C,_n4,_n3,_n2,_n1,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n7,_n6,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0)))))),d4array16(C,_n4,_n3,_n2,_n1,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == ((d4array16(A,_n4,_n3,_n2,_n1,_N5(_n6,_n7,_n8),_n6,_n7,_n8))+(d4array16(B,_n4,_n3,_n2,_n1,_N5(_n6,_n7,_n8),_n6,_n7,_n8))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(B,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array16(B,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8) == d4array16(B,_x2,_x3,_x4,_x5,_N5(_n6,_n7,_n8),_n6,_n7,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(A,_x2,_x3,_x4,_x5,_N8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array28(A,_x2,_x3,_x4,_x5,_N8) == d4array28(A,_x2,_x3,_x4,_x5,_n8 + 1))))
	_s.add(ForAll([_n4,_n1,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n3>=0,_n2>=0))),d4array28(C,_n4,_n3,_n2,_n1,_N8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n1,_n8,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n8>=0,And(_n3>=0,_n2>=0)))),d4array28(C,_n4,_n3,_n2,_n1,_N8) == ((d4array28(C,_n4,_n3,_n2,_n1,_n8 + 1))+(d4array28(C,_n4,_n3,_n2,_n1,_n8 + 1))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,_x4>=0))),d4array28(B,_x2,_x3,_x4,_x5,_N8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array28(B,_x2,_x3,_x4,_x5,_N8) == d4array28(B,_x2,_x3,_x4,_x5,_n8 + 1))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(A,_x2,_x3,_x4,_x5,_N7(_n8),_n8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array23(A,_x2,_x3,_x4,_x5,_N7(_n8),_n8) == d4array23(A,_x2,_x3,_x4,_x5,_n7 + 1,_n8))))
	_s.add(ForAll([_n4,_n1,_n8,_n3,_n2],Implies(And(_n4>=0,And(_n1>=0,And(_n8>=0,And(_n3>=0,_n2>=0)))),d4array23(C,_n4,_n3,_n2,_n1,_N7(_n8),_n8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n7,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0))))),d4array23(C,_n4,_n3,_n2,_n1,_N7(_n8),_n8) == ((d4array23(C,_n4,_n3,_n2,_n1,_n7 + 1,_n8))+(d4array23(C,_n4,_n3,_n2,_n1,_n7 + 1,_n8))))))
	_s.add(ForAll([_x3,_x2,_n8,_x5,_x4],Implies(And(_x3>=0,And(_x2>=0,And(_n8>=0,And(_x5>=0,_x4>=0)))),d4array23(B,_x2,_x3,_x4,_x5,_N7(_n8),_n8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array23(B,_x2,_x3,_x4,_x5,_N7(_n8),_n8) == d4array23(B,_x2,_x3,_x4,_x5,_n7 + 1,_n8))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(A,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8) == d4array(A,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array19(A,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8) == d4array19(A,_x2,_x3,_x4,_x5,_n6 + 1,_n7,_n8))))
	_s.add(ForAll([_n4,_n7,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0))))),d4array19(C,_n4,_n3,_n2,_n1,_N6(_n7,_n8),_n7,_n8) == ((d4array(A,_n4,_n3,_n2,_n1))+(d4array(B,_n4,_n3,_n2,_n1))))))
	_s.add(ForAll([_n4,_n7,_n6,_n1,_n3,_n2,_n8],Implies(And(_n4>=0,And(_n7>=0,And(_n6>=0,And(_n1>=0,And(_n3>=0,And(_n2>=0,_n8>=0)))))),d4array19(C,_n4,_n3,_n2,_n1,_N6(_n7,_n8),_n7,_n8) == ((d4array19(C,_n4,_n3,_n2,_n1,_n6 + 1,_n7,_n8))+(d4array19(C,_n4,_n3,_n2,_n1,_n6 + 1,_n7,_n8))))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,_n8>=0))))),d4array19(B,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8) == d4array(B,_x2,_x3,_x4,_x5))))
	_s.add(ForAll([_x3,_x2,_x5,_x4,_n7,_n6,_n8],Implies(And(_x3>=0,And(_x2>=0,And(_x5>=0,And(_x4>=0,And(_n7>=0,And(_n6>=0,_n8>=0)))))),d4array19(B,_x2,_x3,_x4,_x5,_N6(_n7,_n8),_n7,_n8) == d4array19(B,_x2,_x3,_x4,_x5,_n6 + 1,_n7,_n8))))
	_s.add(A1 == A)
	_s.add(C1 == C)
	_s.add(B1 == B)
	_s.add(m1 == m)
	_s.add(n1 == n)
	_s.add(q1 == q)
	_s.add(p1 == p)
	_s.add(_k1>=0)
	_s.add(_k5>=0)
	_s.add(ForAll([_n2 ,_n3 ,_n4],_N1(_n2, _n3, _n4)>=0))
	_s.add(ForAll([_n3 ,_n4],_N2(_n3, _n4)>=0))
	_s.add(ForAll([_n4],_N3(_n4)>=0))
	_s.add(_N4>=0)
	_s.add(ForAll([_n6 ,_n7 ,_n8],_N5(_n6, _n7, _n8)>=0))
	_s.add(ForAll([_n7 ,_n8],_N6(_n7, _n8)>=0))
	_s.add(ForAll([_n8],_N7(_n8)>=0))
	_s.add(_N8>=0)
	_s.add(Not(ForAll([_n5,_n7,_n6,_n8],Implies(And(_n5<_N5(_n6, _n7, _n8),And(_n7<_N7(_n8),And(_n6<_N6(_n7, _n8),And(_n8<_N8,And(_n5>=0,And(_n7>=0,And(_n6>=0,_n8>=0))))))),((d4array28(C,_n8,_n7,_n6,_n5,_N8))==(((d4array28(A,_n8,_n7,_n6,_n5,_N8))+(d4array28(B,_n8,_n7,_n6,_n5,_N8)))))))))

except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()

	sys.exit(1)

try:
	result=_s.check()
	if sat==result:
		print "Counter Example"
		print _s.model()
	elif unsat==result:
		result
		try:
			if os.path.isfile('j2llogs.logs'):
				file = open('j2llogs.logs', 'a')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
			else:
				file = open('j2llogs.logs', 'w')
				file.write("\n**************\nProof Details\n**************\n"+str(_s.proof().children())+"\n")
				file.close()
		except Exception as e:
			file = open('j2llogs.logs', 'a')
			file.write("\n**************\nProof Details\n**************\n"+"Error"+"\n")
			file.close()
		print "Successfully Proved"
	else:
		print "Failed To Prove"
except Exception as e:
	print "Error(Z3Query)"
	file = open('j2llogs.logs', 'a')

	file.write(str(e))

	file.close()
