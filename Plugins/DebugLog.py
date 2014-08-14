import _environment
import string


class debuglog():
    def commands(self):
        return {
            'on': self.enable, 
            'off': self.disable
        };
    
    
    def usage(self):
        return {
            'on': 'enables debug logging',
            'off': 'disables debug logging'
        };
    
    
    def print_usage(self):
        usage_dict = self.usage();
        keys = usage_dict.keys();
        print '%s [%s]' % (type(self).__name__, string.join(keys, '|'));
        for key in keys:
            print '\t%s - %s' % (key, usage_dict[key]);
    
    
    def enable(self):
        _environment.set_variable(_environment.debug_log_key(), str(True));
    
    
    def disable(self):
        _environment.set_variable(_environment.debug_log_key(), str(False));