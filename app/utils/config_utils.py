import os
import logging
import logging.config
import yaml
logger = logging.getLogger(__name__)


def load_yaml_config():
    CONFIG_DEFAULT = 'app/application.yml'
    CONFIG_LOCAL = 'config/application-local.yml'
    CONFIG_FILE = CONFIG_LOCAL if os.path.exists(CONFIG_LOCAL) else CONFIG_DEFAULT

    with open(CONFIG_FILE, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.info('Loaded configuration file %s' % CONFIG_FILE)

    return config
