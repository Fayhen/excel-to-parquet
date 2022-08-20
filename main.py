#!

"""
excel-to-parquet module and Command Line Interface
"""

import os
import sys
import click
from pathlib import Path

import core.scripts as scripts
from core.tools import CustomLogger
from core.utils import get_datetime


base_path = os.getcwd()
inputs_path = f"{base_path}/inputs"
outputs_path = f"{base_path}/outputs"

Path(inputs_path).mkdir(exist_ok=True)
Path(outputs_path).mkdir(exist_ok=True)


def cli():
    now = get_datetime(formatted=False)
    logger = CustomLogger(now, outputs_path, base_path)
    logger.info("Started program execution.")
    logger.info(f"Program running from directory: {base_path}")

    click.secho("\nRunning program 'excel-to-parquet' version alpha.", fg="green")
    click.echo("\nWelcome. This is a parser program that reads spreadsheets from Excel files, validates data,"
               " and generates a Parquet file of defined structure.")
    click.echo("\nThis is a sample program intended as an example of how to read and process Excel files with"
               " Python and the 'pandas' tool. More information can be found in the README in this program's"
               " root directory, or at https://github.com/Fayhen/excel-to-parquet.")
    # click.echo("\nExcel files are consumed from the '/inputs' folder and results saved to the '/outputs' folder"
    #            " at the root directory of this program. Excel files must also have a defined structure.")

    filenames = scripts.get_excel_files(inputs_path, logger=logger)

    if len(filenames) == 0:
        logger.info(f"No Excel files found on the input directory at: {inputs_path}")
        logger.info("Finishing program execution.")
        click.secho("\nNo Excel files were found on the inputs directory.", fg="yellow")
        click.echo(f"Finished program. Logs can be found at: {click.format_filename(outputs_path)}")
        sys.exit()


if __name__ == "__main__":
    cli()
