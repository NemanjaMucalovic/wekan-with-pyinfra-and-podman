from pyinfra.operations import dnf, server, files

dnf.packages(
    name="install podman",
    packages=["podman"],
    update=True,
    _sudo=True,
)

server.shell(name="pull container images", commands=["podman pull docker.io/library/mongo; podman pull docker.io/wekanteam/wekan"])

files.directory(
    name="create project directory",
    path="~/wekan/",
)

files.template(
    name="Create kube file",
    src="templates/kube.j2",
    dest="~/wekan/kube.yml"
)

files.directory(
    name="create dir for quadlet files",
    path="~/.config/containers/systemd",
)

files.template(
    name="Create podman service file",
    src="templates/wekan.j2",
    dest="~/.config/containers/systemd/wekan.kube",
)
