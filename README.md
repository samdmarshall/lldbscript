lldbscript
==========

lldbscript is a series of scripts that setup an environment that allow for easy debugging and implementing of new scripting functionality in lldb through the python APIs. I spent some time exploring how to easily interface with lldb through the embedded python scripting. This was intended to be a full scripting engine but at the moment the APIs for interacting with an existing instance of lldb (eg, from within xcode or launching lldb yourself) are lacking. So instead i've decided to release this as a way for people to drop in their own scripts and experiment with the APIs.


How To Install
==============


1. open terminal and run `touch .lldbinit`
2. open the `.lldbinit` file in a text editor and enter the following line:

	`command script import MY_PATH`

Where "MY_PATH" is the path to the lldbscript.py file. If you have existing script files loaded here, you can also place them into the /Scripts/ directory of lldbscript and they will get automatically loaded when lldbscript is loaded.


How To Use
==========

0) Restart Xcode

1) Start a new debugger instance, either through Build+Run in Xcode or starting lldb from the command line.

2) enter `dbscript` or `dbscript help`

This should print a list of loaded plugins. If you have lldbscript load other scripts for you they will not appear in this list.
	
3) To get information on a particular plugin enter `dbscript <plugin name>` and it will print the usage information about the plugin.


Writing Plugins
===============

In the "Plugins" directory there is a template called "template_plugin.py". This is the template for creating a new plugin for lldbscript.
