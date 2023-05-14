class EventModel:
  """
  Event model
  """

  def __init__(self, data: dict[str, str]) -> None:
    self.event_id = data['EventID']
    self.computer_name = data['ComputerName']
    self.created_at = data['TimeGenerated']
    self.username = data['UserName']
    self.domain = data['Domain']
    self.sid = data['Sid']
    self.process_name = data['ProcessName']
    self.action = data['Action']

  def to_text(self) -> str:
    """ Get readable form of the event """
    return (
      f"ComputerName: \t {self.computer_name}\n"
      f"TimeGenerated: \t {self.created_at}\n"
      f"UserName: \t\t {self.username}\n"
      f"Domain: \t\t {self.domain}\n"
      f"Sid: \t\t\t {self.sid}\n"
      f"ProcessName: \t {self.process_name}\n"
      f"Action: \t\t {self.action}\n"
    )

  def to_list(self) -> list[str]:
    """ Get event as a dict """
    return [
      self.event_id,
      self.computer_name,
      self.created_at,
      self.username,
      self.domain,
      self.sid,
      self.process_name,
      self.action,
    ]
