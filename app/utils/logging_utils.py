import os
import logging
import logging.config
import yaml
logger = logging.getLogger(__name__)


def setup_logging(
    default_path='logging.yml',
    default_level=logging.INFO,
    default_format='%(levelname)-7.7s] [%(asctime)s] [%(funcName)20s()] L%(lineno)d %(message)s',
    env_key='LOG_CFG'
):
    """
    Set up logging configuration
    """
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level,format=default_format)


def test_logging():
    """
    :return:
    """

    logging.info('Logging enabled in %s' % __name__)
    logging.info('TEST: INFO')
    logging.warning('TEST: WARNING')
    logging.error('TEST: ERROR')
    logging.debug('TEST: DEBUG')