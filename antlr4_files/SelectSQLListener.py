# Generated from SelectSQL.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .SelectSQLParser import SelectSQLParser
else:
    from SelectSQLParser import SelectSQLParser

# This class defines a complete listener for a parse tree produced by SelectSQLParser.
class SelectSQLListener(ParseTreeListener):

    # Enter a parse tree produced by SelectSQLParser#select_statement.
    def enterSelect_statement(self, ctx:SelectSQLParser.Select_statementContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#select_statement.
    def exitSelect_statement(self, ctx:SelectSQLParser.Select_statementContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#select_with_cte.
    def enterSelect_with_cte(self, ctx:SelectSQLParser.Select_with_cteContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#select_with_cte.
    def exitSelect_with_cte(self, ctx:SelectSQLParser.Select_with_cteContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#select_clause.
    def enterSelect_clause(self, ctx:SelectSQLParser.Select_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#select_clause.
    def exitSelect_clause(self, ctx:SelectSQLParser.Select_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#from_clause.
    def enterFrom_clause(self, ctx:SelectSQLParser.From_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#from_clause.
    def exitFrom_clause(self, ctx:SelectSQLParser.From_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#where_clause.
    def enterWhere_clause(self, ctx:SelectSQLParser.Where_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#where_clause.
    def exitWhere_clause(self, ctx:SelectSQLParser.Where_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#group_by_clause.
    def enterGroup_by_clause(self, ctx:SelectSQLParser.Group_by_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#group_by_clause.
    def exitGroup_by_clause(self, ctx:SelectSQLParser.Group_by_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#having_clause.
    def enterHaving_clause(self, ctx:SelectSQLParser.Having_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#having_clause.
    def exitHaving_clause(self, ctx:SelectSQLParser.Having_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#order_by_clause.
    def enterOrder_by_clause(self, ctx:SelectSQLParser.Order_by_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#order_by_clause.
    def exitOrder_by_clause(self, ctx:SelectSQLParser.Order_by_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#limit_clause.
    def enterLimit_clause(self, ctx:SelectSQLParser.Limit_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#limit_clause.
    def exitLimit_clause(self, ctx:SelectSQLParser.Limit_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#column_name_list.
    def enterColumn_name_list(self, ctx:SelectSQLParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#column_name_list.
    def exitColumn_name_list(self, ctx:SelectSQLParser.Column_name_listContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#modifier.
    def enterModifier(self, ctx:SelectSQLParser.ModifierContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#modifier.
    def exitModifier(self, ctx:SelectSQLParser.ModifierContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#select_list.
    def enterSelect_list(self, ctx:SelectSQLParser.Select_listContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#select_list.
    def exitSelect_list(self, ctx:SelectSQLParser.Select_listContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#select_item.
    def enterSelect_item(self, ctx:SelectSQLParser.Select_itemContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#select_item.
    def exitSelect_item(self, ctx:SelectSQLParser.Select_itemContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#expression.
    def enterExpression(self, ctx:SelectSQLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#expression.
    def exitExpression(self, ctx:SelectSQLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#table_list.
    def enterTable_list(self, ctx:SelectSQLParser.Table_listContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#table_list.
    def exitTable_list(self, ctx:SelectSQLParser.Table_listContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#aggregate_function.
    def enterAggregate_function(self, ctx:SelectSQLParser.Aggregate_functionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#aggregate_function.
    def exitAggregate_function(self, ctx:SelectSQLParser.Aggregate_functionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#subquery.
    def enterSubquery(self, ctx:SelectSQLParser.SubqueryContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#subquery.
    def exitSubquery(self, ctx:SelectSQLParser.SubqueryContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#table_column.
    def enterTable_column(self, ctx:SelectSQLParser.Table_columnContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#table_column.
    def exitTable_column(self, ctx:SelectSQLParser.Table_columnContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#table_name.
    def enterTable_name(self, ctx:SelectSQLParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#table_name.
    def exitTable_name(self, ctx:SelectSQLParser.Table_nameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#column_name.
    def enterColumn_name(self, ctx:SelectSQLParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#column_name.
    def exitColumn_name(self, ctx:SelectSQLParser.Column_nameContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#join_list.
    def enterJoin_list(self, ctx:SelectSQLParser.Join_listContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#join_list.
    def exitJoin_list(self, ctx:SelectSQLParser.Join_listContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#join_clause.
    def enterJoin_clause(self, ctx:SelectSQLParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#join_clause.
    def exitJoin_clause(self, ctx:SelectSQLParser.Join_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#join_condition.
    def enterJoin_condition(self, ctx:SelectSQLParser.Join_conditionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#join_condition.
    def exitJoin_condition(self, ctx:SelectSQLParser.Join_conditionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#union_clause.
    def enterUnion_clause(self, ctx:SelectSQLParser.Union_clauseContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#union_clause.
    def exitUnion_clause(self, ctx:SelectSQLParser.Union_clauseContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#condition.
    def enterCondition(self, ctx:SelectSQLParser.ConditionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#condition.
    def exitCondition(self, ctx:SelectSQLParser.ConditionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#logicalCondition.
    def enterLogicalCondition(self, ctx:SelectSQLParser.LogicalConditionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#logicalCondition.
    def exitLogicalCondition(self, ctx:SelectSQLParser.LogicalConditionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#subqueryCondition.
    def enterSubqueryCondition(self, ctx:SelectSQLParser.SubqueryConditionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#subqueryCondition.
    def exitSubqueryCondition(self, ctx:SelectSQLParser.SubqueryConditionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#comparison_condition.
    def enterComparison_condition(self, ctx:SelectSQLParser.Comparison_conditionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#comparison_condition.
    def exitComparison_condition(self, ctx:SelectSQLParser.Comparison_conditionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#between_condition.
    def enterBetween_condition(self, ctx:SelectSQLParser.Between_conditionContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#between_condition.
    def exitBetween_condition(self, ctx:SelectSQLParser.Between_conditionContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#logical_operator.
    def enterLogical_operator(self, ctx:SelectSQLParser.Logical_operatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#logical_operator.
    def exitLogical_operator(self, ctx:SelectSQLParser.Logical_operatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#comparison_operator.
    def enterComparison_operator(self, ctx:SelectSQLParser.Comparison_operatorContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#comparison_operator.
    def exitComparison_operator(self, ctx:SelectSQLParser.Comparison_operatorContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#value.
    def enterValue(self, ctx:SelectSQLParser.ValueContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#value.
    def exitValue(self, ctx:SelectSQLParser.ValueContext):
        pass


    # Enter a parse tree produced by SelectSQLParser#number.
    def enterNumber(self, ctx:SelectSQLParser.NumberContext):
        pass

    # Exit a parse tree produced by SelectSQLParser#number.
    def exitNumber(self, ctx:SelectSQLParser.NumberContext):
        pass



del SelectSQLParser