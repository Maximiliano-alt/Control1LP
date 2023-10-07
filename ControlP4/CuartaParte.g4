grammar CuartaParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                            # Mod
      |   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

modo: op=('encendido'|'apagado')                                  # AsignMod
    ;                                 

puntero: ROT '(' MOV '(' INT ',' INT ')' SUM INT ')'                                 # Pos
       ;

ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
ROT:      'rotar';
SUM:      '+';
INT :   '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;
