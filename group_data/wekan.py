from config import config_from_json

config_data = config_from_json("conf.json", read_from_file=True)

ssh_user = config_data["ssh_user"]
path_to_kube = config_data["path_to_kube"]
path_to_quadlet = config_data["path_to_quadlet"]
