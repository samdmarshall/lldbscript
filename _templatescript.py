import os
import _lldbcmd

SCRIPTS_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'Scripts');

def load_scripts(environment_dict):
    for script in os.listdir(SCRIPTS_PATH):
        if not script.startswith('.') and os.path.isfile(os.path.join(SCRIPTS_PATH, script)):
            script_name, script_extension = os.path.splitext(script)
            if not script_name in environment_dict:
                script_path = os.path.join(SCRIPTS_PATH, script);
                _lldbcmd.execute_command('script', '', 'import', script_path);