import logging, sys

class LogGen:
    
    @staticmethod
    def loggen():
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        
        
        handler2 = logging.StreamHandler(sys.stdout)
        handler2.setLevel(logging.INFO)
        handler2.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))
        logger.addHandler(handler2)

        
        handler = logging.FileHandler(filename="./Logs/automation.log")
        handler.setLevel(logging.INFO)
        handler.setFormatter(logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p'))
        logger.addHandler(handler)
        return logger