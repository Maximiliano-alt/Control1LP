grammar Gramatica; // rename to distinguish from Expr.g4

prog:   stat+ ;

stat:   expr NEWLINE                # printExpr
    |   ID '=' expr NEWLINE         # assign
    |   NEWLINE                     # blank
    ;

expr:   expr op=('encendido'|'apagado')    # EncApa
    |   INT                         # int
    |   COMA
    |   '(' expr ')'                # parens
    ;

COMA :   ',' ; // assigns token name to '*' used above in grammar
ENC :   'encendido' ;
APAG :   'apagado' ;
ID  :   [a-zA-Z]+ ;      // match identifiers
INT :   [0-9]+ ;         // match integers
NEWLINE:'\r'? '\n' ;     // return newlines to parser (is end-statement signal)
WS  :   [ \t]+ -> skip ; // toss out whitespace