
# _parser_Parser_parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightQUESTIONleftLOGICAL_ORleftLOGICAL_ANDleftBITWISE_ORleftBITWISE_XORleftBITWISE_ANDleftEQUALNEQUALIDENTNIDENTleftLESSLESS_EQUALGREATERGREATER_EQUALleftLSHIFTRSHIFTZFRSHIFTleftPLUSMINUSleftTIMESDIVIDEMODULOleftEXPrightUMINUSUPLUSLOGICAL_NOTBITWISE_NOTBINARY BITWISE_AND BITWISE_NOT BITWISE_OR BITWISE_XOR COLON COMMA DIVIDE EQUAL EXP FLOAT GREATER GREATER_EQUAL HEX IDENT LBRACE LBRACKET LESS LESS_EQUAL LOGICAL_AND LOGICAL_NOT LOGICAL_OR LPAREN LSHIFT MINUS MODULO NAME NEQUAL NIDENT OCTAL PERIOD PLUS QUESTION RBRACE RBRACKET RPAREN RSHIFT STRING TIMES ZFRSHIFT\n        expression : expression PLUS expression\n                   | expression MINUS expression\n                   | expression TIMES expression\n                   | expression DIVIDE expression\n                   | expression EXP expression\n                   | expression MODULO expression\n                   | expression LESS expression\n                   | expression LESS_EQUAL expression\n                   | expression GREATER expression\n                   | expression GREATER_EQUAL expression\n                   | expression LSHIFT expression\n                   | expression RSHIFT expression\n                   | expression ZFRSHIFT expression\n                   | expression EQUAL expression\n                   | expression IDENT expression\n                   | expression NEQUAL expression\n                   | expression NIDENT expression\n                   | expression BITWISE_AND expression\n                   | expression BITWISE_OR expression\n                   | expression BITWISE_XOR expression\n                   | expression LOGICAL_OR expression\n                   | expression LOGICAL_AND expression\n        expression : expression QUESTION expression COLON expression\n        expression : MINUS expression %prec UMINUS\n                   | PLUS expression %prec UPLUS\n                   | BITWISE_NOT expression\n                   | LOGICAL_NOT expression\n        \n        expression : atom\n        \n        number : HEX\n               | OCTAL\n               | BINARY\n               | FLOAT\n        \n        atom : number\n             | STRING\n             | global\n             | list\n             | object\n             | group\n             | attraccess\n             | functioncall\n             | indexing\n        global : NAME\n        list : LBRACKET RBRACKET\n             | LBRACKET arglist RBRACKET\n        \n        object : LBRACE RBRACE\n               | LBRACE objectarglist RBRACE\n        \n        objectarglist : objectarglist COMMA objectarg\n                      | objectarg\n        \n        objectarg : objectkey COLON expression\n                  | NAME\n        \n        objectkey : NAME\n                  | STRING\n                  | number\n        group : LPAREN expression RPARENattraccess : atom PERIOD NAMEindexing : atom LBRACKET expression RBRACKET\n        functioncall : atom LPAREN RPAREN\n                     | atom LPAREN arglist RPAREN\n        \n        arglist : arglist COMMA expression\n                | expression\n        '
    
_lr_action_items = {'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,96,97,98,99,100,101,103,104,],[3,25,3,3,3,3,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,-25,-24,-26,-27,3,3,-43,25,-45,25,-1,-2,-3,-4,-5,-6,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-55,-57,25,-44,3,-46,3,-54,3,-58,-56,25,25,25,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,52,53,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,93,94,96,97,98,99,100,101,103,104,],[2,24,2,2,2,2,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-25,-24,-26,-27,2,2,-43,24,-45,24,-1,-2,-3,-4,-5,-6,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,-55,-57,24,-44,2,-46,2,-54,2,-58,-56,24,24,24,]),'BITWISE_NOT':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LOGICAL_NOT':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'STRING':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,95,96,98,],[8,8,8,8,8,8,62,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,62,8,8,]),'HEX':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,95,96,98,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'OCTAL':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,95,96,98,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'BINARY':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,95,96,98,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'FLOAT':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,95,96,98,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'NAME':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,51,52,53,93,95,96,98,],[20,20,20,20,20,20,61,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,88,20,20,20,61,20,20,]),'LBRACKET':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,57,88,89,92,93,94,96,97,98,99,100,],[21,21,21,21,21,53,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-43,-45,-55,-57,-44,21,-46,21,-54,21,-58,-56,]),'LBRACE':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'LPAREN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,54,57,88,89,92,93,94,96,97,98,99,100,],[23,23,23,23,23,52,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,-43,-45,-55,-57,-44,23,-46,23,-54,23,-58,-56,]),'$end':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,92,94,97,99,100,104,],[0,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,-45,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-55,-57,-44,-46,-54,-58,-56,-23,]),'TIMES':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[26,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,26,-45,26,26,26,-3,-4,-5,-6,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-55,-57,26,-44,-46,-54,-58,-56,26,26,26,]),'DIVIDE':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[27,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,27,-45,27,27,27,-3,-4,-5,-6,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-55,-57,27,-44,-46,-54,-58,-56,27,27,27,]),'EXP':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[28,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,28,-45,28,28,28,28,28,-5,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,-55,-57,28,-44,-46,-54,-58,-56,28,28,28,]),'MODULO':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[29,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,29,-45,29,29,29,-3,-4,-5,-6,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,-55,-57,29,-44,-46,-54,-58,-56,29,29,29,]),'LESS':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[30,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,30,-45,30,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,30,30,30,30,30,30,30,30,30,30,-55,-57,30,-44,-46,-54,-58,-56,30,30,30,]),'LESS_EQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[31,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,31,-45,31,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,31,31,31,31,31,31,31,31,31,31,-55,-57,31,-44,-46,-54,-58,-56,31,31,31,]),'GREATER':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[32,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,32,-45,32,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,32,32,32,32,32,32,32,32,32,32,-55,-57,32,-44,-46,-54,-58,-56,32,32,32,]),'GREATER_EQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[33,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,33,-45,33,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,33,33,33,33,33,33,33,33,33,33,-55,-57,33,-44,-46,-54,-58,-56,33,33,33,]),'LSHIFT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[34,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,34,-45,34,-1,-2,-3,-4,-5,-6,34,34,34,34,-11,-12,-13,34,34,34,34,34,34,34,34,34,34,-55,-57,34,-44,-46,-54,-58,-56,34,34,34,]),'RSHIFT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[35,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,35,-45,35,-1,-2,-3,-4,-5,-6,35,35,35,35,-11,-12,-13,35,35,35,35,35,35,35,35,35,35,-55,-57,35,-44,-46,-54,-58,-56,35,35,35,]),'ZFRSHIFT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[36,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,36,-45,36,-1,-2,-3,-4,-5,-6,36,36,36,36,-11,-12,-13,36,36,36,36,36,36,36,36,36,36,-55,-57,36,-44,-46,-54,-58,-56,36,36,36,]),'EQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[37,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,37,-45,37,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,37,37,37,37,37,37,-55,-57,37,-44,-46,-54,-58,-56,37,37,37,]),'IDENT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[38,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,38,-45,38,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,38,38,38,38,38,38,-55,-57,38,-44,-46,-54,-58,-56,38,38,38,]),'NEQUAL':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[39,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,39,-45,39,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,39,39,39,39,39,39,-55,-57,39,-44,-46,-54,-58,-56,39,39,39,]),'NIDENT':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[40,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,40,-45,40,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,40,40,40,40,40,40,-55,-57,40,-44,-46,-54,-58,-56,40,40,40,]),'BITWISE_AND':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[41,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,41,-45,41,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,41,41,41,41,41,-55,-57,41,-44,-46,-54,-58,-56,41,41,41,]),'BITWISE_OR':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[42,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,42,-45,42,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,42,42,42,-55,-57,42,-44,-46,-54,-58,-56,42,42,42,]),'BITWISE_XOR':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[43,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,43,-45,43,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,43,-20,43,43,43,-55,-57,43,-44,-46,-54,-58,-56,43,43,43,]),'LOGICAL_OR':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[44,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,44,-45,44,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,44,-55,-57,44,-44,-46,-54,-58,-56,44,44,44,]),'LOGICAL_AND':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[45,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,45,-45,45,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,45,-22,45,-55,-57,45,-44,-46,-54,-58,-56,45,45,45,]),'QUESTION':([1,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,91,92,94,97,99,100,101,103,104,],[46,-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,46,-45,46,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,46,-55,-57,46,-44,-46,-54,-58,-56,46,46,46,]),'RBRACKET':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,47,48,49,50,54,55,56,57,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,91,92,94,97,99,100,101,104,],[-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,54,-25,-24,-26,-27,-43,92,-60,-45,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-55,-57,100,-44,-46,-54,-58,-56,-59,-23,]),'COMMA':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,55,56,57,58,59,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,90,92,94,97,99,100,101,102,103,104,],[-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,93,-60,-45,95,-48,-50,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-55,-57,93,-44,-46,-54,-58,-56,-59,-47,-49,-23,]),'RPAREN':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,52,54,56,57,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,90,92,94,97,99,100,101,104,],[-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,89,-43,-60,-45,97,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-55,-57,99,-44,-46,-54,-58,-56,-59,-23,]),'COLON':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,47,48,49,50,54,57,60,61,62,63,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,92,94,97,99,100,104,],[-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-25,-24,-26,-27,-43,-45,96,-51,-52,-53,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,98,-55,-57,-44,-46,-54,-58,-56,-23,]),'RBRACE':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,22,47,48,49,50,54,57,58,59,61,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,88,89,92,94,97,99,100,102,103,104,],[-28,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,57,-25,-24,-26,-27,-43,-45,94,-48,-50,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-55,-57,-44,-46,-54,-58,-56,-47,-49,-23,]),'PERIOD':([6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,54,57,88,89,92,94,97,99,100,],[51,-33,-34,-35,-36,-37,-38,-39,-40,-41,-29,-30,-31,-32,-42,-43,-45,-55,-57,-44,-46,-54,-58,-56,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[1,47,48,49,50,56,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,56,91,101,103,104,]),'atom':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'number':([0,2,3,4,5,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,95,96,98,],[7,7,7,7,7,7,63,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,63,7,7,]),'global':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'list':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'object':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'group':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'attraccess':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'functioncall':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'indexing':([0,2,3,4,5,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,52,53,93,96,98,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'arglist':([21,52,],[55,90,]),'objectarglist':([22,],[58,]),'objectarg':([22,95,],[59,102,]),'objectkey':([22,95,],[60,60,]),}

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
  ('number -> HEX','number',1,'p_number','_parser.py',254),
  ('number -> OCTAL','number',1,'p_number','_parser.py',255),
  ('number -> BINARY','number',1,'p_number','_parser.py',256),
  ('number -> FLOAT','number',1,'p_number','_parser.py',257),
  ('atom -> number','atom',1,'p_atom','_parser.py',263),
  ('atom -> STRING','atom',1,'p_atom','_parser.py',264),
  ('atom -> global','atom',1,'p_atom','_parser.py',265),
  ('atom -> list','atom',1,'p_atom','_parser.py',266),
  ('atom -> object','atom',1,'p_atom','_parser.py',267),
  ('atom -> group','atom',1,'p_atom','_parser.py',268),
  ('atom -> attraccess','atom',1,'p_atom','_parser.py',269),
  ('atom -> functioncall','atom',1,'p_atom','_parser.py',270),
  ('atom -> indexing','atom',1,'p_atom','_parser.py',271),
  ('global -> NAME','global',1,'p_global','_parser.py',276),
  ('list -> LBRACKET RBRACKET','list',2,'p_list','_parser.py',281),
  ('list -> LBRACKET arglist RBRACKET','list',3,'p_list','_parser.py',282),
  ('object -> LBRACE RBRACE','object',2,'p_object','_parser.py',293),
  ('object -> LBRACE objectarglist RBRACE','object',3,'p_object','_parser.py',294),
  ('objectarglist -> objectarglist COMMA objectarg','objectarglist',3,'p_objectarglist','_parser.py',303),
  ('objectarglist -> objectarg','objectarglist',1,'p_objectarglist','_parser.py',304),
  ('objectarg -> objectkey COLON expression','objectarg',3,'p_objectarg','_parser.py',313),
  ('objectarg -> NAME','objectarg',1,'p_objectarg','_parser.py',314),
  ('objectkey -> NAME','objectkey',1,'p_objectkey','_parser.py',323),
  ('objectkey -> STRING','objectkey',1,'p_objectkey','_parser.py',324),
  ('objectkey -> number','objectkey',1,'p_objectkey','_parser.py',325),
  ('group -> LPAREN expression RPAREN','group',3,'p_group','_parser.py',330),
  ('attraccess -> atom PERIOD NAME','attraccess',3,'p_attraccess','_parser.py',334),
  ('indexing -> atom LBRACKET expression RBRACKET','indexing',4,'p_indexing','_parser.py',338),
  ('functioncall -> atom LPAREN RPAREN','functioncall',3,'p_functioncall','_parser.py',348),
  ('functioncall -> atom LPAREN arglist RPAREN','functioncall',4,'p_functioncall','_parser.py',349),
  ('arglist -> arglist COMMA expression','arglist',3,'p_arglist','_parser.py',360),
  ('arglist -> expression','arglist',1,'p_arglist','_parser.py',361),
]
