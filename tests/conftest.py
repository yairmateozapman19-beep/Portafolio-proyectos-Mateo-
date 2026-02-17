from _pytest.fixtures import fixture
from tests.config import Config

def pytest_addoption(parser):
    parser.addoption(
        '--env',
        action = 'store',
        help = 'Ambiente de ejecución de pruebas [qa, dev, preprod]'
    )

@fixture(scope='session')
def env(request):
    return request.config.getoption('--env')

@fixture(scope='session')
def app_config(env):
    cfg = Config(env)
    return cfg