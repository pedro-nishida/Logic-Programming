arco(a,b,10).
arco(a,c,2).
arco(a,h,11).
arco(b,d,20).
arco(c,e,10).
arco(d,f,5).
arco(e,f,3).
arco(f,g,4).
arco(h,g,4).

conectados(A,B,C) :- arco(A,B,C);arco(B,A,C).

caminho(A,B,Path,Custo) :-
    caminho(A,B,[A],Path,Custo).

caminho(A,B,_,A->B,Custo) :- conectados(A,B,Custo),!.
caminho(A,B,Ac,A->Path,CustoFinal) :-
    conectados(A,Int,Custo),
    \+ member(Int,Ac),
    caminho(Int,B,[Int|Ac],Path,CustoInt),
    CustoFinal is Custo+CustoInt.