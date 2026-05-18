import logging
import sys
def setup_logger(level:str='INFO'):
    logger=logging.getLogger("tracker.py")
    handler=logging.StreamHandler(sys.stdout)
    formatter=logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt="%y-%m-%d %H:%M:%s"
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(getattr(logging,level.upper(),logging.INFO))
    logger.propagate=False