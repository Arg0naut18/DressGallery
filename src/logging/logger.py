import logging
import logging.config
from src.constants import LoggerConstants


class GalleryLogger:
    def __init__(self):
        # Set up basic configuration
        logging.basicConfig(
            filename=LoggerConstants.FILENAME,
            format=LoggerConstants.FORMAT,
            filemode='a',
            level=LoggerConstants.LOG_LEVEL
        )

        # Get the root logger
        self.logger = logging.getLogger("gallery.logs")

        # Adding Uvicorn loggers to ensure compatibility
        uvicorn_error_logger = logging.getLogger("uvicorn.error")
        uvicorn_error_logger.handlers = self.logger.handlers
        uvicorn_error_logger.propagate = True

        uvicorn_access_logger = logging.getLogger("uvicorn.access")
        uvicorn_access_logger.handlers = self.logger.handlers
        uvicorn_access_logger.propagate = True


logger = GalleryLogger().logger
