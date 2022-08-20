import os
import openpyxl

from typing import Union

from core.tools import CustomLogger


def get_excel_files(path: str, logger: CustomLogger) -> list[str]:
    """
    Gets a list o Excel file names from within the directory path passed as argument.

    :param path: Directory path inside which to collect Excel files.
    :type path: str
    :param logger: Logger instance.
    :type logger: CustomLogger
    :return: List of Excel file names within hte given directory.
    :rtype: list[str]
    """
    filenames = [file for file in os.listdir(path) if file.endswith(".xls") or file.endswith(".xlsx")]
    logger.info(f"Collected {len(filenames)} Excel files from path: {path}")

    return filenames


def read_excel_file(filepath: str, logger: CustomLogger) -> Union[openpyxl.Workbook, None]:
    """
    Reads an Excel file on the given filepath and returns its contents as an openpyxl
    Workbook instance.

    Should reading the Excel file fail, returns None instead.

    :param filepath: Path to the Excel file.
    :type filepath: str
    :param logger: Logger instance.
    :type logger: CustomLogger
    :return: openpyxl Workbook instance.
    :rtype: Union[openpyxl.Workbook, None]
    """
    try:
        wb = openpyxl.load_workbook(filepath, read_only=True)
        return wb

    except Exception as _:
        logger.exception(f"Exception raised to read Excel file at path: {filepath}")
        logger.critical("This file can not be read and will be skipped.")

        return None
