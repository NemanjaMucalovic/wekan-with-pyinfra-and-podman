from pyinfra.operations import dnf

dnf.packages(
    name="install podman",
    packages=["podman"],
    update=True,
    _sudo=True,
)
