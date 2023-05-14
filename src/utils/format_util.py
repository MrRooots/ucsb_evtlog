from dateutil import tz, parser as date_parser
from bs4 import BeautifulSoup
from datetime import datetime

from src.models.event_model import EventModel


class FormatUtil:
  """
  Simple formatting utility container
  """

  @staticmethod
  def get_action_description(action: str) -> str:
    return f"Process {'Creation' if action == '4688' else 'Termination'}"

  @staticmethod
  def datetime_to_iso(timestamp: str) -> str:
    return datetime.strptime(timestamp, "%d.%m.%Y").strftime("%Y-%m-%d")

  @staticmethod
  def datetime_from_iso(iso_time: str) -> str:
    """
    Format windows ISO-8601 (*7-digit with Z*) to readable local datetime
    If formatting error occurs then utc format will be returned
    """

    try:
      utc = datetime.fromisoformat(iso_time[:26]).replace(tzinfo=tz.tzutc()).astimezone(tz.tzlocal())
      return utc.strftime('%d.%m.%Y %H:%M:%S')
    except ValueError:
      return date_parser.parse(iso_time).strftime('%d.%m.%Y %H:%M:%S')

  @staticmethod
  def __parse_event_xml(event: str) -> dict[str, str]:
    soup = BeautifulSoup(event, 'lxml-xml')

    process_name = soup.find('Data', {'Name': 'ProcessName'})
    if not process_name:
      process_name = soup.find('Data', {'Name': 'NewProcessName'})

    return {
      'EventID': soup.find('EventID').text,
      'ComputerName': soup.find('Computer').text,
      'TimeGenerated': FormatUtil.datetime_from_iso(soup.find('TimeCreated').get('SystemTime')),
      'UserName': soup.find('Data', {'Name': 'SubjectUserName'}).text,
      'Domain': soup.find('Data', {'Name': 'SubjectDomainName'}).text,
      'Sid': soup.find('Data', {'Name': 'SubjectUserSid'}).text,
      'ProcessName': process_name.text,
      'Action': FormatUtil.get_action_description(soup.find('EventID').text),
    }

  @staticmethod
  def event_to_model(event) -> EventModel:
    """ Parse given `event` to `EventModel` """
    return EventModel(FormatUtil.__parse_event_xml(event))
