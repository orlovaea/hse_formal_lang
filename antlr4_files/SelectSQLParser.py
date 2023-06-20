# Generated from SelectSQL.g4 by ANTLR 4.13.0
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,44,309,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,2,31,7,31,2,32,7,32,1,0,
        5,0,68,8,0,10,0,12,0,71,9,0,1,0,1,0,1,0,3,0,76,8,0,1,0,3,0,79,8,
        0,1,0,3,0,82,8,0,1,0,3,0,85,8,0,1,0,3,0,88,8,0,1,0,3,0,91,8,0,1,
        0,1,0,1,0,3,0,96,8,0,1,0,3,0,99,8,0,1,0,3,0,102,8,0,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,2,1,2,3,2,113,8,2,1,2,1,2,1,3,1,3,1,3,1,4,1,4,
        1,4,1,5,1,5,1,5,1,5,1,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,134,8,7,1,8,
        1,8,1,8,1,9,1,9,3,9,141,8,9,1,9,1,9,1,9,3,9,146,8,9,5,9,148,8,9,
        10,9,12,9,151,9,9,1,10,1,10,1,11,1,11,3,11,157,8,11,1,11,1,11,1,
        11,3,11,162,8,11,5,11,164,8,11,10,11,12,11,167,9,11,1,11,3,11,170,
        8,11,1,12,1,12,1,12,3,12,175,8,12,1,13,1,13,1,13,1,13,3,13,181,8,
        13,1,14,1,14,1,14,5,14,186,8,14,10,14,12,14,189,9,14,1,14,3,14,192,
        8,14,1,15,1,15,1,15,3,15,197,8,15,1,15,1,15,3,15,201,8,15,1,15,1,
        15,1,16,1,16,1,16,1,16,3,16,209,8,16,1,16,3,16,212,8,16,1,17,1,17,
        1,17,1,17,1,18,1,18,1,19,1,19,1,20,1,20,1,20,5,20,225,8,20,10,20,
        12,20,228,9,20,1,21,3,21,231,8,21,1,21,1,21,1,21,3,21,236,8,21,1,
        21,3,21,239,8,21,1,21,1,21,3,21,243,8,21,1,22,1,22,1,22,1,22,1,22,
        1,22,1,22,1,22,5,22,253,8,22,10,22,12,22,256,9,22,1,23,1,23,3,23,
        260,8,23,1,24,1,24,1,24,1,24,5,24,266,8,24,10,24,12,24,269,9,24,
        1,25,1,25,1,25,1,25,1,25,1,25,3,25,277,8,25,1,25,1,25,3,25,281,8,
        25,1,26,1,26,1,26,1,26,1,27,1,27,1,27,1,27,1,28,1,28,1,28,1,28,1,
        28,1,28,1,29,1,29,1,30,1,30,1,31,1,31,1,31,1,31,3,31,305,8,31,1,
        32,1,32,1,32,1,69,0,33,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,
        32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,62,64,0,3,1,0,9,10,
        2,0,23,24,41,42,1,0,33,38,317,0,69,1,0,0,0,2,103,1,0,0,0,4,110,1,
        0,0,0,6,116,1,0,0,0,8,119,1,0,0,0,10,122,1,0,0,0,12,126,1,0,0,0,
        14,129,1,0,0,0,16,135,1,0,0,0,18,140,1,0,0,0,20,152,1,0,0,0,22,169,
        1,0,0,0,24,171,1,0,0,0,26,180,1,0,0,0,28,191,1,0,0,0,30,193,1,0,
        0,0,32,204,1,0,0,0,34,213,1,0,0,0,36,217,1,0,0,0,38,219,1,0,0,0,
        40,221,1,0,0,0,42,230,1,0,0,0,44,244,1,0,0,0,46,257,1,0,0,0,48,261,
        1,0,0,0,50,280,1,0,0,0,52,282,1,0,0,0,54,286,1,0,0,0,56,290,1,0,
        0,0,58,296,1,0,0,0,60,298,1,0,0,0,62,304,1,0,0,0,64,306,1,0,0,0,
        66,68,3,2,1,0,67,66,1,0,0,0,68,71,1,0,0,0,69,70,1,0,0,0,69,67,1,
        0,0,0,70,72,1,0,0,0,71,69,1,0,0,0,72,73,3,4,2,0,73,75,3,6,3,0,74,
        76,3,40,20,0,75,74,1,0,0,0,75,76,1,0,0,0,76,78,1,0,0,0,77,79,3,8,
        4,0,78,77,1,0,0,0,78,79,1,0,0,0,79,81,1,0,0,0,80,82,3,10,5,0,81,
        80,1,0,0,0,81,82,1,0,0,0,82,84,1,0,0,0,83,85,3,12,6,0,84,83,1,0,
        0,0,84,85,1,0,0,0,85,87,1,0,0,0,86,88,3,14,7,0,87,86,1,0,0,0,87,
        88,1,0,0,0,88,90,1,0,0,0,89,91,3,16,8,0,90,89,1,0,0,0,90,91,1,0,
        0,0,91,95,1,0,0,0,92,93,3,46,23,0,93,94,3,0,0,0,94,96,1,0,0,0,95,
        92,1,0,0,0,95,96,1,0,0,0,96,98,1,0,0,0,97,99,5,11,0,0,98,97,1,0,
        0,0,98,99,1,0,0,0,99,101,1,0,0,0,100,102,5,0,0,1,101,100,1,0,0,0,
        101,102,1,0,0,0,102,1,1,0,0,0,103,104,5,25,0,0,104,105,3,18,9,0,
        105,106,5,17,0,0,106,107,5,28,0,0,107,108,3,0,0,0,108,109,5,29,0,
        0,109,3,1,0,0,0,110,112,5,2,0,0,111,113,3,20,10,0,112,111,1,0,0,
        0,112,113,1,0,0,0,113,114,1,0,0,0,114,115,3,22,11,0,115,5,1,0,0,
        0,116,117,5,3,0,0,117,118,3,28,14,0,118,7,1,0,0,0,119,120,5,4,0,
        0,120,121,3,48,24,0,121,9,1,0,0,0,122,123,5,5,0,0,123,124,5,6,0,
        0,124,125,3,18,9,0,125,11,1,0,0,0,126,127,5,7,0,0,127,128,3,48,24,
        0,128,13,1,0,0,0,129,130,5,8,0,0,130,131,5,6,0,0,131,133,3,18,9,
        0,132,134,7,0,0,0,133,132,1,0,0,0,133,134,1,0,0,0,134,15,1,0,0,0,
        135,136,5,27,0,0,136,137,3,64,32,0,137,17,1,0,0,0,138,141,3,38,19,
        0,139,141,3,34,17,0,140,138,1,0,0,0,140,139,1,0,0,0,141,149,1,0,
        0,0,142,145,5,39,0,0,143,146,3,38,19,0,144,146,3,34,17,0,145,143,
        1,0,0,0,145,144,1,0,0,0,146,148,1,0,0,0,147,142,1,0,0,0,148,151,
        1,0,0,0,149,147,1,0,0,0,149,150,1,0,0,0,150,19,1,0,0,0,151,149,1,
        0,0,0,152,153,5,14,0,0,153,21,1,0,0,0,154,157,3,24,12,0,155,157,
        3,34,17,0,156,154,1,0,0,0,156,155,1,0,0,0,157,165,1,0,0,0,158,161,
        5,39,0,0,159,162,3,24,12,0,160,162,3,34,17,0,161,159,1,0,0,0,161,
        160,1,0,0,0,162,164,1,0,0,0,163,158,1,0,0,0,164,167,1,0,0,0,165,
        163,1,0,0,0,165,166,1,0,0,0,166,170,1,0,0,0,167,165,1,0,0,0,168,
        170,5,1,0,0,169,156,1,0,0,0,169,168,1,0,0,0,170,23,1,0,0,0,171,174,
        3,26,13,0,172,173,5,17,0,0,173,175,3,38,19,0,174,172,1,0,0,0,174,
        175,1,0,0,0,175,25,1,0,0,0,176,181,3,38,19,0,177,181,3,30,15,0,178,
        181,3,32,16,0,179,181,3,34,17,0,180,176,1,0,0,0,180,177,1,0,0,0,
        180,178,1,0,0,0,180,179,1,0,0,0,181,27,1,0,0,0,182,187,3,36,18,0,
        183,184,5,39,0,0,184,186,3,36,18,0,185,183,1,0,0,0,186,189,1,0,0,
        0,187,185,1,0,0,0,187,188,1,0,0,0,188,192,1,0,0,0,189,187,1,0,0,
        0,190,192,3,32,16,0,191,182,1,0,0,0,191,190,1,0,0,0,192,29,1,0,0,
        0,193,194,5,21,0,0,194,196,5,28,0,0,195,197,3,20,10,0,196,195,1,
        0,0,0,196,197,1,0,0,0,197,200,1,0,0,0,198,201,3,38,19,0,199,201,
        3,34,17,0,200,198,1,0,0,0,200,199,1,0,0,0,201,202,1,0,0,0,202,203,
        5,29,0,0,203,31,1,0,0,0,204,205,5,28,0,0,205,206,3,0,0,0,206,211,
        5,29,0,0,207,209,5,17,0,0,208,207,1,0,0,0,208,209,1,0,0,0,209,210,
        1,0,0,0,210,212,3,36,18,0,211,208,1,0,0,0,211,212,1,0,0,0,212,33,
        1,0,0,0,213,214,3,36,18,0,214,215,5,40,0,0,215,216,3,38,19,0,216,
        35,1,0,0,0,217,218,5,31,0,0,218,37,1,0,0,0,219,220,5,31,0,0,220,
        39,1,0,0,0,221,226,3,42,21,0,222,223,5,39,0,0,223,225,3,42,21,0,
        224,222,1,0,0,0,225,228,1,0,0,0,226,224,1,0,0,0,226,227,1,0,0,0,
        227,41,1,0,0,0,228,226,1,0,0,0,229,231,5,22,0,0,230,229,1,0,0,0,
        230,231,1,0,0,0,231,232,1,0,0,0,232,233,5,12,0,0,233,238,3,36,18,
        0,234,236,5,17,0,0,235,234,1,0,0,0,235,236,1,0,0,0,236,237,1,0,0,
        0,237,239,3,36,18,0,238,235,1,0,0,0,238,239,1,0,0,0,239,242,1,0,
        0,0,240,241,5,13,0,0,241,243,3,44,22,0,242,240,1,0,0,0,242,243,1,
        0,0,0,243,43,1,0,0,0,244,245,3,34,17,0,245,246,3,60,30,0,246,254,
        3,34,17,0,247,248,3,58,29,0,248,249,3,34,17,0,249,250,3,60,30,0,
        250,251,3,34,17,0,251,253,1,0,0,0,252,247,1,0,0,0,253,256,1,0,0,
        0,254,252,1,0,0,0,254,255,1,0,0,0,255,45,1,0,0,0,256,254,1,0,0,0,
        257,259,5,16,0,0,258,260,5,15,0,0,259,258,1,0,0,0,259,260,1,0,0,
        0,260,47,1,0,0,0,261,267,3,50,25,0,262,263,3,58,29,0,263,264,3,50,
        25,0,264,266,1,0,0,0,265,262,1,0,0,0,266,269,1,0,0,0,267,265,1,0,
        0,0,267,268,1,0,0,0,268,49,1,0,0,0,269,267,1,0,0,0,270,281,3,54,
        27,0,271,272,3,26,13,0,272,276,5,18,0,0,273,277,5,20,0,0,274,275,
        5,19,0,0,275,277,5,20,0,0,276,273,1,0,0,0,276,274,1,0,0,0,277,281,
        1,0,0,0,278,281,3,52,26,0,279,281,3,56,28,0,280,270,1,0,0,0,280,
        271,1,0,0,0,280,278,1,0,0,0,280,279,1,0,0,0,281,51,1,0,0,0,282,283,
        3,26,13,0,283,284,3,60,30,0,284,285,3,32,16,0,285,53,1,0,0,0,286,
        287,3,26,13,0,287,288,3,60,30,0,288,289,3,62,31,0,289,55,1,0,0,0,
        290,291,3,26,13,0,291,292,5,26,0,0,292,293,3,64,32,0,293,294,5,23,
        0,0,294,295,3,64,32,0,295,57,1,0,0,0,296,297,7,1,0,0,297,59,1,0,
        0,0,298,299,7,2,0,0,299,61,1,0,0,0,300,301,5,43,0,0,301,302,5,31,
        0,0,302,305,5,43,0,0,303,305,3,64,32,0,304,300,1,0,0,0,304,303,1,
        0,0,0,305,63,1,0,0,0,306,307,5,32,0,0,307,65,1,0,0,0,38,69,75,78,
        81,84,87,90,95,98,101,112,133,140,145,149,156,161,165,169,174,180,
        187,191,196,200,208,211,226,230,235,238,242,254,259,267,276,280,
        304
    ]

class SelectSQLParser ( Parser ):

    grammarFileName = "SelectSQL.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'*'", "'SELECT'", "'FROM'", "'WHERE'", 
                     "'GROUP'", "'BY'", "'HAVING'", "'ORDER'", "'ASC'", 
                     "'DESC'", "';'", "'JOIN'", "'ON'", "'DISTINCT'", "'ALL'", 
                     "'UNION'", "'AS'", "'IS'", "'NOT'", "'NULL'", "<INVALID>", 
                     "<INVALID>", "'AND'", "'OR'", "'WITH'", "'BETWEEN'", 
                     "'LIMIT'", "'('", "')'", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "<INVALID>", "'<'", "'<='", "'>'", 
                     "'>='", "','", "'.'", "'&'", "'|'", "'\"'" ]

    symbolicNames = [ "<INVALID>", "ASTERISK", "SELECT", "FROM", "WHERE", 
                      "GROUP", "BY", "HAVING", "ORDER", "ASC", "DESC", "SEMICOLON", 
                      "JOIN", "ON", "DISTINCT", "ALL", "UNION", "AS", "IS", 
                      "NOT", "NULL", "AGGREGATE", "JOIN_TYPE", "AND", "OR", 
                      "WITH", "BETWEEN", "LIMIT", "LPAREN", "RPAREN", "STRING", 
                      "IDENTIFIER", "NUMBER", "EQ", "NE", "LT", "LTE", "GT", 
                      "GTE", "COMMA", "DOT", "AMP", "PIPE", "QT", "WS" ]

    RULE_select_statement = 0
    RULE_select_with_cte = 1
    RULE_select_clause = 2
    RULE_from_clause = 3
    RULE_where_clause = 4
    RULE_group_by_clause = 5
    RULE_having_clause = 6
    RULE_order_by_clause = 7
    RULE_limit_clause = 8
    RULE_column_name_list = 9
    RULE_modifier = 10
    RULE_select_list = 11
    RULE_select_item = 12
    RULE_expression = 13
    RULE_table_list = 14
    RULE_aggregate_function = 15
    RULE_subquery = 16
    RULE_table_column = 17
    RULE_table_name = 18
    RULE_column_name = 19
    RULE_join_list = 20
    RULE_join_clause = 21
    RULE_join_condition = 22
    RULE_union_clause = 23
    RULE_condition = 24
    RULE_logicalCondition = 25
    RULE_subqueryCondition = 26
    RULE_comparison_condition = 27
    RULE_between_condition = 28
    RULE_logical_operator = 29
    RULE_comparison_operator = 30
    RULE_value = 31
    RULE_number = 32

    ruleNames =  [ "select_statement", "select_with_cte", "select_clause", 
                   "from_clause", "where_clause", "group_by_clause", "having_clause", 
                   "order_by_clause", "limit_clause", "column_name_list", 
                   "modifier", "select_list", "select_item", "expression", 
                   "table_list", "aggregate_function", "subquery", "table_column", 
                   "table_name", "column_name", "join_list", "join_clause", 
                   "join_condition", "union_clause", "condition", "logicalCondition", 
                   "subqueryCondition", "comparison_condition", "between_condition", 
                   "logical_operator", "comparison_operator", "value", "number" ]

    EOF = Token.EOF
    ASTERISK=1
    SELECT=2
    FROM=3
    WHERE=4
    GROUP=5
    BY=6
    HAVING=7
    ORDER=8
    ASC=9
    DESC=10
    SEMICOLON=11
    JOIN=12
    ON=13
    DISTINCT=14
    ALL=15
    UNION=16
    AS=17
    IS=18
    NOT=19
    NULL=20
    AGGREGATE=21
    JOIN_TYPE=22
    AND=23
    OR=24
    WITH=25
    BETWEEN=26
    LIMIT=27
    LPAREN=28
    RPAREN=29
    STRING=30
    IDENTIFIER=31
    NUMBER=32
    EQ=33
    NE=34
    LT=35
    LTE=36
    GT=37
    GTE=38
    COMMA=39
    DOT=40
    AMP=41
    PIPE=42
    QT=43
    WS=44

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.0")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class Select_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Select_clauseContext,0)


        def from_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.From_clauseContext,0)


        def select_with_cte(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Select_with_cteContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Select_with_cteContext,i)


        def join_list(self):
            return self.getTypedRuleContext(SelectSQLParser.Join_listContext,0)


        def where_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Where_clauseContext,0)


        def group_by_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Group_by_clauseContext,0)


        def having_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Having_clauseContext,0)


        def order_by_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Order_by_clauseContext,0)


        def limit_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Limit_clauseContext,0)


        def union_clause(self):
            return self.getTypedRuleContext(SelectSQLParser.Union_clauseContext,0)


        def select_statement(self):
            return self.getTypedRuleContext(SelectSQLParser.Select_statementContext,0)


        def SEMICOLON(self):
            return self.getToken(SelectSQLParser.SEMICOLON, 0)

        def EOF(self):
            return self.getToken(SelectSQLParser.EOF, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_select_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_statement" ):
                listener.enterSelect_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_statement" ):
                listener.exitSelect_statement(self)




    def select_statement(self):

        localctx = SelectSQLParser.Select_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_select_statement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 69
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
            while _alt!=1 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1+1:
                    self.state = 66
                    self.select_with_cte() 
                self.state = 71
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

            self.state = 72
            self.select_clause()
            self.state = 73
            self.from_clause()
            self.state = 75
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==12 or _la==22:
                self.state = 74
                self.join_list()


            self.state = 78
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 77
                self.where_clause()


            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==5:
                self.state = 80
                self.group_by_clause()


            self.state = 84
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==7:
                self.state = 83
                self.having_clause()


            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==8:
                self.state = 86
                self.order_by_clause()


            self.state = 90
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==27:
                self.state = 89
                self.limit_clause()


            self.state = 95
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==16:
                self.state = 92
                self.union_clause()
                self.state = 93
                self.select_statement()


            self.state = 98
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(SelectSQLParser.SEMICOLON)


            self.state = 101
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 100
                self.match(SelectSQLParser.EOF)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_with_cteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WITH(self):
            return self.getToken(SelectSQLParser.WITH, 0)

        def column_name_list(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_name_listContext,0)


        def AS(self):
            return self.getToken(SelectSQLParser.AS, 0)

        def LPAREN(self):
            return self.getToken(SelectSQLParser.LPAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SelectSQLParser.Select_statementContext,0)


        def RPAREN(self):
            return self.getToken(SelectSQLParser.RPAREN, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_select_with_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_with_cte" ):
                listener.enterSelect_with_cte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_with_cte" ):
                listener.exitSelect_with_cte(self)




    def select_with_cte(self):

        localctx = SelectSQLParser.Select_with_cteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_select_with_cte)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 103
            self.match(SelectSQLParser.WITH)
            self.state = 104
            self.column_name_list()
            self.state = 105
            self.match(SelectSQLParser.AS)
            self.state = 106
            self.match(SelectSQLParser.LPAREN)
            self.state = 107
            self.select_statement()
            self.state = 108
            self.match(SelectSQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SELECT(self):
            return self.getToken(SelectSQLParser.SELECT, 0)

        def select_list(self):
            return self.getTypedRuleContext(SelectSQLParser.Select_listContext,0)


        def modifier(self):
            return self.getTypedRuleContext(SelectSQLParser.ModifierContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_select_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_clause" ):
                listener.enterSelect_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_clause" ):
                listener.exitSelect_clause(self)




    def select_clause(self):

        localctx = SelectSQLParser.Select_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_select_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(SelectSQLParser.SELECT)
            self.state = 112
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 111
                self.modifier()


            self.state = 114
            self.select_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class From_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FROM(self):
            return self.getToken(SelectSQLParser.FROM, 0)

        def table_list(self):
            return self.getTypedRuleContext(SelectSQLParser.Table_listContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_from_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFrom_clause" ):
                listener.enterFrom_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFrom_clause" ):
                listener.exitFrom_clause(self)




    def from_clause(self):

        localctx = SelectSQLParser.From_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_from_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SelectSQLParser.FROM)
            self.state = 117
            self.table_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Where_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHERE(self):
            return self.getToken(SelectSQLParser.WHERE, 0)

        def condition(self):
            return self.getTypedRuleContext(SelectSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_where_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhere_clause" ):
                listener.enterWhere_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhere_clause" ):
                listener.exitWhere_clause(self)




    def where_clause(self):

        localctx = SelectSQLParser.Where_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_where_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 119
            self.match(SelectSQLParser.WHERE)
            self.state = 120
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Group_by_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GROUP(self):
            return self.getToken(SelectSQLParser.GROUP, 0)

        def BY(self):
            return self.getToken(SelectSQLParser.BY, 0)

        def column_name_list(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_name_listContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_group_by_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGroup_by_clause" ):
                listener.enterGroup_by_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGroup_by_clause" ):
                listener.exitGroup_by_clause(self)




    def group_by_clause(self):

        localctx = SelectSQLParser.Group_by_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_group_by_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(SelectSQLParser.GROUP)
            self.state = 123
            self.match(SelectSQLParser.BY)
            self.state = 124
            self.column_name_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Having_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def HAVING(self):
            return self.getToken(SelectSQLParser.HAVING, 0)

        def condition(self):
            return self.getTypedRuleContext(SelectSQLParser.ConditionContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_having_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterHaving_clause" ):
                listener.enterHaving_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitHaving_clause" ):
                listener.exitHaving_clause(self)




    def having_clause(self):

        localctx = SelectSQLParser.Having_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_having_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.match(SelectSQLParser.HAVING)
            self.state = 127
            self.condition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Order_by_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ORDER(self):
            return self.getToken(SelectSQLParser.ORDER, 0)

        def BY(self):
            return self.getToken(SelectSQLParser.BY, 0)

        def column_name_list(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_name_listContext,0)


        def ASC(self):
            return self.getToken(SelectSQLParser.ASC, 0)

        def DESC(self):
            return self.getToken(SelectSQLParser.DESC, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_order_by_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrder_by_clause" ):
                listener.enterOrder_by_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrder_by_clause" ):
                listener.exitOrder_by_clause(self)




    def order_by_clause(self):

        localctx = SelectSQLParser.Order_by_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_order_by_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129
            self.match(SelectSQLParser.ORDER)
            self.state = 130
            self.match(SelectSQLParser.BY)
            self.state = 131
            self.column_name_list()
            self.state = 133
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9 or _la==10:
                self.state = 132
                _la = self._input.LA(1)
                if not(_la==9 or _la==10):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Limit_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LIMIT(self):
            return self.getToken(SelectSQLParser.LIMIT, 0)

        def number(self):
            return self.getTypedRuleContext(SelectSQLParser.NumberContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_limit_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLimit_clause" ):
                listener.enterLimit_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLimit_clause" ):
                listener.exitLimit_clause(self)




    def limit_clause(self):

        localctx = SelectSQLParser.Limit_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_limit_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(SelectSQLParser.LIMIT)
            self.state = 136
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_name_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Column_nameContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Column_nameContext,i)


        def table_column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Table_columnContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Table_columnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SelectSQLParser.COMMA)
            else:
                return self.getToken(SelectSQLParser.COMMA, i)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_column_name_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_name_list" ):
                listener.enterColumn_name_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_name_list" ):
                listener.exitColumn_name_list(self)




    def column_name_list(self):

        localctx = SelectSQLParser.Column_name_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_column_name_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 138
                self.column_name()
                pass

            elif la_ == 2:
                self.state = 139
                self.table_column()
                pass


            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 142
                self.match(SelectSQLParser.COMMA)
                self.state = 145
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 143
                    self.column_name()
                    pass

                elif la_ == 2:
                    self.state = 144
                    self.table_column()
                    pass


                self.state = 151
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ModifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISTINCT(self):
            return self.getToken(SelectSQLParser.DISTINCT, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_modifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModifier" ):
                listener.enterModifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModifier" ):
                listener.exitModifier(self)




    def modifier(self):

        localctx = SelectSQLParser.ModifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_modifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(SelectSQLParser.DISTINCT)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def select_item(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Select_itemContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Select_itemContext,i)


        def table_column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Table_columnContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Table_columnContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SelectSQLParser.COMMA)
            else:
                return self.getToken(SelectSQLParser.COMMA, i)

        def ASTERISK(self):
            return self.getToken(SelectSQLParser.ASTERISK, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_select_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_list" ):
                listener.enterSelect_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_list" ):
                listener.exitSelect_list(self)




    def select_list(self):

        localctx = SelectSQLParser.Select_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_select_list)
        self._la = 0 # Token type
        try:
            self.state = 169
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [21, 28, 31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 156
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 154
                    self.select_item()
                    pass

                elif la_ == 2:
                    self.state = 155
                    self.table_column()
                    pass


                self.state = 165
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 158
                    self.match(SelectSQLParser.COMMA)
                    self.state = 161
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                    if la_ == 1:
                        self.state = 159
                        self.select_item()
                        pass

                    elif la_ == 2:
                        self.state = 160
                        self.table_column()
                        pass


                    self.state = 167
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [1]:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.match(SelectSQLParser.ASTERISK)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Select_itemContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SelectSQLParser.ExpressionContext,0)


        def AS(self):
            return self.getToken(SelectSQLParser.AS, 0)

        def column_name(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_nameContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_select_item

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSelect_item" ):
                listener.enterSelect_item(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSelect_item" ):
                listener.exitSelect_item(self)




    def select_item(self):

        localctx = SelectSQLParser.Select_itemContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_select_item)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            self.expression()
            self.state = 174
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17:
                self.state = 172
                self.match(SelectSQLParser.AS)
                self.state = 173
                self.column_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def column_name(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_nameContext,0)


        def aggregate_function(self):
            return self.getTypedRuleContext(SelectSQLParser.Aggregate_functionContext,0)


        def subquery(self):
            return self.getTypedRuleContext(SelectSQLParser.SubqueryContext,0)


        def table_column(self):
            return self.getTypedRuleContext(SelectSQLParser.Table_columnContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)




    def expression(self):

        localctx = SelectSQLParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_expression)
        try:
            self.state = 180
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.column_name()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.aggregate_function()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 178
                self.subquery()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 179
                self.table_column()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Table_nameContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Table_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SelectSQLParser.COMMA)
            else:
                return self.getToken(SelectSQLParser.COMMA, i)

        def subquery(self):
            return self.getTypedRuleContext(SelectSQLParser.SubqueryContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_table_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_list" ):
                listener.enterTable_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_list" ):
                listener.exitTable_list(self)




    def table_list(self):

        localctx = SelectSQLParser.Table_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_table_list)
        self._la = 0 # Token type
        try:
            self.state = 191
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [31]:
                self.enterOuterAlt(localctx, 1)
                self.state = 182
                self.table_name()
                self.state = 187
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==39:
                    self.state = 183
                    self.match(SelectSQLParser.COMMA)
                    self.state = 184
                    self.table_name()
                    self.state = 189
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                pass
            elif token in [28]:
                self.enterOuterAlt(localctx, 2)
                self.state = 190
                self.subquery()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Aggregate_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGGREGATE(self):
            return self.getToken(SelectSQLParser.AGGREGATE, 0)

        def LPAREN(self):
            return self.getToken(SelectSQLParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(SelectSQLParser.RPAREN, 0)

        def column_name(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_nameContext,0)


        def table_column(self):
            return self.getTypedRuleContext(SelectSQLParser.Table_columnContext,0)


        def modifier(self):
            return self.getTypedRuleContext(SelectSQLParser.ModifierContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_aggregate_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAggregate_function" ):
                listener.enterAggregate_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAggregate_function" ):
                listener.exitAggregate_function(self)




    def aggregate_function(self):

        localctx = SelectSQLParser.Aggregate_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_aggregate_function)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            self.match(SelectSQLParser.AGGREGATE)
            self.state = 194
            self.match(SelectSQLParser.LPAREN)
            self.state = 196
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==14:
                self.state = 195
                self.modifier()


            self.state = 200
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.state = 198
                self.column_name()
                pass

            elif la_ == 2:
                self.state = 199
                self.table_column()
                pass


            self.state = 202
            self.match(SelectSQLParser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubqueryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(SelectSQLParser.LPAREN, 0)

        def select_statement(self):
            return self.getTypedRuleContext(SelectSQLParser.Select_statementContext,0)


        def RPAREN(self):
            return self.getToken(SelectSQLParser.RPAREN, 0)

        def table_name(self):
            return self.getTypedRuleContext(SelectSQLParser.Table_nameContext,0)


        def AS(self):
            return self.getToken(SelectSQLParser.AS, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_subquery

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubquery" ):
                listener.enterSubquery(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubquery" ):
                listener.exitSubquery(self)




    def subquery(self):

        localctx = SelectSQLParser.SubqueryContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_subquery)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(SelectSQLParser.LPAREN)
            self.state = 205
            self.select_statement()
            self.state = 206
            self.match(SelectSQLParser.RPAREN)
            self.state = 211
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 208
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 207
                    self.match(SelectSQLParser.AS)


                self.state = 210
                self.table_name()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_columnContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_name(self):
            return self.getTypedRuleContext(SelectSQLParser.Table_nameContext,0)


        def DOT(self):
            return self.getToken(SelectSQLParser.DOT, 0)

        def column_name(self):
            return self.getTypedRuleContext(SelectSQLParser.Column_nameContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_table_column

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_column" ):
                listener.enterTable_column(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_column" ):
                listener.exitTable_column(self)




    def table_column(self):

        localctx = SelectSQLParser.Table_columnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_table_column)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 213
            self.table_name()
            self.state = 214
            self.match(SelectSQLParser.DOT)
            self.state = 215
            self.column_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Table_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SelectSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_table_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTable_name" ):
                listener.enterTable_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTable_name" ):
                listener.exitTable_name(self)




    def table_name(self):

        localctx = SelectSQLParser.Table_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_table_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self.match(SelectSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Column_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(SelectSQLParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_column_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterColumn_name" ):
                listener.enterColumn_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitColumn_name" ):
                listener.exitColumn_name(self)




    def column_name(self):

        localctx = SelectSQLParser.Column_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_column_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(SelectSQLParser.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def join_clause(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Join_clauseContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Join_clauseContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(SelectSQLParser.COMMA)
            else:
                return self.getToken(SelectSQLParser.COMMA, i)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_join_list

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_list" ):
                listener.enterJoin_list(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_list" ):
                listener.exitJoin_list(self)




    def join_list(self):

        localctx = SelectSQLParser.Join_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_join_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.join_clause()
            self.state = 226
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==39:
                self.state = 222
                self.match(SelectSQLParser.COMMA)
                self.state = 223
                self.join_clause()
                self.state = 228
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def JOIN(self):
            return self.getToken(SelectSQLParser.JOIN, 0)

        def table_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Table_nameContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Table_nameContext,i)


        def JOIN_TYPE(self):
            return self.getToken(SelectSQLParser.JOIN_TYPE, 0)

        def ON(self):
            return self.getToken(SelectSQLParser.ON, 0)

        def join_condition(self):
            return self.getTypedRuleContext(SelectSQLParser.Join_conditionContext,0)


        def AS(self):
            return self.getToken(SelectSQLParser.AS, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_join_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_clause" ):
                listener.enterJoin_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_clause" ):
                listener.exitJoin_clause(self)




    def join_clause(self):

        localctx = SelectSQLParser.Join_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_join_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 230
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 229
                self.match(SelectSQLParser.JOIN_TYPE)


            self.state = 232
            self.match(SelectSQLParser.JOIN)
            self.state = 233
            self.table_name()
            self.state = 238
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==17 or _la==31:
                self.state = 235
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==17:
                    self.state = 234
                    self.match(SelectSQLParser.AS)


                self.state = 237
                self.table_name()


            self.state = 242
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 240
                self.match(SelectSQLParser.ON)
                self.state = 241
                self.join_condition()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Join_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def table_column(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Table_columnContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Table_columnContext,i)


        def comparison_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Comparison_operatorContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Comparison_operatorContext,i)


        def logical_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Logical_operatorContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Logical_operatorContext,i)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_join_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJoin_condition" ):
                listener.enterJoin_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJoin_condition" ):
                listener.exitJoin_condition(self)




    def join_condition(self):

        localctx = SelectSQLParser.Join_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_join_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 244
            self.table_column()
            self.state = 245
            self.comparison_operator()
            self.state = 246
            self.table_column()
            self.state = 254
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6597094932480) != 0):
                self.state = 247
                self.logical_operator()
                self.state = 248
                self.table_column()
                self.state = 249
                self.comparison_operator()
                self.state = 250
                self.table_column()
                self.state = 256
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Union_clauseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def UNION(self):
            return self.getToken(SelectSQLParser.UNION, 0)

        def ALL(self):
            return self.getToken(SelectSQLParser.ALL, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_union_clause

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnion_clause" ):
                listener.enterUnion_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnion_clause" ):
                listener.exitUnion_clause(self)




    def union_clause(self):

        localctx = SelectSQLParser.Union_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_union_clause)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 257
            self.match(SelectSQLParser.UNION)
            self.state = 259
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==15:
                self.state = 258
                self.match(SelectSQLParser.ALL)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def logicalCondition(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.LogicalConditionContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.LogicalConditionContext,i)


        def logical_operator(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.Logical_operatorContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.Logical_operatorContext,i)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition" ):
                listener.enterCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition" ):
                listener.exitCondition(self)




    def condition(self):

        localctx = SelectSQLParser.ConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_condition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.logicalCondition()
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 6597094932480) != 0):
                self.state = 262
                self.logical_operator()
                self.state = 263
                self.logicalCondition()
                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicalConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def comparison_condition(self):
            return self.getTypedRuleContext(SelectSQLParser.Comparison_conditionContext,0)


        def expression(self):
            return self.getTypedRuleContext(SelectSQLParser.ExpressionContext,0)


        def IS(self):
            return self.getToken(SelectSQLParser.IS, 0)

        def NULL(self):
            return self.getToken(SelectSQLParser.NULL, 0)

        def NOT(self):
            return self.getToken(SelectSQLParser.NOT, 0)

        def subqueryCondition(self):
            return self.getTypedRuleContext(SelectSQLParser.SubqueryConditionContext,0)


        def between_condition(self):
            return self.getTypedRuleContext(SelectSQLParser.Between_conditionContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_logicalCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogicalCondition" ):
                listener.enterLogicalCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogicalCondition" ):
                listener.exitLogicalCondition(self)




    def logicalCondition(self):

        localctx = SelectSQLParser.LogicalConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_logicalCondition)
        try:
            self.state = 280
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,36,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 270
                self.comparison_condition()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 271
                self.expression()
                self.state = 272
                self.match(SelectSQLParser.IS)
                self.state = 276
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [20]:
                    self.state = 273
                    self.match(SelectSQLParser.NULL)
                    pass
                elif token in [19]:
                    self.state = 274
                    self.match(SelectSQLParser.NOT)
                    self.state = 275
                    self.match(SelectSQLParser.NULL)
                    pass
                else:
                    raise NoViableAltException(self)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 278
                self.subqueryCondition()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 279
                self.between_condition()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SubqueryConditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SelectSQLParser.ExpressionContext,0)


        def comparison_operator(self):
            return self.getTypedRuleContext(SelectSQLParser.Comparison_operatorContext,0)


        def subquery(self):
            return self.getTypedRuleContext(SelectSQLParser.SubqueryContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_subqueryCondition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSubqueryCondition" ):
                listener.enterSubqueryCondition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSubqueryCondition" ):
                listener.exitSubqueryCondition(self)




    def subqueryCondition(self):

        localctx = SelectSQLParser.SubqueryConditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_subqueryCondition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 282
            self.expression()
            self.state = 283
            self.comparison_operator()
            self.state = 284
            self.subquery()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SelectSQLParser.ExpressionContext,0)


        def comparison_operator(self):
            return self.getTypedRuleContext(SelectSQLParser.Comparison_operatorContext,0)


        def value(self):
            return self.getTypedRuleContext(SelectSQLParser.ValueContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_comparison_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_condition" ):
                listener.enterComparison_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_condition" ):
                listener.exitComparison_condition(self)




    def comparison_condition(self):

        localctx = SelectSQLParser.Comparison_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_comparison_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 286
            self.expression()
            self.state = 287
            self.comparison_operator()
            self.state = 288
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Between_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SelectSQLParser.ExpressionContext,0)


        def BETWEEN(self):
            return self.getToken(SelectSQLParser.BETWEEN, 0)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SelectSQLParser.NumberContext)
            else:
                return self.getTypedRuleContext(SelectSQLParser.NumberContext,i)


        def AND(self):
            return self.getToken(SelectSQLParser.AND, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_between_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBetween_condition" ):
                listener.enterBetween_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBetween_condition" ):
                listener.exitBetween_condition(self)




    def between_condition(self):

        localctx = SelectSQLParser.Between_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_between_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 290
            self.expression()
            self.state = 291
            self.match(SelectSQLParser.BETWEEN)
            self.state = 292
            self.number()
            self.state = 293
            self.match(SelectSQLParser.AND)
            self.state = 294
            self.number()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Logical_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AND(self):
            return self.getToken(SelectSQLParser.AND, 0)

        def OR(self):
            return self.getToken(SelectSQLParser.OR, 0)

        def AMP(self):
            return self.getToken(SelectSQLParser.AMP, 0)

        def PIPE(self):
            return self.getToken(SelectSQLParser.PIPE, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_logical_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_operator" ):
                listener.enterLogical_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_operator" ):
                listener.exitLogical_operator(self)




    def logical_operator(self):

        localctx = SelectSQLParser.Logical_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_logical_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 296
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 6597094932480) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Comparison_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQ(self):
            return self.getToken(SelectSQLParser.EQ, 0)

        def NE(self):
            return self.getToken(SelectSQLParser.NE, 0)

        def LT(self):
            return self.getToken(SelectSQLParser.LT, 0)

        def LTE(self):
            return self.getToken(SelectSQLParser.LTE, 0)

        def GT(self):
            return self.getToken(SelectSQLParser.GT, 0)

        def GTE(self):
            return self.getToken(SelectSQLParser.GTE, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_comparison_operator

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparison_operator" ):
                listener.enterComparison_operator(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparison_operator" ):
                listener.exitComparison_operator(self)




    def comparison_operator(self):

        localctx = SelectSQLParser.Comparison_operatorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_comparison_operator)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 298
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 541165879296) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QT(self, i:int=None):
            if i is None:
                return self.getTokens(SelectSQLParser.QT)
            else:
                return self.getToken(SelectSQLParser.QT, i)

        def IDENTIFIER(self):
            return self.getToken(SelectSQLParser.IDENTIFIER, 0)

        def number(self):
            return self.getTypedRuleContext(SelectSQLParser.NumberContext,0)


        def getRuleIndex(self):
            return SelectSQLParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = SelectSQLParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_value)
        try:
            self.state = 304
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [43]:
                self.enterOuterAlt(localctx, 1)
                self.state = 300
                self.match(SelectSQLParser.QT)
                self.state = 301
                self.match(SelectSQLParser.IDENTIFIER)
                self.state = 302
                self.match(SelectSQLParser.QT)
                pass
            elif token in [32]:
                self.enterOuterAlt(localctx, 2)
                self.state = 303
                self.number()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMBER(self):
            return self.getToken(SelectSQLParser.NUMBER, 0)

        def getRuleIndex(self):
            return SelectSQLParser.RULE_number

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumber" ):
                listener.enterNumber(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumber" ):
                listener.exitNumber(self)




    def number(self):

        localctx = SelectSQLParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_number)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 306
            self.match(SelectSQLParser.NUMBER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





