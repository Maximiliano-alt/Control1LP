grammar CuartaParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                            # Mod
      |   puntero NEWLINE                                         # Dib
      |   NEWLINE                                                 # blank
      ;

modo: op=('encendido'|'apagado')                                  # AsignMod
<<<<<<< HEAD
    ;

repetir: REP INT                                                  #Rep
    ;                                 

puntero: op=('mover'|'rotar')'(' puntero (',' puntero)? ')'       # Pos
    |    ROT '(' MOV '(' puntero ',' puntero ')' op=('+'|'-') puntero ')'  #Ang
       | INT                                                      # INT
       ;    
=======
    ;                                 

puntero: ROT '(' MOV '(' INT ',' INT ')' SUM INT ')'                                 # Pos
       ;
>>>>>>> 20ee51737b76975390f3e7cc80b69ad1917b23c0

ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
<<<<<<< HEAD
ROT:      'rotar' ;
SUM:      '+';
RES:      '-';
REP:      'repetir';
INT :  '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;
=======
ROT:      'rotar';
SUM:      '+';
INT :   '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;
>>>>>>> 20ee51737b76975390f3e7cc80b69ad1917b23c0
