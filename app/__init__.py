# pylint: disable=unnecessary-dunder-call, invalid-name, unnecessary-pass

'''
    Defines the Application which is a REPL defined to be an interactive calculator
'''

import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command

class App:
    '''
        The Application is a REPL defined to be an interactive calculator
    '''
    def __init__(self): # Constructor
        self.command_handler = CommandHandler()

    def load_plugins(self):
        '''
            # Dynamically load all plugins in the plugins directory
        '''
        plugins_package = 'app.plugins'
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_package.replace('.', '/')]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)) and item is not Command:  # Added extra condition as it was registering the command twice
                            if plugin_name == "menu":
                                self.command_handler.register_command(plugin_name, item(self.command_handler))
                            else:
                                self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        '''
            Registers all the commands to be used by the user and starts the REPL
            Exits the app when the user types 'exit'
        '''
        # Register commands here
        self.load_plugins()

        self.command_handler.list_commands()
        print("Type 'exit' to exit.")
        while True:  #REPL Read, Evaluate, Print, Loop
            self.command_handler.execute_command(input(">>> ").split())
