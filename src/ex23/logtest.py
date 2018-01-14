import logging
import logging.config

if __name__ == '__main__' :
    myLogger=logging.getLogger('logtests')
    myLogger.setLevel(logging.DEBUG)

    myStreamHandler=logging.StreamHandler()
    myStreamHandler.setLevel(logging.DEBUG)
    myLogger.addHandler(myStreamHandler)

    myFormatter=logging.Formatter("%(asctime)s-%(name)s-%(msg)s")
    myStreamHandler.setFormatter(myFormatter)

    myLogger.debug("This is a debug message.")
    myLogger.warning("This is a warning message.")

