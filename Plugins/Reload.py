import _plugins
import _scripts


class Reload():
    def commands(self):
        return {
            'plugins': self.plugins,
            'scripts': self.scripts
        };
    
    
    def usage(self):
        print "Reload [plugins|scripts]";
    
    
    def plugins(self):
        _plugins.reload_plugins();
    
    
    def scripts(self):
        _scripts.reload_scripts();