import pytest
from datetime import datetime
from package.display import show, write


# Mock datetime class
class MockDateTime(datetime):
    @classmethod
    def now(cls):
        return datetime.strptime("1234", "%H%M")  # Mock time to 12:34


# Mock file operations
def mock_glob_single_file(*args, **kwargs):
    return ["test_file.txt"]


def mock_glob_no_file(*args, **kwargs):
    return []


def mock_glob_multiple_files(*args, **kwargs):
    return ["test1.txt", "test2.txt"]


def mock_open_file_content(*args, **kwargs):
    class MockFile:
        def __enter__(self):
            return self

        def __exit__(self, *args):
            pass

        def read(self):
            return "Sample content"

    return MockFile()


# Mock subprocess for clipboard operations
def mock_subprocess_run(*args, **kwargs):
    return None


# Test cases for show function
def test_show_correct_password(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)
    monkeypatch.setattr("glob.glob", mock_glob_single_file)
    monkeypatch.setattr("builtins.open", mock_open_file_content)

    # Should not raise any exception
    show("test_snippet", "1234")


def test_show_incorrect_password(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)

    with pytest.raises(ValueError, match="syntax error: incorrect password"):
        show("test_snippet", "5678")


# Test cases for clipboard functionality
def test_show_with_clipboard_linux(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)
    monkeypatch.setattr("glob.glob", mock_glob_single_file)
    monkeypatch.setattr(
        "package.show.glob.glob", mock_glob_single_file
    )  # Added this line
    monkeypatch.setattr("builtins.open", mock_open_file_content)
    monkeypatch.setattr("sys.platform", "linux")
    monkeypatch.setattr("shutil.which", lambda x: "/usr/bin/xclip")
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)

    show("test_snippet", "1234", clipboard=1)


def test_show_with_clipboard_windows(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)
    monkeypatch.setattr("glob.glob", mock_glob_single_file)
    monkeypatch.setattr(
        "package.show.glob.glob", mock_glob_single_file
    )  # Added this line
    monkeypatch.setattr("builtins.open", mock_open_file_content)
    monkeypatch.setattr("sys.platform", "win32")
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)

    show("test_snippet", "1234", clipboard=1)


def test_show_with_clipboard_macos(monkeypatch):
    monkeypatch.setattr("package.show.datetime", MockDateTime)
    monkeypatch.setattr("glob.glob", mock_glob_single_file)
    monkeypatch.setattr(
        "package.show.glob.glob", mock_glob_single_file
    )  # Added this line
    monkeypatch.setattr("builtins.open", mock_open_file_content)
    monkeypatch.setattr("sys.platform", "darwin")
    monkeypatch.setattr("subprocess.run", mock_subprocess_run)

    show("test_snippet", "1234", clipboard=1)


# Test cases for write function
def test_write_correct_password(monkeypatch):
    monkeypatch.setattr("package.write.datetime", MockDateTime)
    monkeypatch.setattr("glob.glob", mock_glob_single_file)
    monkeypatch.setattr(
        "package.write.glob.glob", mock_glob_single_file
    )  # Added this line
    monkeypatch.setattr("shutil.copyfile", lambda x, y: None)

    write("test_snippet", "1234")


def test_write_incorrect_password(monkeypatch):
    monkeypatch.setattr("package.write.datetime", MockDateTime)

    with pytest.raises(ValueError, match="syntax error: incorrect password"):
        write("test_snippet", "5678")
