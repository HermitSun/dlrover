import os
from pathlib import Path
from typing import List

from sftrain.python.common.log import default_logger as logger


def is_same_path(path1: str, path2: str):
    """
    Is target path the same.

    Args:
        path1 (str): Path 1.
        path2 (str): Path 2.

    Returns:
        result
    """

    return Path(path1).resolve() == Path(path2).resolve()


def read_last_n_lines(filepath: str, n_lines: int) -> List[bytearray]:
    try:
        with open(filepath, "rb") as f:
            remain_lines = n_lines
            block_size = 1024
            buffer = bytearray()

            f.seek(0, 2)
            total_size = f.tell()

            while remain_lines > 0 and total_size > 0:
                read_size = min(block_size, total_size)
                f.seek(-read_size, 1)
                buffer.extend(f.read(read_size))
                total_size -= read_size
                f.seek(-read_size, 1)

                remain_lines -= buffer.count(b"\n")

            lines = buffer.split(b"\n")
            return lines[-n_lines:]
    except Exception as e:
        logger.error(f"Fail to read {n_lines} line from {filepath}: {e}")
        return []


def find_file_in_parents(filename, start_dir=None):
    """
    Find target file in parent directories.

    Args:
        filename (str): Target filename.
        start_dir (str, optional): Target directory. Defaults to None(from
            current directory).

    Returns:
        result(str): The target file path.
    """

    if start_dir is None:
        start_dir = os.path.abspath(os.curdir)

    current_dir = start_dir

    while True:
        file_path = os.path.join(current_dir, filename)

        if os.path.isfile(file_path):
            return file_path

        parent_dir = os.path.dirname(current_dir)

        if parent_dir == current_dir:
            return None

        current_dir = parent_dir
