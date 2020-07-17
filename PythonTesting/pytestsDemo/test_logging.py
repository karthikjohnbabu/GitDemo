import logging
def test_loggingDemo():
    logger = logging.getLogger(__name__)

    fileHandler = logging.FileHandler ('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
    fileHandler.setFormatter(formatter)


    logger.addHandler(fileHandler)  #filehandler object.

    logger.setLevel(logging.INFO)
    logger.debug("A debug statment is executed")
    logger.info("Information Statement")
    logger.warning("once the automation script finds a negative value in bank account warning will be generated")
    logger.error("A major error has happened")
    logger.critical("Critical issue")

