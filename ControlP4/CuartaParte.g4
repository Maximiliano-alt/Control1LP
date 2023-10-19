grammar CuartaParte;

prog: dibujo+ ;

dibujo:   modo NEWLINE                                         # Mod
      |   movimiento NEWLINE                                   # Mov
      |   rotacion NEWLINE                                     # Rot
      |   repetir NEWLINE                                      # Rep
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

repetir: REP INT ':' movimiento                                # SntxRepMov
       | REP INT ':' rotacion                                  # SntxRepRot
       ;

SUM : '+' ;
REST : '-' ;
ENC :     'encendido' ;
APAG :    'apagado' ;
MOV:      'mover' ;
ROT:      'rotar' ;
REP:      'repetir' ;
INT : '-'? [0-9]+ ;
NEWLINE:  '\r'? '\n' ;
WS :      [ \t]+ -> skip ;