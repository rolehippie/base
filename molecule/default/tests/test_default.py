import os
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("package", [
    "apt-transport-https",
    "software-properties-common",
    "tree",
    "htop",
    "iotop",
    "sysstat",
    "ipvsadm",
    "update-notifier-common",
    "socat",
    "jq",
    "curl",
    "apt-dater-host",
    "net-tools",
    "traceroute",
    "acl",
    "haveged"
])
def test_is_installed(host, package):
    pkg = host.package(package)
    assert pkg.is_installed
