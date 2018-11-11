import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_authorized_keys_file(host):
    f = host.file('/home/deploy/.ssh/authorized_keys')

    assert f.exists
    assert f.user == 'deploy'
    assert f.group == 'deploy'
