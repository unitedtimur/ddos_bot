import logging, os
from datetime import date

if not os.path.isdir("logs"):
            os.mkdir("logs")

class Log:
    @staticmethod
    def log_info(information):
        #logging.basicConfig(handlers    = [ logging.FileHandler('logs/system-' + str(date.today()) + '.log', 'a', 'utf-8') ],
        #                    level       = logging.INFO,  
        #                    format      = '%(asctime)s - %(levelname)s : %(message)s')
        #logging.info(information)
        print(str(information) + '\n')

    @staticmethod
    def log_crit(critical):
        logging.basicConfig(handlers    = [ logging.FileHandler('logs/system-' + str(date.today()) + '.log', 'a', 'utf-8') ],
                            level       = logging.CRITICAL,
                            format      = '%(asctime)s - %(levelname)s : %(message)s')
        logging.critical(critical)
        print(str(critical) + '\n')
        