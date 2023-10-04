from pyinfra.operations import dnf, server, files, systemd


def get_testinfra_username(host):
    """Gets the username for Testinfra from group_data."""
    return host.get_group_data("wekan", "ssh_user")


dnf.packages(
    name="install podman",
    packages=["podman"],
    update=True,
    _sudo=True,
)

server.shell(
    name="pull container images",
    commands=[
        "podman pull docker.io/library/mongo; podman pull docker.io/wekanteam/wekan"
    ],
)

files.directory(
    name="create project directory",
    path="/home/nemanja/wekan/",
)

files.template(
    name="Create kube file", src="templates/kube.j2", dest="/home/nemanja/wekan/kube.yml"
)

files.directory(
    name="create dir for quadlet files",
    path="/home/nemanja/.config/containers/systemd",
)

files.template(
    name="Create podman service file",
    src="templates/wekan.j2",
    dest="/home/nemanja/.config/containers/systemd/wekan.kube",
)

systemd.service(
    name="Start kube service",
    service="wekan",
    running=True,
    daemon_reload=True,
    user_mode=True,
    user_name="nemanja"
)

