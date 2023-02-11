hoje(dia(19,julho,2022)).

produto('banana','duzia',5.00).
produto('limao','duzia',7.5).
cesta([['banana', 2],['limao']]).

preco_cesta([],0.0).
preco_cesta([[Nome,Quant]|Resto],Preco) :-
    preco_cesta(Resto,PrecoResto),
    produto(Nome,_,PrecoProduto),
    P is PrecoProduto*Quant,
    Preco is P+PrecoResto.
comprimento([],0).
comprimento([_|T],C) :-
    comprimento(T,CT),
    C is CT + 1.

junta([],L,L).
junta([H|T],L,[H|R]):-
    junta(T,L,R).

resolve(S) :-
    S = barraca(_,_,_,_,_),
    exatamente_a_direita(A, julio),
    nome(A,julio)
    profissao(B,bancario),
    em_algum_lugar_entre(S,C,D,E),
    condimento(C,pimenta),
    condimento(D,maionese),
    condimento(D,mostarda),
    algum_cliente(S,F),
    nome(F,fabiano),
    pastel(F,frango),
    está_ao_lado(S,G,H),
    camiseta(G,vermelha),
    suco(H,maracuja),
    em_algum_lugar_entre(S,I,F,J),
    condimento(I,vinagrete),
    nome(J,carlos),
    algum_cliente(S,K),
    exatamente_a_esquerda(S,L,M),
    profissao(L,relojoeiro),
    suco(M,maça),
    em_algum_lugar_a_esquerda(S,G,N),
    condimento(N,ketchup),
    quarta_posicao(S,O),
    condimento(O,mostarda),
    profissao(S,P,Q),
    profissao(P,feirante),
    condimento(Q,pimenta),
    em_algum_lugar_entre(S,R,T,U),
    pastel(R,frango),
    pastel(T,carne),
    pastel(U,calabreza),
    algum_cliente(S,X),
    camiseta(X,azul),
    condimento(X,maionese),
    exatamente_a_direita(S,Y,Z),
    nome(Y,rubens),
    pastel(Z,queijo),
    algum_cliente(S,A1),
    profissao(A1,maracuja),
    em_algum_lugar_a_esquerda(S,A2,A3),
    camiseta(A2,amarela),
    camiseta(A3,branca),
    em_algum_lugar_entre(S,A4,A5,A6),
    suco(A6,limao),
    primeira_posicao(A7,pizza),
    algum_cliente(S,A8)
    profissao(A8,bancario),
    camiseta(A9,verde),
    em_algum_lugar_entre(S,A9,A10,A11),
    condimento(A10,pimenta),
    profissao(A9,relojoeiro),
    camiseta(A11,azul),
    algum_cliente(S,A12),
    nome(A12,marcelo),
    algum_cliente(S,A13),
    suco(A13,uva),
    algum_cliente(S,A14),
    profissao(A14,vendedor).

primeira_posicao(barraca(X,_,_,_,_),X).

nome(cliente(X,_,_,_,_,_),X).
pastel(cliente(_,_,X,_,_,_),X).
condimento(cliente(_,_,_,X,_,_),X).
suco(cliente(_,_,_,,_,X)).
profissao(cliente(_,_,_,X,_,X)).

