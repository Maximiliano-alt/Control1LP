grammar TerceraParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                         # Mod
      |   movimiento NEWLINE                                   # Mov
      |   rotacion NEWLINE                                     # Rot
      |   NEWLINE                                              # blank
      ;

modo: op=('encendido'|'apagado')                               # AsignMod
    ;                                 

movimiento: MOV '(' INT (',' INT)? ')'                         # SntxMov
          | INT                                                # INT
          ;

rotacion: ROT '(' INT (',' INT)? ')'                           # SntxRot
        | ROT '(' movimiento op=('-'|'+') movimiento ')'       # SntxRotOp
        ;

SUM : '+' ;
REST : '-' ;
ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
ROT:      'rotar' ;
INT : '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;