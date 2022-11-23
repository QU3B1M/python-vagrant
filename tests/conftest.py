import pytest

from src.vagrant.machines import VMsDefiner, VagrantMachine


@pytest.fixture
def restore_definition_file():
    original_data = VMsDefiner.get_defined_machines()
    yield
    VMsDefiner._save_machines(original_data)
