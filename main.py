from src.core.event_manager import EventManager
from src.config.config import Config
from src.utils.arg_parser import ArgParser
from src.utils.report_manager import ReportManager
from src.utils.timer import Timer


@Timer.timeit
def main():
  config = Config(**ArgParser.parse_console())

  event_manager = EventManager(config)
  report_manager = ReportManager(config)

  report_manager.make_report(
    event_manager.get_events()
  )


if __name__ == '__main__':
  main()
