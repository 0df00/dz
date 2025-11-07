import functools
import sys
from datetime import datetime
from typing import Callable, Optional, ParamSpec, TextIO, TypeVar

P = ParamSpec("P")  # Для параметров оборачиваемой функции
R = TypeVar("R")  # Для возвращаемого значения оборачиваемой функции


def log(
    filename: Optional[str] = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Декоратор для логовв вызовов функций"""

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        @functools.wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            # Определяем куда писать лог
            log_output: Optional[TextIO] = None
            file_handle: Optional[TextIO] = None
            if filename:
                try:
                    file_handle = open(filename, "a", encoding="utf-8")
                    log_output = file_handle
                except Exception as e:
                    print(f"log decorator error opening file: {e}", file=sys.stderr)

            # Получаем текущую дату и время
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            try:
                result: R = func(*args, **kwargs)
                log_message = f"[{timestamp}] {func.__name__} ok"
                print(log_message, file=log_output)
                if file_handle:
                    file_handle.close()
                return result
            except Exception as e:
                log_message = f"[{timestamp}] {func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                print(log_message, file=log_output)
                if file_handle:
                    file_handle.close()
                raise

        return wrapper

    return decorator
