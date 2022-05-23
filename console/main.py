from os import system


class console:
    """
    This class is just an implementation of javascript console in python
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def log(val, *args, **kwargs) -> None:
        """
        Prints output to the console
        """
        print(val, *args, **kwargs)

    @staticmethod
    def warn(val, *args, **kwargs) -> None:
        """
        Prints warning string
        """
        print(f"\033[1;33m{val}\033[m", *args, **kwargs)

    @staticmethod
    def error(val, *args, **kwargs) -> None:
        """
        Prints error string
        """
        print(f"\033[1;31m{val}\033[m", *args, **kwargs)

    @staticmethod
    def info(val, *args, **kwargs) -> None:
        """
        Prints info string
        """
        print(f"\033[1;34m{val}\033[m", *args, **kwargs)

    @staticmethod
    def debug(val, *args, **kwargs) -> None:
        """
        Prints debug string
        """
        print(f"\033[1;30m{val}\033[m", *args, **kwargs)

    @staticmethod
    def status(val, *args, **kwargs) -> None:
        """
        Prints a  purple colored string
        """
        print(f"\033[1;35m{val}\033[m", *args, **kwargs)

    @staticmethod
    def clear() -> None:
        """
        Clears the console
        """
        system("cls")
