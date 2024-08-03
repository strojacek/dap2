grammar SAS;
import CommonGrammar;

parse
 : (sas_stmt_list)* EOF
 ;

// Abort Statement
abort_stmt
 : ABORT (ABEND | CANCEL (file_spec)? | RETURN )? INT? NOLIST? ';';
 
file_spec: STRINGLITERAL ;

// Array Statement
array_stmt
 : ARRAY array_name LBracket array_subscript RBracket DOLLAR? INT? array_elements?  initial_value_list? ';';


array_name: Identifier ;
array_subscript 
 : '*'
 | INT (',' INT)*
 | INT ':' INT (',' INT ':' INT)*
 ; 
 
array_elements
 : ARRAY_NUMERIC_ELEMENTS
 | ARRAY_CHARACTER_ELEMENTS
 | ARRAY_ALL_ELEMENTS
 | Identifier+
 | Identifier '-' Identifier
 ;
 
initial_value_list
 : '('
    (initial_value_list_item)
    (COMMA? initial_value_list_item)*
   ')'
 ;

initial_value_list_item
 : INT ':' INT
 | constant_iter_value '*' initial_value_list
 | constant_iter_value '*' constant_value
 | constant_value
 ;

initial_value_list_bk
 : '('
    ((constant_iter_value '*' initial_value_list) | (constant_iter_value '*' constant_value) | constant_value)   
    (COMMA? ((constant_iter_value '*' initial_value_list) | (constant_iter_value '*' constant_value) | constant_value))*
   ')'
 ;
 
constant_iter_value
 : INT
 ;
 
constant_value
 : INT
 | FloatingPointLiteral
 | STRINGLITERAL
 ;

// Assignment Statement
assign_stmt
 : Identifier '=' expression ';'
 ;

// By Statement
by_stmt
 : BY (DESCENDING? Identifier) (DESCENDING? Identifier)* NOTSORTED? GROUPFORMAT? ';'
 ;

// Call Statement
call_stmt
 : CALL expression '(' expressionList? ')' ';'
 ;

// Data Statement
data_stmt
 : DATA ';'
 | DATA Tk_NULL datastmt_cmd? NOLIST? ';' 
 | DATA dataset_name_opt+ datastmt_cmd? NOLIST? ';'
 | DATA view_dsname_opt+ '/' VIEW '=' view_name passwd_opt? source_opt? NESTING? NOLIST? ';'
 | DATA dataset_name '/' PGM '=' program_name passwd_opt? source_opt? NESTING? NOLIST? ';'
 | DATA VIEW '=' view_name passwd_opt? NOLIST? ';'
 | DATA PGM '=' program_name passwd_opt? NOLIST? ';'
 ;
// DATA <data-set-name-1 <(data-set-options-1)>> 
// DATA view-name <data-set-name-1 <(data-set-options-1)>>
dataset_name_opt
 : dataset_name ('(' variables '=' (~('('|')'))*? ')')?
 ;
 
datastmt_cmd
 : '/' DEBUG? NESTING? (STACK '=' INT)?
 ;
 
 // view-name <data-set-name-1 <(data-set-options-1)>>
view_dsname_opt
 : variables variables? ('(' variables '=' (~('('|')'))*? ')')?
 ;
 
view_name : variables  ;
dataset_name : variables;
program_name : variables;
passwd_opt  : '(' (ALTER|READ|PW) '=' (~('('|')'))*? ')' ;
source_opt : ('(' SOURCE '=' (SAVE | ENCRYPT | NOSAVE) ')') ;

// Cards/Datalines Statement
datalines_stmt
 : (DATALINES|CARDS) ';' ~(';')*? ';' 
 ;

datalines4_stmt
 : (DATALINES4|CARDS4) ';' .*? END_DATALINES4
 ;

// Do Loop Statements
do_stmt
 : DO expression TO expression  ';'
 | sas_stmt_list
 | RUN ';'
 ;

do_by_stmt
 : DO expression TO expression BY expression  ';'
 | sas_stmt_list
 | RUN ';'
 ;

do_while_stmt
 : DO expression TO expression WHILE expression  ';'
 | sas_stmt_list
 | RUN ';'
 ;

do_until_stmt
 : DO expression TO expression UNTIL expression  ';'
 | sas_stmt_list
 | RUN ';'
 ;

// Drop statement
drop_stmt 
 : DROP (variables | variables '-' variables)+ ';'
 ;

// Infile statement
infile_stmt
 : INFILE file_specification device_type? infile_options*  ';'
 ;

file_specification
 : STRINGLITERAL
 | Identifier
 | CARDS
 | CARDS4
 | DATALINES
 | DATALINES4
 ;
 
device_type
 : DISK
 | DUMMY
 | GTERM
 | PIPE
 | PLOTTER
 | PRINTER
 | TAPE
 | TEMP
 | TERMINAL
 | UPRINTER
 ;
 
// FIXME: here delimiter allows both character and string
infile_options
 : Identifier EQUAL expression
 | DSD
 | EXPANDTABS 
 | NOEXPANDTABS
 | FLOWOVER 
 | MISSOVER
 | PAD 
 | NOPAD
 | SCANOVER
 | SHAREBUFFERS
 | STOPOVER
 | TRUNCOVER
 | V_INFILE_
 ;

// Input statement
input_stmt
 : INPUT input_specification* INPUT_ODS? (AT | AT AT)? ';'
 ;

put_stmt
 : PUT put_specification* INPUT_ODS? (AT | AT AT)? ';'
 ;

input_specification
 : pointer_control
 | input_variable_format
 | column_specifications
 | '(' identifiers_list ')' '(' informat_list ')' 
 ;

put_specification
 : pointer_control
 | put_variable_format
 | column_specifications
 | '(' identifiers_list ')' '(' informat_list ')'
 ;

pointer_control
 : line_point_control
 | column_point_control
 ;
 
informat_list 
 : (Informat COMMA? (pointer_control)? )+
 ;
 
input_variable_format 
 : input_variable EQUAL?  format_modifier? Informat?
 | input_variable EQUAL? format_modifier? DOLLAR?
 ;
input_variable 
 : variables
 | variables '-' variables
 | variables '{' '*' '}'
 ;
 
put_variable_format
 : put_variable EQUAL?  format_modifier? Informat?
 | put_variable EQUAL? format_modifier? DOLLAR?
 ;
put_variable
 : V_INFILE_
 | ARRAY_ALL_ELEMENTS
 | input_variable
 | (INT '*')? STRINGLITERAL
 | literal
 ;


column_point_control
 : AT INT
 | AT FloatingPointLiteral
 | AT Identifier
 | AT '(' expression ')'
 | '+' INT
 | '+' Identifier
 | '+' FloatingPointLiteral
 | '+' '(' expression ')'
 ;
 
line_point_control
 : '#' INT
 | '#' FloatingPointLiteral
 | '#' '(' expression ')'
 | '/'
 ;
 
format_modifier
 : '?' 
 | '??'
 | '&'
 | ':'
 | '~'
 ;
 
column_specifications
 : INT '-' INT
 ;

// Means Proc Statement
means_proc 
 : DROP (variables | variables '-' variables)+ ';'
 ;
 

// Proc statement
proc_stmt
 : PROC proc_name (~';')*? ';'
 ;
 
proc_name
 : ANOVA
 | CORR
 | MEANS
 | REG
 | SGPLOT
 | PRINT
 ;

// Run Statement
run_stmt
 : RUN CANCEL? ';'
 ;

sas_stmt_list
 : abort_stmt
 | array_stmt
 | by_stmt
 | call_stmt
 | datalines_stmt
 | datalines4_stmt
 | delete_stmt
 | drop_stmt
 | data_stmt
 | if_stmt
 | if_then_else_stmt
 | infile_stmt
 | input_stmt
 | put_stmt
 | means_proc
 | proc_stmt
 // assign must go last
 | assign_stmt
 | run_stmt
 ;
 
if_stmt 
 : IF expression ';'
 ;

if_then_else_stmt
 : IF expression THEN sas_stmt_list (ELSE sas_stmt_list)? 
 ;
 
delete_stmt : DELETE ';' ;
