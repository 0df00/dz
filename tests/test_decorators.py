from typing import Any, Optional
from unittest.mock import patch

import pytest

from src.decorators import log


def test_log_console_success(capsys: Any) -> None:
    """Тест логов в консоль при успехе"""

    @log()
    def successful_func(a: int, b: int) -> int:
        return a + b

    result = successful_func(1, 2)
    assert result == 3

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    last_line = output_lines[-1] if output_lines else ""
    assert "successful_func ok" in last_line


def test_log_console_error(capsys: Any) -> None:
    """Тест логов в консоль при ошибке"""

    @log()
    def error_func() -> None:
        raise ValueError("Test error")

    with pytest.raises(ValueError):
        error_func()

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    last_line = output_lines[-1] if output_lines else ""
    assert "error_func error: ValueError. Inputs: (), {}" in last_line


def test_log_file_success(temp_log_file: str) -> None:
    """Тест логов в файл при упехе"""

    @log(filename=temp_log_file)
    def file_success_func(x: int) -> int:
        return x * 2

    result = file_success_func(5)
    assert result == 10

    # Читаем файл и проверяем содержимое
    with open(temp_log_file, "r", encoding="utf-8") as f:
        log_content = f.read()

    assert "file_success_func ok" in log_content
    assert "[20" in log_content


def test_log_file_error(temp_log_file: str) -> None:
    """Тест логов в файл при ошибке"""

    @log(filename=temp_log_file)
    def file_error_func(y: float) -> float:
        return 1 / y

    with pytest.raises(ZeroDivisionError):
        file_error_func(0)

    # Читаем файл и проверяем содержимое
    with open(temp_log_file, "r", encoding="utf-8") as f:
        log_content = f.read()

    assert "file_error_func error: ZeroDivisionError. Inputs: (0,), {}" in log_content
    assert "[20" in log_content


def test_log_args(capsys: Any) -> None:
    """Тест логов с аргументами"""

    @log()
    def func_with_args(a: int, b: int = 10, c: Optional[int] = None) -> int:
        if a == 0:
            raise RuntimeError("a is zero")
        return a + b + (c or 0)

    result = func_with_args(1, b=20, c=5)
    assert result == 26

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    last_line = output_lines[-1] if output_lines else ""
    assert "func_with_args ok" in last_line

    with pytest.raises(RuntimeError):
        func_with_args(0, b=20, c=5)

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    last_line = output_lines[-1] if output_lines else ""
    assert "func_with_args error: RuntimeError. Inputs: (0,), {'b': 20, 'c': 5}" in last_line


def test_log_no_filename_still_works(capsys: Any) -> None:
    """Тест декоратор без filename работает (в консоль)"""

    @log()
    def simple_func() -> str:
        return "ok"

    result = simple_func()
    assert result == "ok"

    captured = capsys.readouterr()
    output_lines = captured.out.strip().split("\n")
    last_line = output_lines[-1] if output_lines else ""
    assert "simple_func ok" in last_line


def test_log_file_open_error(capsys: Any) -> None:
    """Тест логов ошибки открытие файла"""
    with patch("src.decorators.open", side_effect=PermissionError("Mocked PermissionError")):

        @log(filename="test_file.log")
        def dummy_func() -> str:
            return "result_if_no_error"

        result = dummy_func()
        assert result == "result_if_no_error"

    captured = capsys.readouterr()
    assert "log decorator error opening file:" in captured.err
