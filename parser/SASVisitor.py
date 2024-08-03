# Generated from SAS.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .SASParser import SASParser
else:
    from SASParser import SASParser


# This class defines a complete generic visitor for a parse tree produced by SASParser.

class SASVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by SASParser#parse.
    def visitParse(self, ctx: SASParser.ParseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#abort_stmt.
    def visitAbort_stmt(self, ctx: SASParser.Abort_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#file_spec.
    def visitFile_spec(self, ctx: SASParser.File_specContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#array_stmt.
    def visitArray_stmt(self, ctx: SASParser.Array_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#array_name.
    def visitArray_name(self, ctx: SASParser.Array_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#array_subscript.
    def visitArray_subscript(self, ctx: SASParser.Array_subscriptContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#array_elements.
    def visitArray_elements(self, ctx: SASParser.Array_elementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#initial_value_list.
    def visitInitial_value_list(self, ctx: SASParser.Initial_value_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#initial_value_list_item.
    def visitInitial_value_list_item(self, ctx: SASParser.Initial_value_list_itemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#initial_value_list_bk.
    def visitInitial_value_list_bk(self, ctx: SASParser.Initial_value_list_bkContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#constant_iter_value.
    def visitConstant_iter_value(self, ctx: SASParser.Constant_iter_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#constant_value.
    def visitConstant_value(self, ctx: SASParser.Constant_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#assign_stmt.
    def visitAssign_stmt(self, ctx: SASParser.Assign_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#by_stmt.
    def visitBy_stmt(self, ctx: SASParser.By_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#call_stmt.
    def visitCall_stmt(self, ctx: SASParser.Call_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#data_stmt.
    def visitData_stmt(self, ctx: SASParser.Data_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#dataset_name_opt.
    def visitDataset_name_opt(self, ctx: SASParser.Dataset_name_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#datastmt_cmd.
    def visitDatastmt_cmd(self, ctx: SASParser.Datastmt_cmdContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#view_dsname_opt.
    def visitView_dsname_opt(self, ctx: SASParser.View_dsname_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#view_name.
    def visitView_name(self, ctx: SASParser.View_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#dataset_name.
    def visitDataset_name(self, ctx: SASParser.Dataset_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#program_name.
    def visitProgram_name(self, ctx: SASParser.Program_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#passwd_opt.
    def visitPasswd_opt(self, ctx: SASParser.Passwd_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#source_opt.
    def visitSource_opt(self, ctx: SASParser.Source_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#datalines_stmt.
    def visitDatalines_stmt(self, ctx: SASParser.Datalines_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#datalines4_stmt.
    def visitDatalines4_stmt(self, ctx: SASParser.Datalines4_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#do_stmt.
    def visitDo_stmt(self, ctx: SASParser.Do_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#do_by_stmt.
    def visitDo_by_stmt(self, ctx: SASParser.Do_by_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#do_while_stmt.
    def visitDo_while_stmt(self, ctx: SASParser.Do_while_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#do_until_stmt.
    def visitDo_until_stmt(self, ctx: SASParser.Do_until_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#drop_stmt.
    def visitDrop_stmt(self, ctx: SASParser.Drop_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#infile_stmt.
    def visitInfile_stmt(self, ctx: SASParser.Infile_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#file_specification.
    def visitFile_specification(self, ctx: SASParser.File_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#device_type.
    def visitDevice_type(self, ctx: SASParser.Device_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#infile_options.
    def visitInfile_options(self, ctx: SASParser.Infile_optionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#input_stmt.
    def visitInput_stmt(self, ctx: SASParser.Input_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#put_stmt.
    def visitPut_stmt(self, ctx: SASParser.Put_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#input_specification.
    def visitInput_specification(self, ctx: SASParser.Input_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#put_specification.
    def visitPut_specification(self, ctx: SASParser.Put_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#pointer_control.
    def visitPointer_control(self, ctx: SASParser.Pointer_controlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#informat_list.
    def visitInformat_list(self, ctx: SASParser.Informat_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#input_variable_format.
    def visitInput_variable_format(self, ctx: SASParser.Input_variable_formatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#input_variable.
    def visitInput_variable(self, ctx: SASParser.Input_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#put_variable_format.
    def visitPut_variable_format(self, ctx: SASParser.Put_variable_formatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#put_variable.
    def visitPut_variable(self, ctx: SASParser.Put_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#column_point_control.
    def visitColumn_point_control(self, ctx: SASParser.Column_point_controlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#line_point_control.
    def visitLine_point_control(self, ctx: SASParser.Line_point_controlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#format_modifier.
    def visitFormat_modifier(self, ctx: SASParser.Format_modifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#column_specifications.
    def visitColumn_specifications(self, ctx: SASParser.Column_specificationsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#means_proc.
    def visitMeans_proc(self, ctx: SASParser.Means_procContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#proc_stmt.
    def visitProc_stmt(self, ctx: SASParser.Proc_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#proc_name.
    def visitProc_name(self, ctx: SASParser.Proc_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#run_stmt.
    def visitRun_stmt(self, ctx: SASParser.Run_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#sas_stmt_list.
    def visitSas_stmt_list(self, ctx: SASParser.Sas_stmt_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#if_stmt.
    def visitIf_stmt(self, ctx: SASParser.If_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#if_then_else_stmt.
    def visitIf_then_else_stmt(self, ctx: SASParser.If_then_else_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#delete_stmt.
    def visitDelete_stmt(self, ctx: SASParser.Delete_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#expression.
    def visitExpression(self, ctx: SASParser.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#expressionList.
    def visitExpressionList(self, ctx: SASParser.ExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#of_var_list.
    def visitOf_var_list(self, ctx: SASParser.Of_var_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#identifiers_list.
    def visitIdentifiers_list(self, ctx: SASParser.Identifiers_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#in_var_list.
    def visitIn_var_list(self, ctx: SASParser.In_var_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#colonInts.
    def visitColonInts(self, ctx: SASParser.ColonIntsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#literal.
    def visitLiteral(self, ctx: SASParser.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASParser#variables.
    def visitVariables(self, ctx: SASParser.VariablesContext):
        return self.visitChildren(ctx)


del SASParser
