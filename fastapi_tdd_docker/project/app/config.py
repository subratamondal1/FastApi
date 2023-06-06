# project/app/config.py

# logging: provides a way to log messages and events in your application
import logging
# os: provides access to operating system features such as environment variables
import os
# pydantic: library for data validation and settings management using Python type annotations
from pydantic import BaseSettings

from functools import lru_cache


# creates a logger object named log that uses the uvicorn logger, which is an ASGI server that runs FastAPI applications
log = logging.getLogger("uvicorn")


# This class represents the configuration settings for your application. It has two attributes: environment and testing.
class Settings(BaseSettings):
    # The environment attribute is a string that indicates the environment in which your application is running, such as 
    # 'dev', 'prod', etc. It gets its value from the environment variable ENVIRONMENT, or defaults to "dev" if not set.
    environment: str = os.getenv("ENVIRONMENT", "dev")
    # The testing attribute is a boolean that indicates whether your application is in testing mode or not. It gets 
    # its value from the environment variable TESTING, or defaults to 0 (which is equivalent to False) if not set.
    testing: bool = os.getenv("TESTING", 0)

# get_settings(): returns an instance of the Settings class. This function logs a message saying that it is loading the config settings 
# from the environment, and then calls the constructor of the Settings class.
@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return Settings()

