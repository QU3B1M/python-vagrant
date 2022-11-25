import pytest

from src.vagrant.machines import VMsDefiner, VagrantMachine


@pytest.fixture()
def restore_definition_file():
    """Do some cleanup the definitions file after test execution."""
    original_data = VMsDefiner.get_defined_machines()
    yield
    VMsDefiner._save_machines(original_data)
