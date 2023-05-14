import sys

from src.config.exceptions import MissingRequiredArgumentException
from src.core.event_manager import EventManager
from src.config.config import Config


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
    param, val = arg.replace('--', '').split('=') if '=' in arg else (Config.CMD_ARGS[0], arg)
    args[param.replace('-', '_')] = val

  if Config.CMD_ARGS[0] not in args:
    raise MissingRequiredArgumentException()

  return args


def main():
  config = Config(**parse_console())

  print(config.computer_name)
  print(config.sid)
  print(config.start_date)
  print(config.end_date)
  print(config.make_excel)

  event_manager = EventManager(config)

  for event in event_manager.get_events():
    print(event)


if __name__ == '__main__':
  main()
