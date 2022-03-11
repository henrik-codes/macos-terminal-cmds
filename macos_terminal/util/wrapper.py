# -*- coding: utf-8 -*-

from pathlib import Path
import subprocess
import logging


log = logging.getLogger(__name__)


def run(scriptname, *args, on_error):
    script_path = Path(__file__).joinpath('../../applescript/_').resolve().with_name(scriptname)

    process = subprocess.run(
        [str(script_path), *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE)

    log.debug('%s stdout: %s', script_path.name, process.stdout)
    log.debug('%s stderr: %s', script_path.name, process.stderr)
    log.debug('%s exit code: %d', script_path.name, process.returncode)

    if process.returncode != 0:
        raise on_error

    return process.stdout.strip().decode('utf-8')
