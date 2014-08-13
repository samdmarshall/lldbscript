import os
import lldb

class MachO():
    def commands(self):
        return {
            'arch': self.arch
        };
    
    
    def usage(self):
        print "MachO [arch]";
    
    
    def arch(self):
        print "architecture lookup";