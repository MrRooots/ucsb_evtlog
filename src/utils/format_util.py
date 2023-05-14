from dateutil import tz, parser as date_parser
from bs4 import BeautifulSoup
from datetime import datetime


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
  def format_event(event) -> str:
    """ Return readable form of the event """
    soup = BeautifulSoup(event, 'lxml-xml')

    process_name = soup.find('Data', {'Name': 'ProcessName'})
    if not process_name:
      process_name = soup.find('Data', {'Name': 'NewProcessName'})

    return (
      f"EventID: \t\t {soup.find('EventID').text}\n"
      f"ComputerName: \t {soup.find('Computer').text}\n"
      f"TimeGenerated: \t {FormatUtil.datetime_from_iso(soup.find('TimeCreated').get('SystemTime'))}\n"
      f"UserName: \t\t {soup.find('Data', {'Name': 'SubjectUserName'}).text}\n"
      f"Domain: \t\t {soup.find('Data', {'Name': 'SubjectDomainName'}).text}\n"
      f"Sid: \t\t\t {soup.find('Data', {'Name': 'SubjectUserSid'}).text}\n"
      f"ProcessName \t {process_name.text}\n"
      f"Action: \t\t {FormatUtil.get_action_description(soup.find('EventID').text)}\n"
    )
