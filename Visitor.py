import os
from parser.SASVisitor import SASVisitor
import statsmodels as sm
import numpy as np
import pandas as pd


class Visitor(SASVisitor):

    # Visit a parse tree produced by SASVisitor#parse.
    def visitParse(self, ctx: SASVisitor.ParseContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#abort_stmt.
    def visitAbort_stmt(self, ctx: SASVisitor.Abort_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#file_spec.
    def visitFile_spec(self, ctx: SASVisitor.File_specContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#array_stmt.
    def visitArray_stmt(self, ctx: SASVisitor.Array_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#array_name.
    def visitArray_name(self, ctx: SASVisitor.Array_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#array_subscript.
    def visitArray_subscript(self, ctx: SASVisitor.Array_subscriptContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#array_elements.
    def visitArray_elements(self, ctx: SASVisitor.Array_elementsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#initial_value_list.
    def visitInitial_value_list(self, ctx: SASVisitor.Initial_value_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#initial_value_list_item.
    def visitInitial_value_list_item(self, ctx: SASVisitor.Initial_value_list_itemContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#initial_value_list_bk.
    def visitInitial_value_list_bk(self, ctx: SASVisitor.Initial_value_list_bkContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#constant_iter_value.
    def visitConstant_iter_value(self, ctx: SASVisitor.Constant_iter_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#constant_value.
    def visitConstant_value(self, ctx: SASVisitor.Constant_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#assign_stmt.
    def visitAssign_stmt(self, ctx: SASVisitor.Assign_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#by_stmt.
    def visitBy_stmt(self, ctx: SASVisitor.By_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#call_stmt.
    def visitCall_stmt(self, ctx: SASVisitor.Call_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#data_stmt.
    def visitData_stmt(self, ctx: SASVisitor.Data_stmtContext):
        print(f"Visiting data_stmt with context: {ctx}")
        dataset_name = ctx.dataset_name().getText()
        dataset_array = np.array([dataset_name])
        print(f"Dataset name: {dataset_name}")
        print(f"NumPy array created: {dataset_array}")
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#dataset_name_opt.
    def visitDataset_name_opt(self, ctx: SASVisitor.Dataset_name_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#datastmt_cmd.
    def visitDatastmt_cmd(self, ctx: SASVisitor.Datastmt_cmdContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#view_dsname_opt.
    def visitView_dsname_opt(self, ctx: SASVisitor.View_dsname_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#view_name.
    def visitView_name(self, ctx: SASVisitor.View_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#dataset_name.
    def visitDataset_name(self, ctx: SASVisitor.Dataset_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#program_name.
    def visitProgram_name(self, ctx: SASVisitor.Program_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#passwd_opt.
    def visitPasswd_opt(self, ctx: SASVisitor.Passwd_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#source_opt.
    def visitSource_opt(self, ctx: SASVisitor.Source_optContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#datalines_stmt.
    def visitDatalines_stmt(self, ctx: SASVisitor.Datalines_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#datalines4_stmt.
    def visitDatalines4_stmt(self, ctx: SASVisitor.Datalines4_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#drop_stmt.
    def visitDrop_stmt(self, ctx: SASVisitor.Drop_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#infile_stmt.
    def visitInfile_stmt(self, ctx: SASVisitor.Infile_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#file_specification.
    def visitFile_specification(self, ctx: SASVisitor.File_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#device_type.
    def visitDevice_type(self, ctx: SASVisitor.Device_typeContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#infile_options.
    def visitInfile_options(self, ctx: SASVisitor.Infile_optionsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#input_stmt.
    def visitInput_stmt(self, ctx: SASVisitor.Input_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#put_stmt.
    def visitPut_stmt(self, ctx: SASVisitor.Put_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#input_specification.
    def visitInput_specification(self, ctx: SASVisitor.Input_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#put_specification.
    def visitPut_specification(self, ctx: SASVisitor.Put_specificationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#pointer_control.
    def visitPointer_control(self, ctx: SASVisitor.Pointer_controlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#informat_list.
    def visitInformat_list(self, ctx: SASVisitor.Informat_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#input_variable_format.
    def visitInput_variable_format(self, ctx: SASVisitor.Input_variable_formatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#input_variable.
    def visitInput_variable(self, ctx: SASVisitor.Input_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#put_variable_format.
    def visitPut_variable_format(self, ctx: SASVisitor.Put_variable_formatContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#put_variable.
    def visitPut_variable(self, ctx: SASVisitor.Put_variableContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#column_point_control.
    def visitColumn_point_control(self, ctx: SASVisitor.Column_point_controlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#line_point_control.
    def visitLine_point_control(self, ctx: SASVisitor.Line_point_controlContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#format_modifier.
    def visitFormat_modifier(self, ctx: SASVisitor.Format_modifierContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#column_specifications.
    def visitColumn_specifications(self, ctx: SASVisitor.Column_specificationsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#means_proc.
    def visitMeans_proc(self, ctx: SASVisitor.Means_procContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#proc_stmt.
    def visitProc_stmt(self, ctx: SASVisitor.Proc_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#proc_name.
    def visitProc_name(self, ctx: SASVisitor.Proc_nameContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#run_stmt.
    def visitRun_stmt(self, ctx: SASVisitor.Run_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#sas_stmt_list.
    def visitSas_stmt_list(self, ctx: SASVisitor.Sas_stmt_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#if_stmt.
    def visitIf_stmt(self, ctx: SASVisitor.If_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#if_then_else_stmt.
    def visitIf_then_else_stmt(self, ctx: SASVisitor.If_then_else_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#delete_stmt.
    def visitDelete_stmt(self, ctx: SASVisitor.Delete_stmtContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#expression.
    def visitExpression(self, ctx: SASVisitor.ExpressionContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#expressionList.
    def visitExpressionList(self, ctx: SASVisitor.ExpressionListContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#of_var_list.
    def visitOf_var_list(self, ctx: SASVisitor.Of_var_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#identifiers_list.
    def visitIdentifiers_list(self, ctx: SASVisitor.Identifiers_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#in_var_list.
    def visitIn_var_list(self, ctx: SASVisitor.In_var_listContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#colonInts.
    def visitColonInts(self, ctx: SASVisitor.ColonIntsContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#literal.
    def visitLiteral(self, ctx: SASVisitor.LiteralContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by SASVisitor#variables.
    def visitVariables(self, ctx: SASVisitor.VariablesContext):
        return self.visitChildren(ctx)
