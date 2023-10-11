grammar CuartaParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                            # Mod
      |   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

modo: op=('encendido'|'apagado')                                  # AsignMod
    ;

repetir: REP INT                                                  #Rep
    ;                                 

puntero: op=('mover'|'rotar')'(' puntero (',' puntero)? ')'       # Pos
    |    ROT '(' MOV '(' puntero ',' puntero ')' op=('+'|'-') puntero ')'  #Ang
       | INT                                                      # INT
       ;    

ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
ROT:      'rotar' ;
SUM:      '+';
RES:      '-';
REP:      'repetir';
INT :  '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;