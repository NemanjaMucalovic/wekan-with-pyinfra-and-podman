def test_if_podman_is_installed(host):
    assert host.package("podman").is_installed


def test_if_images_are_pulled(host):
    cmd = host.check_output("podman images")
    assert "docker.io/library/mongo" and "docker.io/wekanteam/wekan" in cmd


def test_if_wekan_dir_is_there(host, config_data):
    assert host.file(
        f"/home/{config_data['ssh_user']}/{config_data['path_to_kube']}"
    ).is_directory


def test_if_kube_yaml_is_copied(host, config_data):
    assert host.file(
        f"/home/{config_data['ssh_user']}/{config_data['path_to_kube']}/kube.yml"
    ).exists


def test_if_systemd_dir_is_there(host, config_data):
    assert host.file(
        f"/home/{config_data['ssh_user']}/{config_data['path_to_quadlet']}"
    ).is_directory


def test_if_quadlet_yaml_is_copied(host, config_data):
    assert host.file(
        f"/home/{config_data['ssh_user']}/{config_data['path_to_quadlet']}/wekan.kube"
    ).exists


def test_backend_pod_is_running(host):
    assert host.podman("wekan-board").is_running


def test_mongo_pod_is_running(host):
    assert host.podman("wekan-db").is_running


def test_health_route(host):
    cmd = host.run("curl -I localhost:8080/login")
    assert "200" in cmd.stdout


def test_port_is_opened(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening
