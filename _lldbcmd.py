import lldb
import string


def execute_in_lldb(ignore_breakpoints, fetch_dynamic, timeout_value, all_threads, expr):
    frame = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame();
    if not frame:
        return 'error: invalid frame';
    expr_options = lldb.SBExpressionOptions();
    expr_options.SetIgnoreBreakpoints(ignore_breakpoints);
    expr_options.SetFetchDynamicValue(fetch_dynamic);
    expr_options.SetTimeoutInMicroSeconds(timeout_value*1000*1000); # N second timeout
    expr_options.SetTryAllThreads(all_threads);
    expr_sbvalue = frame.EvaluateExpression(expr, expr_options);
    if expr_sbvalue.error.Success():
        return lldb.value(expr_sbvalue);
    else:
        return expr_sbvalue.error;


def execute_command(cmd, name, evaltype, value):
    command = string.join(('command', cmd, name, evaltype, value), ' ');
    ci =  lldb.debugger.GetCommandInterpreter();    
    result = lldb.SBCommandReturnObject();
    ci.HandleCommand(command, result);