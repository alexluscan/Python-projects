from src.tests import test_book
from src.ui.ui import UI
from src.tests.test_book import Test
from src.repository.BinaryFileRepository import Binary
from src.repository.JSONRepository import JSON
from src.repository.MemoryRepository import Memory
from src.repository.TextFileRepository import Text
from jproperties import Properties

def get_repo_from_properties():
    configs = Properties()
    with open('settings.properties', 'rb') as config_file:
        configs.load(config_file)

    repo_string = configs.get("REPO").data
    repo = ""

    if repo_string == "Memory":
        repo = Memory()

    elif repo_string == "Text":
        repo = Text()

    elif repo_string == "Binary":
        repo = Binary()

    elif repo_string == "JSON":
        repo = JSON()

    return repo


def start():
    ui = UI(get_repo_from_properties())
    test = Test(get_repo_from_properties())
    test.test_all()
    ui.print_ui()

start()