import logging
import os

class LogContextFilter(logging.Filter):
    """
    Injects contextual information into the log such as appName, environment.namespace and environment.podName
    """

    def __init__(self):
        self.name = os.getenv('APP_NAME', 'unknown')
        self.podName = os.getenv('APP_POD_NAME', 'unknown')
        self.version = os.getenv('APP_VERSION', 'unknown')
        self.namespace = os.getenv('APP_NAMESPACE', 'unknown')

    def filter(self, record):
        record.appName = self.name
        record.version = self.version
        record.environment = {'podName': self.podName, 'namespace': self.namespace}

        return True

