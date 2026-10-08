from src.utils import read_json_file


def test_read_json_file_not_found():
    result = read_json_file("nonexistent.json")

    assert result == []


def test_read_json_file_empty(tmp_path):
    file_path = tmp_path / "empty.json"
    file_path.write_text("", encoding="utf-8")

    result = read_json_file(str(file_path))

    assert result == []


def test_read_json_file_not_list(tmp_path):
    file_path = tmp_path / "object.json"
    file_path.write_text('{"amount": "100"}', encoding="utf-8")

    result = read_json_file(str(file_path))

    assert result == []


def test_read_json_file_list(tmp_path):
    file_path = tmp_path / "operations.json"
    file_path.write_text(
        '[{"amount": "100", "currency": "USD"}]',
        encoding="utf-8",
    )

    result = read_json_file(str(file_path))

    assert result == [{"amount": "100", "currency": "USD"}]
