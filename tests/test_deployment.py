def test_if_podman_is_installed(host):
    assert host.package("podman").is_installed


def test_if_images_are_pulled(host):
    cmd = host.check_output("podman images")
    assert "docker.io/library/mongo" and "docker.io/wekanteam/wekan" in cmd


def test_if_wekan_dir_is_there(host):
    assert host.file("~/wekan").is_directory


def test_if_kube_yaml_is_copied(host):
    assert host.file("~/wekan/kube.yml").exists


def test_if_systemd_dir_is_there(host):
    assert host.file("~/.config/containers/systemd/").is_directory


def test_if_quadlet_yaml_is_copied(host):
    assert host.file("~/.config/containers/systemd/wekan.kube").exists


def test_backend_pod_is_running(host):
    assert host.podman("route-planner-deployment-pod-fast-api").is_running


def test_health_route(host):
    cmd = host.run("curl -I localhost:8080/login")
    assert "alive" in cmd.stdout


def test_port_is_opened(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening


def test_mongodb_pod_is_running(host):
    assert host.podman("route-planner-deployment-pod-mongodb").is_running
