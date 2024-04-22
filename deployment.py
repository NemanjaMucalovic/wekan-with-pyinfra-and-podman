from pyinfra import host
from pyinfra.operations import server, dnf, files, systemd


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
    path=f"/home/{host.data.ssh_user}/{host.data.path_to_kube}",
)

files.template(
    name="Create kube file",
    src="templates/kube.j2",
    dest=f"/home/{host.data.ssh_user}/{host.data.path_to_kube}/kube.yml",
)

files.directory(
    name="create dir for quadlet files",
    path=f"/home/{host.data.ssh_user}/{host.data.path_to_quadlet}",
)

files.template(
    name="Create podman service file",
    src="templates/wekan.j2",
    dest=f"/home/{host.data.ssh_user}/{host.data.path_to_quadlet}/wekan.kube",
    ssh_user=host.data.ssh_user,
    kube_path=host.data.path_to_kube,
)

systemd.service(
    name="Start kube service",
    service="wekan",
    running=True,
    daemon_reload=True,
    user_mode=True,
    user_name=host.data.ssh_user,
)
