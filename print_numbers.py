#!/usr/bin/env python3
"""1부터 100까지 숫자를 출력하는 프로그램"""


def print_numbers(start: int = 1, end: int = 100) -> None:
    """지정된 범위의 숫자를 출력한다.

    Args:
        start: 시작 숫자 (기본값: 1)
        end: 끝 숫자 (기본값: 100)
    """
    for number in range(start, end + 1):
        print(number)


if __name__ == "__main__":
    print_numbers()
