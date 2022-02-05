
from pathlib import Path


# current path
BASE_DIR = Path(__file__).resolve().parent
EXAMPLES_DIR = BASE_DIR.joinpath('examples')


def get_file_path(file_name: Path) -> str:
    """Returns full path to file."""
    return EXAMPLES_DIR.joinpath(file_name).as_posix()


def get_file_content(file_path: str, read_mode: str = 'rb') -> str:
    """Returns file content of given file_path."""
    with open(file_path, read_mode) as file:
        return file.read()


def get_html_example_1251_encoding(file_name: str = 'example_1251_encoding.html'):
    """Returns content of example win 1251 encoding."""
    full_file_path = get_file_path(Path(file_name))

    return get_file_content(full_file_path)
