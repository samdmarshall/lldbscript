import _lldbcmd
import _print
import string

class reveal():
    def commands(self):
        return {
            'load': self.load_reveal,
            'start': self.start_reveal,
			'stop': self.stop_reveal
        };
    
    
    def usage(self):
        return {
            'load': 'loads reveal.dylib into your app (works for device and simulator, NOTE: libReveal.dylib must be on the device already, on iOS 8 you will need to weak link it against your app for it to load)',
            'start': 'starts the reveal service',
            'stop': 'stops the reveal service'
        };
    
    
    def print_usage(self):
        usage_dict = self.usage();
        keys = usage_dict.keys();
        print '%s [%s]' % (type(self).__name__, string.join(keys, '|'));
        for key in keys:
            print '\t%s - %s' % (key, usage_dict[key]);
    
    
    def load_reveal(self, args):
        location = int(str(execute_in_lldb(True, lldb.eNoDynamicValues, 3, False, '((NSRange)[(NSString *)[[UIDevice currentDevice] model] rangeOfString:@"Simulator"]).location')).split(' ')[-1]);
        if location == 2147483647:
            _print.debuglog([_print.Colour('cyan',True), _print.String('%s', 'Loading on Device...'), _print.Colour('reset', True)]);
            _lldbcmd.execute('expr', '(void*)dlopen([(NSString*)[(NSBundle*)[NSBundle mainBundle] pathForResource:@"libReveal" ofType:@"dylib"] cStringUsingEncoding:0x4], 0x2);');
        else:
            _print.debuglog([_print.Colour('cyan',True), _print.String('%s', 'Loading on Simulator...'), _print.Colour('reset', True)]);
            _lldbcmd.execute('expr', '(void*)dlopen("/Applications/Reveal.app/Contents/SharedSupport/iOS-Libraries/libReveal.dylib", 0x2);');
    
    
    def start_reveal(self, args):
        _lldbcmd.execute('expr', '(void)[(NSNotificationCenter*)[NSNotificationCenter defaultCenter] postNotificationName:@"IBARevealRequestStart" object:nil];');
    
    
    def stop_reveal(self, args):
        _lldbcmd.execute('expr', '(void)[(NSNotificationCenter*)[NSNotificationCenter defaultCenter] postNotificationName:@"IBARevealRequestStop" object:nil];');