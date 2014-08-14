import _plugins
import _scripts
import string

class reload():
    def commands(self):
        return {
            'plugins': self.plugins,
            'scripts': self.scripts
        };
    
    
    def usage(self):
        return {
            'plugins': 'reloads plugins found in \'Plugins\' directory',
            'scripts': 'reloads scripts found in \'Scripts\' directory',
            'core': 'reloads dbscript core scripts'
        };
    
    
    def print_usage(self):
        usage_dict = self.usage();
        keys = usage_dict.keys();
        print '%s [%s]' % (type(self).__name__, string.join(keys, '|'));
        for key in keys:
            print '\t%s - %s' % (key, usage_dict[key]);
    
    
    def plugins(self, args):
        _plugins.load_plugins({});
    
    
    def scripts(self, args):
        _scripts.load_scripts({});
    
    
    def core(self, args):
        lldbscript.reload_scripts({});