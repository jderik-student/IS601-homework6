# pylint: disable=unnecessary-dunder-call, invalid-name, unnecessary-pass

'''
    Defines the Application which is a REPL defined to be an interactive calculator
'''

import logging
import logging.config
import os
import pkgutil
import importlib
import sys
from icecream import ic
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command

class App:
    '''
        The Application is a REPL defined to be an interactive calculator
    '''
    def __init__(self): # Constructor
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        if self.get_environment_variable("ENVIRONMENT") == "DEV": # pragma: no cover
            logger = logging.getLogger()
            logger.setLevel(logging.DEBUG)
            for handler in logger.handlers:
                handler.setLevel(logging.DEBUG)
            logging.debug("Logging level set to DEBUG")
        self.command_handler = CommandHandler()

    def configure_logging(self):
        '''
            Configures logging
        '''
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else: # pragma: no cover
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

        logging.info("Logging configured")

    def load_environment_variables(self):
        '''
            Loads environment variables from .env file
        '''
        settings = {key: value for key, value in os.environ.items()}
        logging.info("Environment variables loaded. %s", settings)
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        '''
            Returns the specified environment variable 
        '''
        logging.info(self.settings.get(env_var, None))
        return self.settings.get(env_var, None)

    def load_plugins(self):
        '''
            Dynamically load all plugins in the plugins directory
        '''
        plugins_package = 'app.plugins'
        plugins_path = plugins_package.replace('.', '/')
        if not os.path.exists(plugins_path): # pragma: no cover
            logging.warning("Plugins directory '%s' not found.", plugins_path)
            print("Plugins directory '%s' not found.", plugins_path)
            sys.exit(0)
        for _, plugin_name, is_pkg in pkgutil.iter_modules([plugins_path]):
            if is_pkg:
                plugin_module = importlib.import_module(f'{plugins_package}.{plugin_name}')
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)) and item is not Command:  # Added extra condition as it was registering the command twice
                            try:
                                if plugin_name == "menu":
                                    self.command_handler.register_command(plugin_name, item(self.command_handler))
                                else:
                                    self.command_handler.register_command(plugin_name, item())
                                logging.info("Command %s from plugin %s registered.", plugin_name, plugin_module)
                            except Exception as e: # pragma: no cover
                                logging.error("Failed to import plugin %s: %s", plugin_name, ic.format(e))
                    except TypeError:
                        continue  # If item is not a class or unrelated class, just ignore

    def start(self):
        '''
            Registers all the commands to be used by the user and starts the REPL
            Exits the app when the user types 'exit'
        '''
        # Register commands here
        self.load_plugins()
        logging.info("Application Started")

        self.command_handler.list_commands()
        print("Type 'exit' to exit.")
        try:
            while True:  #REPL Read, Evaluate, Print, Loop
                self.command_handler.execute_command(input(">>> ").split())
        except KeyboardInterrupt:
            logging.info("Application interrupted and exiting gracefully.")
            sys.exit(0)
        finally:
            logging.info("Application shutdown.")
