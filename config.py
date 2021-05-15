from configparser import ConfigParser

class Config:
    def __init__(self):
        self.cfg = ConfigParser()
        self.cfg.read('config.ini')  
    
    def get_general_config(self,section):
        config_projeto1 = {k:int(v) for k,v in self.cfg.items(section)}
        return config_projeto1
    


