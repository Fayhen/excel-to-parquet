import os
import logging


class CustomLogger:
    formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%dT%H:%M:%S%z")

    def __init__(self, filename, filepath, base_path):
        os.chdir(filepath)

        self.filename = f"{filename}.log"
        self.file_handler = logging.FileHandler(self.filename)
        self.file_handler.setFormatter(self.formatter)

        self.logger = logging.getLogger(filename)
        self.logger.addHandler(self.file_handler)
        self.logger.setLevel(logging.INFO)

        self.error_filename = f"{filename}.errors.log"
        self.error_file_handler = logging.FileHandler(self.error_filename, delay=True)
        self.error_file_handler.setFormatter(self.formatter)

        self.error_logger = logging.getLogger(self.error_filename)
        self.error_logger.addHandler(self.error_file_handler)
        self.error_logger.setLevel(logging.INFO)
        self.error_logger.propagate = False

        os.chdir(base_path)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warn(self, message):
        self.logger.warning(message)
        self.error_logger.warning(message)

    def error(self, message):
        self.logger.error(message)
        self.error_logger.error(message)

    def critical(self, message):
        self.logger.critical(message)
        self.error_logger.critical(message)

    def exception(self, message):
        self.logger.exception(message)
        self.error_logger.exception(message)
