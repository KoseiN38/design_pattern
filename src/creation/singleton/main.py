from src.creation.singleton.process.connect import DatabaseConnector
from src.utils.logger import logger

if __name__ == "__main__":
    try:
        db1 = DatabaseConnector("mysql")
        db2 = DatabaseConnector("postgres")
        db1.connect()
        db1.connect()
        logger.info(db1 is db2)
    except Exception as e:
        logger.error(e)
        raise e
