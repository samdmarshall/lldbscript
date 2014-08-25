# This is a template class!
#
# CLASSNAME needs to be the same as the file name, this is case sensitive in the script engine
#
# Everything listed below is an example of how to create a plugin, the methods 'commands', 'usage', and 'print_usage' are required, you add the rest of the functionality.
#
# commands():
#   this method defines the keywords used by this plugin to trigger actions. This returns a dictionary where the keys are the argument strings  
#   and the values are the function pointers as to what should be called.
#
# usage():
#   This method is used to define the help/usage description for the plugin. This returns a dictionary where the keys are the same as those used
#   in commands(), and the values are strings that give a brief description of what each option does.
#
# print_usage():
#   This method is used to display the help/usage descriptions onscreen. This should not be modified.
#
#
#
#import string
#
#class CLASSNAME():
#    def commands(self):
#        return {
#            'COMMAND1': self.foo,
#            'COMMAND2': self.bar,
#			 'COMMAND3': self.baz
#        };
#    
#    
#    def usage(self):
#        return {
#            'COMMAND1': 'foo',
#            'COMMAND2': 'bar',
#            'COMMAND3': 'baz'
#        };
#    
#    
#    def print_usage(self):
#        usage_dict = self.usage();
#        keys = usage_dict.keys();
#        print '%s [%s]' % (self.__class__.__name__, string.join(keys, '|'));
#        for key in keys:
#            print '\t%s - %s' % (key, usage_dict[key]);
#    
#    
#    def foo(self, args):
#        print 'foo';
#    
#    
#    def bar(self, args):
#        print 'bar';
#    
#    
#    def baz(self, args):
#        print 'baz';