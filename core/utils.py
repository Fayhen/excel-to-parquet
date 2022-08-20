from datetime import datetime, timezone


def get_datetime(tz: timezone = timezone.utc, formatted: bool = True) -> str:
    """
    Generates an aware date and time string for the moment of invocation. Timezone
    and a `formatted` boolean flag may be passed as optional arguments. Timezone must
    be an instance of the ``datetime.timezone`` class. The `formatted` flag generates
    a more human-readable string with the ``%Y-%m-%d %H:%M:%S %Z`` format. Otherwise,
    the string has a shorter ``%Y%m%d%H%M%S`` format.

    :param tz: Timezone to be used. Defaults to UTC.
    :type tz: timezone
    :param formatted: Whether to format the string or not. Defaults to True.
    :type formatted: bool
    :return: Datetime string for the moment of invocation.
    :rtype: str
    """
    now = datetime.now(tz)

    if formatted:
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")
    else:
        return now.strftime("%Y%m%d%H%M%S")
