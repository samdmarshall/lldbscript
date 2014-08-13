#!/usr/bin/python

import lldb
import commands
import shlex
import os
import subprocess

# expressions
find_if_sim = '((NSRange)[(NSString *)[[UIDevice currentDevice] model] rangeOfString:@"Simulator"]).location'
get_app_container = '(char*)[(NSString*)[(NSBundle*)[NSBundle mainBundle] bundlePath] UTF8String]'
load_reveal_sim = 'command alias reveal_load_sim expr (void*)dlopen("/Applications/Reveal.app/Contents/SharedSupport/iOS-Libraries/libReveal.dylib", 0x2);'
load_reveal_device =  'command alias reveal_load_dev expr (void*)dlopen([(NSString*)[(NSBundle*)[NSBundle mainBundle] pathForResource:@"libReveal" ofType:@"dylib"] cStringUsingEncoding:0x4], 0x2);' #'command alias reveal_load_dev expr (void*)dlopen([(NSString*)[((NSArray *)NSSearchPathForDirectoriesInDomains(9, 1, YES))[0] stringByAppendingPathComponent:@"libReveal.dylib"] cStringUsingEncoding:0x4], 0x2);'
start_reveal = 'command alias reveal_start expr (void)[(NSNotificationCenter*)[NSNotificationCenter defaultCenter] postNotificationName:@"IBARevealRequestStart" object:nil];'
stop_reveal = 'command alias reveal_stop expr (void)[(NSNotificationCenter*)[NSNotificationCenter defaultCenter] postNotificationName:@"IBARevealRequestStop" object:nil];'

def __lldb_init_module(debugger, internal_dict):
    print 'Loading debugging scripting commands...'
    debugger.HandleCommand('command script add -f reveal_loader.load_commands reveal')
    debugger.HandleCommand(load_reveal_sim)
    debugger.HandleCommand(load_reveal_device)
    debugger.HandleCommand(start_reveal)
    debugger.HandleCommand(stop_reveal)
    print 'Finished!'


def create_command_arguments(command):
	return shlex.split(command)


def execute_in_lldb(ignore_breakpoints, fetch_dynamic, timeout_value, all_threads, expr):
    frame = lldb.debugger.GetSelectedTarget().GetProcess().GetSelectedThread().GetSelectedFrame()
    if not frame:
        return 'error: invalid frame'
    
    expr_options = lldb.SBExpressionOptions()
    expr_options.SetIgnoreBreakpoints(ignore_breakpoints);
    expr_options.SetFetchDynamicValue(fetch_dynamic);
    expr_options.SetTimeoutInMicroSeconds(timeout_value*1000*1000) # N second timeout
    expr_options.SetTryAllThreads(all_threads)
    expr_sbvalue = frame.EvaluateExpression(expr, expr_options)
    if expr_sbvalue.error.Success():
        return lldb.value(expr_sbvalue)
    else:
        return expr_sbvalue.error


def find_app(command): 
    
    was_loaded = 0
    
    location = int(str(execute_in_lldb(True, lldb.eNoDynamicValues, 3, False, find_if_sim)).split(' ')[-1])
    
    print 'Signing libReveal.dylib...'
    run_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "reveal_loader")
    
    codesign_reveal_args = (run_path, "-s")
    codesign_reveal_popen = subprocess.Popen(codesign_reveal_args, stdout=subprocess.PIPE)
    codesign_reveal_popen.wait()
    codesign_reveal_output = codesign_reveal_popen.stdout.read()
    
    if location == 2147483647:
        container_path = str(str(execute_in_lldb(True, lldb.eNoDynamicValues, 3, False, get_app_container)).split(' ')[-1])[1:-1]
        
        exec_path = str(lldb.debugger.GetSelectedTarget().GetExecutable())
    
        print 'Copying to device...'
        print run_path + ' ' + '-d' + ' ' + exec_path + ' ' + container_path
        revealer_args = (run_path, '-d', exec_path, container_path)
        revealer_popen = subprocess.Popen(revealer_args, stdout=subprocess.PIPE)
        revealer_popen.wait()
        revealer_output = revealer_popen.stdout.read()
    
        print 'Loading on device...'
        was_loaded = lldb.debugger.HandleCommand('reveal_load_dev')
    else:
        print 'Loading on simulator...'
        was_loaded = lldb.debugger.HandleCommand('reveal_load_sim')
    
    if was_loaded != 0:
        print 'Starting Reveal...'
        lldb.debugger.HandleCommand('reveal_start')
    else:
        print 'There was an error loading Reveal!'
    

def usage():
    print "reveal_loader.py Commands:"
    print "      help -- displays this info"
    print "      load -- loads reveal library onto iOS device or simulator and starts"
    print "     start -- starts the reveal library"
    print "      stop -- stops the reveal library"


def load_commands(debugger, command, result, internal_dict):
    cmd_args = create_command_arguments(command)
    if len(cmd_args) == 1 and cmd_args[0] == 'load':
        find_app(cmd_args)
    elif len(cmd_args) == 1 and cmd_args[0] == 'start':
        lldb.debugger.HandleCommand('reveal_start')
    elif len(cmd_args) == 1 and cmd_args[0] == 'stop':
        lldb.debugger.HandleCommand('reveal_stop')
    else:
        usage()