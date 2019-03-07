
# _parser_Parser_parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightQUESTIONleftLOGICAL_ORleftLOGICAL_ANDleftBITWISE_ORleftBITWISE_XORleftBITWISE_ANDleftEQUALNEQUALIDENTNIDENTleftLESSLESS_EQUALGREATERGREATER_EQUALleftLSHIFTRSHIFTZFRSHIFTleftPLUSMINUSleftTIMESDIVIDEMODULOleftEXPrightUMINUSUPLUSLOGICAL_NOTBITWISE_NOTBINARY BITWISE_AND BITWISE_NOT BITWISE_OR BITWISE_XOR COLON COMMA DIVIDE EQUAL EXP FLOAT GREATER GREATER_EQUAL HEX IDENT LBRACE LBRACKET LESS LESS_EQUAL LOGICAL_AND LOGICAL_NOT LOGICAL_OR LPAREN LSHIFT MINUS MODULO NAME NEQUAL NIDENT OCTAL PERIOD PLUS QUESTION RBRACE RBRACKET RPAREN RSHIFT STRING TIMES ZFRSHIFT\n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression TIMES expression\n                   | expression DIVIDE expression\n                   | expression EXP expression\n                   | expression MODULO expression\n                   | expression LESS expression\n                   | expression LESS_EQUAL expression\n                   | expression GREATER expression\n                   | expression GREATER_EQUAL expression\n                   | expression LSHIFT expression\n                   | expression RSHIFT expression\n                   | expression ZFRSHIFT expression\n                   | expression EQUAL expression\n                   | expression IDENT expression\n                   | expression NEQUAL expression\n                   | expression NIDENT expression\n                   | expression BITWISE_AND expression\n                   | expression BITWISE_OR expression\n                   | expression BITWISE_XOR expression\n                   | expression LOGICAL_OR expression\n                   | expression LOGICAL_AND expression\n        expression : expression QUESTION expression COLON expression\n        expression : MINUS expression %prec UMINUS\n                   | PLUS expression %prec UPLUS\n                   | BITWISE_NOT expression\n                   | LOGICAL_NOT expression\n        \n        expression : atom\n        \n        atom : number\n             | string\n             | global\n             | list\n             | object\n             | group\n             | attraccess\n             | functioncall\n             | indexing\n        \n        number : HEX\n               | OCTAL\n               | BINARY\n               | FLOAT\n        string : STRINGglobal : NAME\n        list : LBRACKET RBRACKET\n             | LBRACKET arglist RBRACKET\n        \n        object : LBRACE RBRACE\n               | LBRACE objectarglist RBRACE\n        \n        objectarglist : objectarglist COMMA objectarg\n                      | objectarg\n        \n        objectarg : objectkey COLON expression\n                  | NAME\n        \n        objectkey : NAME\n                  | string\n                  | number\n        group : LPAREN expression RPARENattraccess : atom PERIOD NAMEindexing : atom LBRACKET expression RBRACKET\n        functioncall : atom LPAREN RPAREN\n                     | atom LPAREN arglist RPAREN\n        \n        arglist : arglist COMMA expression\n                | expression\n        '
    
_lr_action_items = {'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,97,98,99,100,101,102,104,105,],[3,26,3,3,3,3,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-25,-24,-26,-27,3,3,-44,26,-46,26,-1,-2,-3,-4,-5,-6,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-56,-58,26,-45,3,-47,3,-55,3,-59,-57,26,26,26,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,53,54,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,97,98,99,100,101,102,104,105,],[2,25,2,2,2,2,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-25,-24,-26,-27,2,2,-44,25,-46,25,-1,-2,-3,-4,-5,-6,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-56,-58,25,-45,2,-47,2,-55,2,-59,-57,25,25,25,]),'BITWISE_NOT':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LOGICAL_NOT':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'HEX':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'OCTAL':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'BINARY':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'FLOAT':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'STRING':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'NAME':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,52,53,54,94,96,97,99,],[21,21,21,21,21,21,62,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,89,21,21,21,62,21,21,]),'LBRACKET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,55,58,89,90,93,94,95,97,98,99,100,101,],[22,22,22,22,22,54,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,-44,-46,-56,-58,-45,22,-47,22,-55,22,-59,-57,]),'LBRACE':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,55,58,89,90,93,94,95,97,98,99,100,101,],[24,24,24,24,24,53,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-44,-46,-56,-58,-45,24,-47,24,-55,24,-59,-57,]),'$end':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,58,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,93,95,98,100,101,105,],[0,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,-46,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-56,-58,-45,-47,-55,-59,-57,-23,]),'TIMES':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[27,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,27,-46,27,27,27,-3,-4,-5,-6,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-56,-58,27,-45,-47,-55,-59,-57,27,27,27,]),'DIVIDE':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[28,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,28,-46,28,28,28,-3,-4,-5,-6,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-56,-58,28,-45,-47,-55,-59,-57,28,28,28,]),'EXP':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[29,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,29,-46,29,29,29,29,29,-5,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-56,-58,29,-45,-47,-55,-59,-57,29,29,29,]),'MODULO':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[30,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,30,-46,30,30,30,-3,-4,-5,-6,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,-56,-58,30,-45,-47,-55,-59,-57,30,30,30,]),'LESS':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[31,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,31,-46,31,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,31,31,31,31,31,31,31,31,31,31,-56,-58,31,-45,-47,-55,-59,-57,31,31,31,]),'LESS_EQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[32,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,32,-46,32,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,32,32,32,32,32,32,32,32,32,32,-56,-58,32,-45,-47,-55,-59,-57,32,32,32,]),'GREATER':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[33,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,33,-46,33,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,33,33,33,33,33,33,33,33,33,33,-56,-58,33,-45,-47,-55,-59,-57,33,33,33,]),'GREATER_EQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[34,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,34,-46,34,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,34,34,34,34,34,34,34,34,34,34,-56,-58,34,-45,-47,-55,-59,-57,34,34,34,]),'LSHIFT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[35,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,35,-46,35,-1,-2,-3,-4,-5,-6,35,35,35,35,-11,-12,-13,35,35,35,35,35,35,35,35,35,35,-56,-58,35,-45,-47,-55,-59,-57,35,35,35,]),'RSHIFT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[36,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,36,-46,36,-1,-2,-3,-4,-5,-6,36,36,36,36,-11,-12,-13,36,36,36,36,36,36,36,36,36,36,-56,-58,36,-45,-47,-55,-59,-57,36,36,36,]),'ZFRSHIFT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[37,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,37,-46,37,-1,-2,-3,-4,-5,-6,37,37,37,37,-11,-12,-13,37,37,37,37,37,37,37,37,37,37,-56,-58,37,-45,-47,-55,-59,-57,37,37,37,]),'EQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[38,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,38,-46,38,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,38,38,38,38,38,38,-56,-58,38,-45,-47,-55,-59,-57,38,38,38,]),'IDENT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[39,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,39,-46,39,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,39,39,39,39,39,39,-56,-58,39,-45,-47,-55,-59,-57,39,39,39,]),'NEQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[40,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,40,-46,40,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,40,40,40,40,40,40,-56,-58,40,-45,-47,-55,-59,-57,40,40,40,]),'NIDENT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[41,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,41,-46,41,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,41,41,41,41,41,41,-56,-58,41,-45,-47,-55,-59,-57,41,41,41,]),'BITWISE_AND':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[42,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,42,-46,42,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,42,42,42,42,42,-56,-58,42,-45,-47,-55,-59,-57,42,42,42,]),'BITWISE_OR':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[43,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,43,-46,43,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,43,43,43,-56,-58,43,-45,-47,-55,-59,-57,43,43,43,]),'BITWISE_XOR':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[44,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,44,-46,44,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,44,-20,44,44,44,-56,-58,44,-45,-47,-55,-59,-57,44,44,44,]),'LOGICAL_OR':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[45,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,45,-46,45,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,45,-56,-58,45,-45,-47,-55,-59,-57,45,45,45,]),'LOGICAL_AND':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[46,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,46,-46,46,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,46,-22,46,-56,-58,46,-45,-47,-55,-59,-57,46,46,46,]),'QUESTION':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,95,98,100,101,102,104,105,],[47,-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,47,-46,47,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,47,-56,-58,47,-45,-47,-55,-59,-57,47,47,47,]),'RBRACKET':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,48,49,50,51,55,56,57,58,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,92,93,95,98,100,101,102,105,],[-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,55,-25,-24,-26,-27,-44,93,-61,-46,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-56,-58,101,-45,-47,-55,-59,-57,-60,-23,]),'COMMA':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,56,57,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,93,95,98,100,101,102,103,104,105,],[-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,94,-61,-46,96,-49,-51,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-56,-58,94,-45,-47,-55,-59,-57,-60,-48,-50,-23,]),'RPAREN':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,53,55,57,58,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,91,93,95,98,100,101,102,105,],[-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,90,-44,-61,-46,98,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-56,-58,100,-45,-47,-55,-59,-57,-60,-23,]),'COLON':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,48,49,50,51,55,58,61,62,63,64,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,93,95,98,100,101,105,],[-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-25,-24,-26,-27,-44,-46,97,-52,-53,-54,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,99,-56,-58,-45,-47,-55,-59,-57,-23,]),'RBRACE':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,48,49,50,51,55,58,59,60,62,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,89,90,93,95,98,100,101,103,104,105,],[-28,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,58,-25,-24,-26,-27,-44,-46,95,-49,-51,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-56,-58,-45,-47,-55,-59,-57,-48,-50,-23,]),'PERIOD':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,55,58,89,90,93,95,98,100,101,],[52,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-44,-46,-56,-58,-45,-47,-55,-59,-57,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[1,48,49,50,51,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,57,92,102,104,105,]),'atom':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'number':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[7,7,7,7,7,7,64,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,64,7,7,]),'string':([0,2,3,4,5,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,96,97,99,],[8,8,8,8,8,8,63,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,63,8,8,]),'global':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'list':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'object':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'group':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'attraccess':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'functioncall':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'indexing':([0,2,3,4,5,22,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,53,54,94,97,99,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'arglist':([22,53,],[56,91,]),'objectarglist':([23,],[59,]),'objectarg':([23,96,],[60,103,]),'objectkey':([23,96,],[61,61,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','_parser.py',206),
  ('expression -> expression MINUS expression','expression',3,'p_expression_binop','_parser.py',207),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','_parser.py',208),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_binop','_parser.py',209),
  ('expression -> expression EXP expression','expression',3,'p_expression_binop','_parser.py',210),
  ('expression -> expression MODULO expression','expression',3,'p_expression_binop','_parser.py',211),
  ('expression -> expression LESS expression','expression',3,'p_expression_binop','_parser.py',212),
  ('expression -> expression LESS_EQUAL expression','expression',3,'p_expression_binop','_parser.py',213),
  ('expression -> expression GREATER expression','expression',3,'p_expression_binop','_parser.py',214),
  ('expression -> expression GREATER_EQUAL expression','expression',3,'p_expression_binop','_parser.py',215),
  ('expression -> expression LSHIFT expression','expression',3,'p_expression_binop','_parser.py',216),
  ('expression -> expression RSHIFT expression','expression',3,'p_expression_binop','_parser.py',217),
  ('expression -> expression ZFRSHIFT expression','expression',3,'p_expression_binop','_parser.py',218),
  ('expression -> expression EQUAL expression','expression',3,'p_expression_binop','_parser.py',219),
  ('expression -> expression IDENT expression','expression',3,'p_expression_binop','_parser.py',220),
  ('expression -> expression NEQUAL expression','expression',3,'p_expression_binop','_parser.py',221),
  ('expression -> expression NIDENT expression','expression',3,'p_expression_binop','_parser.py',222),
  ('expression -> expression BITWISE_AND expression','expression',3,'p_expression_binop','_parser.py',223),
  ('expression -> expression BITWISE_OR expression','expression',3,'p_expression_binop','_parser.py',224),
  ('expression -> expression BITWISE_XOR expression','expression',3,'p_expression_binop','_parser.py',225),
  ('expression -> expression LOGICAL_OR expression','expression',3,'p_expression_binop','_parser.py',226),
  ('expression -> expression LOGICAL_AND expression','expression',3,'p_expression_binop','_parser.py',227),
  ('expression -> expression QUESTION expression COLON expression','expression',5,'p_expression_ternary','_parser.py',233),
  ('expression -> MINUS expression','expression',2,'p_expression_unaryop','_parser.py',238),
  ('expression -> PLUS expression','expression',2,'p_expression_unaryop','_parser.py',239),
  ('expression -> BITWISE_NOT expression','expression',2,'p_expression_unaryop','_parser.py',240),
  ('expression -> LOGICAL_NOT expression','expression',2,'p_expression_unaryop','_parser.py',241),
  ('expression -> atom','expression',1,'p_expression_atom','_parser.py',248),
  ('atom -> number','atom',1,'p_atom','_parser.py',254),
  ('atom -> string','atom',1,'p_atom','_parser.py',255),
  ('atom -> global','atom',1,'p_atom','_parser.py',256),
  ('atom -> list','atom',1,'p_atom','_parser.py',257),
  ('atom -> object','atom',1,'p_atom','_parser.py',258),
  ('atom -> group','atom',1,'p_atom','_parser.py',259),
  ('atom -> attraccess','atom',1,'p_atom','_parser.py',260),
  ('atom -> functioncall','atom',1,'p_atom','_parser.py',261),
  ('atom -> indexing','atom',1,'p_atom','_parser.py',262),
  ('number -> HEX','number',1,'p_number','_parser.py',268),
  ('number -> OCTAL','number',1,'p_number','_parser.py',269),
  ('number -> BINARY','number',1,'p_number','_parser.py',270),
  ('number -> FLOAT','number',1,'p_number','_parser.py',271),
  ('string -> STRING','string',1,'p_string','_parser.py',276),
  ('global -> NAME','global',1,'p_global','_parser.py',280),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','_parser.py',285),
  ('list -> LBRACKET arglist RBRACKET','list',3,'p_list','_parser.py',286),
  ('object -> LBRACE RBRACE','object',2,'p_object','_parser.py',297),
  ('object -> LBRACE objectarglist RBRACE','object',3,'p_object','_parser.py',298),
  ('objectarglist -> objectarglist COMMA objectarg','objectarglist',3,'p_objectarglist','_parser.py',307),
  ('objectarglist -> objectarg','objectarglist',1,'p_objectarglist','_parser.py',308),
  ('objectarg -> objectkey COLON expression','objectarg',3,'p_objectarg','_parser.py',317),
  ('objectarg -> NAME','objectarg',1,'p_objectarg','_parser.py',318),
  ('objectkey -> NAME','objectkey',1,'p_objectkey','_parser.py',327),
  ('objectkey -> string','objectkey',1,'p_objectkey','_parser.py',328),
  ('objectkey -> number','objectkey',1,'p_objectkey','_parser.py',329),
  ('group -> LPAREN expression RPAREN','group',3,'p_group','_parser.py',334),
  ('attraccess -> atom PERIOD NAME','attraccess',3,'p_attraccess','_parser.py',338),
  ('indexing -> atom LBRACKET expression RBRACKET','indexing',4,'p_indexing','_parser.py',342),
  ('functioncall -> atom LPAREN RPAREN','functioncall',3,'p_functioncall','_parser.py',352),
  ('functioncall -> atom LPAREN arglist RPAREN','functioncall',4,'p_functioncall','_parser.py',353),
  ('arglist -> arglist COMMA expression','arglist',3,'p_arglist','_parser.py',364),
  ('arglist -> expression','arglist',1,'p_arglist','_parser.py',365),
]
