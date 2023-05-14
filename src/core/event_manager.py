import win32api
import win32evtlog
import winerror

from src.config.config import Config
from src.core.query_manager import QueryManager
from src.utils.format_util import FormatUtil


class EventManager:
  """
  Class that works with events.
  Collect, filter, return in readable format
  """

  # Configuration container
  config: Config = None

  # Log reader handler
  handler = None

  # Log reader config flags
  flags = None

  # Total list of filtered events
  events = []

  def __init__(self, config: Config) -> None:
    self.config = config
    self.handler = self.__create_handler()
    self.flags = win32evtlog.EVENTLOG_BACKWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ

  def __create_handler(self):
    """ Attempt to create event log reader handler """
    print('[EventManager]: Creating handler')
    try:
      handler = win32evtlog.OpenEventLog(self.config.remote_computer_name,
                                         self.config.log_type)
      print('[EventManager]: Handler created')

      return handler
    except win32api.error as error:
      if error.winerror == winerror.ERROR_PRIVILEGE_NOT_HELD:
        exit('[FatalError]: The script must be run as an administrator!')
      else:
        exit(f'[FatalError]: Unhandled exception during handler creation: {error}')

  def get_events(self) -> list:
    """ Get events that specified in config file """
    print(f'[EventManager]: Total events count: {win32evtlog.GetNumberOfEventLogRecords(self.handler)}')
    print(f'[EventManager]: Filtering starts. Please wait')

    events = win32evtlog.EvtQuery('Security', win32evtlog.EvtQueryReverseDirection,
                                  QueryManager.build_xml_query_from_config(self.config),
                                  None)

    while True:
      event = win32evtlog.EvtNext(events, 15)

      if len(event) == 0:
        break

      for e in event:
        event_xml = win32evtlog.EvtRender(e, win32evtlog.EvtRenderEventXml)
        print(FormatUtil.format_event(event_xml))

    return self.events
