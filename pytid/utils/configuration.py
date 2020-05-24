import os
import yaml

default_config = os.path.join("config", "configuration.yml")


class Configuration:

    def __init__(self, config_file=default_config):

        with open(config_file, "r") as f:
            conf = yaml.safe_load(f)

        self._conf = conf
        self.gnss = conf.get("gnss")
        self.logging = conf.get("logging")
        self.plotting = conf.get("plotting")
