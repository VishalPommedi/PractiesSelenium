import logging
import os

class LogConfigurator:
    def __init__(self):
        pass

    def beforeall(self, context):
        # Get the absolute path of the feature file
        feature_file_path = context.feature.filename

        # Create the log file path by replacing the file extension
        log_file_path = os.path.splitext(feature_file_path)[0] + ".log"

        # Create a custom log file formatter
        log_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        global file_handler
        # Create a file handler and set the formatter
        file_handler = logging.FileHandler(log_file_path)
        file_handler.setFormatter(log_formatter)
        global root_logger
        # Get the root logger and add the file handler
        root_logger = logging.getLogger()
        root_logger.addHandler(file_handler)

    def after(self):
        # root_logger = logging.getLogger()
        root_logger.removeHandler(file_handler)
        file_handler.close()    