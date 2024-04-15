from src.ui.ui import UI
from src.repository.BinaryFileRepository import Binary
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

    return repo



if __name__ == "__main__":
        user_interface = UI(get_repo_from_properties())
        user_interface._main_loop()