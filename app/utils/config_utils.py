import os
import logging
import logging.config
import yaml

logger = logging.getLogger(__name__)


def load_yaml_config():
    config_default = 'app/application.yaml'
    config_local = 'config/application.yaml'
    config_file = config_local if os.path.exists(config_local) else config_default

    with open(config_file, 'rt') as f:
        config = yaml.safe_load(f.read())
    logging.info('Loaded configuration file: %s' % config_file)

    return config
