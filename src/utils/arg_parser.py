import sys

from src.config.config import Config
from src.config.exceptions import MissingRequiredArgumentException


class ArgParser:
  @staticmethod
  def parse_console() -> dict[str, str]:
    """ Parse cmd variables into dict """
    args = {}

    if '-help' in sys.argv:
      exit((
        "Available params are stored if src.config.Config file:\n"
        "\t--name_or_ip -- [REQUIRED]: can be passed without '--'\n"
        "\t--sid: str\n"
        "\t--end_date: str\n"
        "\t--start_date: str\n"
        "\t--make_excel -- If specified then excel file will be created\n"
      ))

    for arg in sys.argv[1::]:
      arg = arg.replace('--', '')

      if '=' in arg:
        param, val = arg.split('=')
      else:
        if arg == Config.CMD_ARGS[-1]:
          param, val = Config.CMD_ARGS[-1], arg
        else:
          param, val = Config.CMD_ARGS[0], arg

      args[param.replace('-', '_')] = val

    if Config.CMD_ARGS[0] not in args:
      raise MissingRequiredArgumentException()

    return args
