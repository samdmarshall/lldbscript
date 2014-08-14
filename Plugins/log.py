import _lldbcmd
import string

class log():
    def commands(self):
        return {
            'po': self.print_object,
            'p': self.print_scalar
        };
    
    
    def usage(self):
        return {
            'po': 'print object',
            'p': 'print value'
        };
    
    
    def print_usage(self):
        usage_dict = self.usage();
        keys = usage_dict.keys();
        print '%s [%s]' % (type(self).__name__, string.join(keys, '|'));
        for key in keys:
            print '\t%s - %s' % (key, usage_dict[key]);
    
    
    def print_object(self, args):
        string_args = string.join(args, ' ');
        output_str = '';
        result = _lldbcmd.execute('po', string_args);
        if result.Succeeded() == True:
            output_str += result.GetOutput();
        else:
            output_str += '';
        print output_str;
    
    
    def print_scalar(self, args):
        string_args = string.join(args, ' ');
        output_str = '';
        result = _lldbcmd.execute('p', string_args);
        if result.Succeeded() == True:
            output_str += result.GetOutput();
        else:
            output_str += '';
        print output_str;