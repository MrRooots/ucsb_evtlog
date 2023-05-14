from src.utils.format_util import FormatUtil


class Config:
  """
  Configuration container
  """

  # Name of the remote computer
  computer_name = None

  # Filtering: User SID
  sid = None

  # Filtering: start date
  start_date = None

  # Filtering: end date
  end_date = None

  # Creates Excel file if set to True, otherwise creates txt document
  make_excel = None

  # Default filename to save results in
  filename = 'results'

  # Type of logs to collect
  log_type = 'Security'

  # IDs of events to filter
  event_ids = [4688, 4689]

  # Available cmd arguments
  CMD_ARGS = [
    'name_or_ip',  # This argument is required
    'sid',
    'end_date',
    'start_date',
    'make_excel',
  ]

  def __init__(self,
               name_or_ip: str = 'localhost',
               sid: str = None,
               start_date: str = None,
               end_date: str = None,
               make_excel: bool = False) -> None:
    self.computer_name = name_or_ip

    self.sid = sid
    self.start_date = FormatUtil.datetime_to_iso(start_date) + 'T00:00:00Z' if start_date else start_date
    self.end_date = FormatUtil.datetime_to_iso(end_date) + 'T23:59:59Z' if end_date else end_date

    self.make_excel = make_excel
