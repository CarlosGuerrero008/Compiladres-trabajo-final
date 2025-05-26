grammar InventarioDSL;

script: statement+ ;

statement
    : loadStmt
    | filterStmt
    | aggregateStmt
    | printStmt
    ;

loadStmt: 'load' STRING ';' ;

filterStmt
    : 'filter' 'column' STRING comparisonOperator value ';'
    | 'filter' 'column' STRING 'between' value 'and' value ';'
    ;

aggregateStmt: 'aggregate' aggregationOperator 'column' STRING ';' ;
printStmt: 'print' ';' ;

comparisonOperator: '>' | '<' | '=' | '>=' | '<=' ;
aggregationOperator: 'count' | 'sum' | 'average' ;

value: STRING | NUMERIC ;

BETWEEN: 'between' ;
AND: 'and' ;

STRING: '"' (~["\r\n])* '"' ;
NUMERIC: [0-9]+ ('.' [0-9]+)? ;
ID: [a-zA-Z_][a-zA-Z0-9_]* ;

WS: [ \t\r\n]+ -> skip ;
