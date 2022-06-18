
import pytest
firefox_mark =pytest.mark.firefox


@pytest.fixture()
def before_each(request):
    print("Called before each test " + request.node.name)


@pytest.fixture(scope='session', autouse=True)
def init_brwsr(request):
    print("Called before all tests " + request.node.name)


@pytest.fixture()
def message():
    return "This is message"


def firefox():
    return ""


def chrome_mobile():
    return ""

@firefox_mark
@pytest.fixture()
def client():
    client = 123
    print("Подготовили клиента")
    yield client
    print("А теперь удаляем клиента")


def test_first(before_each):
    print(before_each)
    assert 1 == 1


def test_second(before_each):
    assert 1 == 2, "Единица не должна быть равна двойке!"
