import _environment


class DebugLog():
    def commands(self):
        return {
            'on': self.enable, 
            'off': self.disable
        };
    
    
    def usage(self):
        print "DebugLog [on|off]";
    
    
    def enable(self):
        _environment.set_variable('DEBUG_LOG_ENABLED', str(True));
    
    
    def disable(self):
        _environment.set_variable('DEBUG_LOG_ENABLED', str(False));