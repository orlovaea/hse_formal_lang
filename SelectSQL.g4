grammar SelectSQL;

select_statement: 
    (select_with_cte)*? 
    select_clause 
    from_clause 
    (join_list)? 
    (where_clause)? 
    (group_by_clause)? 
    (having_clause)? 
    (order_by_clause)? 
    (limit_clause)? 
    (union_clause select_statement)? 
    (SEMICOLON)?
    (EOF)?;

select_with_cte: WITH column_name_list AS LPAREN select_statement RPAREN;

select_clause: SELECT modifier? select_list;

from_clause: FROM table_list;

where_clause: WHERE condition;

group_by_clause: GROUP BY column_name_list;

having_clause: HAVING condition;

order_by_clause: ORDER BY column_name_list (ASC | DESC)?;

limit_clause: LIMIT number;

column_name_list: (column_name | table_column) (COMMA (column_name | table_column))*;

modifier: DISTINCT;

select_list: (select_item | table_column) (COMMA (select_item | table_column))* | ASTERISK;

select_item: expression (AS column_name)?;

expression: column_name | aggregate_function | subquery | table_column;

table_list: table_name (COMMA table_name)* | subquery;

aggregate_function: AGGREGATE LPAREN modifier? (column_name | table_column) RPAREN;

subquery: LPAREN select_statement RPAREN (AS? table_name)?;

table_column: table_name DOT column_name;

table_name: IDENTIFIER;

column_name: IDENTIFIER;

join_list: join_clause (COMMA join_clause)*;

join_clause: (JOIN_TYPE)? JOIN table_name (AS? table_name)? (ON join_condition)?;

join_condition: table_column comparison_operator table_column (logical_operator table_column comparison_operator table_column)*;

union_clause: UNION (ALL)?;

condition: logicalCondition (logical_operator logicalCondition)*;

logicalCondition: comparison_condition
                | expression IS (NULL | NOT NULL)
                | subqueryCondition
                | between_condition;

subqueryCondition: expression comparison_operator subquery;

comparison_condition: expression comparison_operator value;

between_condition: expression BETWEEN number AND number;

logical_operator: AND | OR | AMP | PIPE;

comparison_operator: EQ | NE | LT | LTE | GT | GTE;

value: QT IDENTIFIER QT | number;

number: NUMBER;

ASTERISK: '*';
SELECT: 'SELECT';
FROM: 'FROM';
WHERE: 'WHERE';
GROUP: 'GROUP';
BY: 'BY';
HAVING: 'HAVING';
ORDER: 'ORDER';
ASC: 'ASC';
DESC: 'DESC';
SEMICOLON: ';';
JOIN: 'JOIN';
ON: 'ON';
DISTINCT: 'DISTINCT';
ALL: 'ALL';
UNION: 'UNION';
AS: 'AS';
IS: 'IS';
NOT: 'NOT';
NULL: 'NULL';
AGGREGATE: 'SUM' | 'COUNT' | 'AVG' | 'MIN' | 'MAX';
JOIN_TYPE: 'INNER' | 'OUTER' | 'LEFT' | 'RIGHT' | 'FULL' | 'CROSS';
AND: 'AND';
OR: 'OR';
WITH: 'WITH';
BETWEEN: 'BETWEEN';
LIMIT: 'LIMIT';
LPAREN: '(';
RPAREN: ')';
STRING: '\'' .*? '\'';
IDENTIFIER: [a-zA-Z][a-zA-Z0-9_]*;
NUMBER: [0-9]+;
EQ: '=';
NE: '<>' | '!=' ;
LT: '<';
LTE: '<=';
GT: '>';
GTE: '>=';
COMMA: ',';
DOT: '.';
AMP: '&';
PIPE: '|';
QT: '"';
WS: [ \t\r\n]+ -> skip;
