import inspect
import logging


class Loggen:
    @staticmethod
    def loggen():
        loggerName=inspect.stack()[1][3]
        logger=logging.getLogger(loggerName)
        filehandler=logging.FileHandler(".\\Logs\\logfile.log")
        formatter=logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s",
                                    datefmt="%m/%d/%Y %I:%M:%S %p")
        filehandler.setFormatter(formatter)
        logger.addHandler(filehandler)
        logger.setLevel(logging.INFO)
        return logger