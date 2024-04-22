from config import config_from_json

config_data = config_from_json("conf.json", read_from_file=True)

servers = [config_data["target"]]
