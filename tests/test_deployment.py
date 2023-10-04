def test_if_podman_is_installed(host):
    assert host.package("podman").is_installed


def test_backend_pod_is_running(host):
    assert host.podman("route-planner-deployment-pod-fast-api").is_running


def test_health_route(host):
    cmd = host.run("curl -I localhost:8080/login")
    assert "alive" in cmd.stdout


def test_port_is_opened(host):
    assert host.socket("tcp://0.0.0.0:8080").is_listening


def test_mongodb_pod_is_running(host):
    assert host.podman("route-planner-deployment-pod-mongodb").is_running
