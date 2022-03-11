# -*- coding: utf-8 -*-

import sys
from ..lib import MacOSTerminalException


def entrypoint(callable):
    def _wrapper(*args, **kwargs):
        try:
            return callable(*args, **kwargs)
        except MacOSTerminalException as error:
            print(error, file=sys.stderr)
            sys.exit(1)
        except KeyboardInterrupt:
            sys.exit(1)

    return _wrapper
