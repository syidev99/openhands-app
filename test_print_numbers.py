#!/usr/bin/env python3
"""print_numbers.py 테스트"""

import pytest
from io import StringIO
from unittest.mock import patch

from print_numbers import print_numbers


class TestPrintNumbers:
    """print_numbers 함수 테스트"""

    def test_default_range_1_to_100(self):
        """TC-001: 기본값(1~100) 출력 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers()
            output = mock_stdout.getvalue()
            lines = output.strip().split("\n")

            assert len(lines) == 100
            assert lines[0] == "1"
            assert lines[-1] == "100"

    def test_custom_range_1_to_10(self):
        """TC-002: 커스텀 범위(1~10) 출력 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(1, 10)
            output = mock_stdout.getvalue()
            lines = output.strip().split("\n")

            assert len(lines) == 10
            assert lines == ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

    def test_custom_range_50_to_55(self):
        """TC-003: 중간 범위(50~55) 출력 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(50, 55)
            output = mock_stdout.getvalue()
            lines = output.strip().split("\n")

            assert len(lines) == 6
            assert lines == ["50", "51", "52", "53", "54", "55"]

    def test_single_number(self):
        """TC-004: 단일 숫자(start == end) 출력 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(42, 42)
            output = mock_stdout.getvalue()

            assert output.strip() == "42"

    def test_negative_numbers(self):
        """TC-005: 음수 범위(-5~5) 출력 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(-5, 5)
            output = mock_stdout.getvalue()
            lines = output.strip().split("\n")

            assert len(lines) == 11
            assert lines[0] == "-5"
            assert lines[-1] == "5"

    def test_empty_range_start_greater_than_end(self):
        """TC-006: 빈 범위(start > end) 테스트 - 출력 없음"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(10, 5)
            output = mock_stdout.getvalue()

            assert output == ""

    def test_large_range(self):
        """TC-007: 큰 범위(1~1000) 출력 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(1, 1000)
            output = mock_stdout.getvalue()
            lines = output.strip().split("\n")

            assert len(lines) == 1000
            assert lines[0] == "1"
            assert lines[499] == "500"
            assert lines[-1] == "1000"

    def test_zero_included(self):
        """TC-008: 0 포함 범위(-2~2) 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(-2, 2)
            output = mock_stdout.getvalue()
            lines = output.strip().split("\n")

            assert "0" in lines
            assert lines == ["-2", "-1", "0", "1", "2"]

    def test_output_format_newline_separated(self):
        """TC-009: 출력 형식(개행 구분) 테스트"""
        with patch("sys.stdout", new_callable=StringIO) as mock_stdout:
            print_numbers(1, 3)
            output = mock_stdout.getvalue()

            assert output == "1\n2\n3\n"

    def test_return_value_is_none(self):
        """TC-010: 반환값이 None인지 테스트"""
        with patch("sys.stdout", new_callable=StringIO):
            result = print_numbers(1, 5)

            assert result is None
