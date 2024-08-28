import yaml
class ConfigReader:
    def __init__(self, config_file='config/config.yaml'):
        self.config_file = config_file

    def read_config(self):
        with open(self.config_file, 'r') as file:
            config = yaml.safe_load(file)
        return config