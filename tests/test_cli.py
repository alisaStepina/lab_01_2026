import subprocess
import sys


def test_cli_calc():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "calc", "2+2"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "4.0" in result.stdout


def test_cli_convert():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "convert", "100", "--from", "cm", "--to", "m"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 0
    assert "1.0" in result.stdout


def test_cli_error():
    result = subprocess.run(
        [sys.executable, "-m", "toolkit", "convert", "1", "--from", "m", "--to", "kg"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert result.returncode == 2