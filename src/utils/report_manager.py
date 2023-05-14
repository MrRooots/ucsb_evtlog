import pandas as pd
from src.config.config import Config
from src.models.event_model import EventModel


class ReportManager:
  """
  Class controls the creation of Excel | TXT files with results
  """

  # Configuration container
  config: Config = None

  def __init__(self, config: Config) -> None:
    self.config = config

  def make_excel(self, events: list[EventModel]) -> None:
    """ Create Excel file for given results """
    with pd.ExcelWriter(f'{self.config.filename}.xlsx') as writer:
      df = pd.DataFrame([event.to_list() for event in events],
                        columns=self.config.COLLECTED_DATA)
      df.to_excel(writer, 'results', index=False)

    print(f'[ReportManager]: Result saved to: {self.config.filename}.xlsx')

  def make_txt(self, events: list[EventModel]) -> None:
    """ Create Txt file for given results """
    with open(f'{self.config.filename}.txt', 'w') as file:
      for event in events:
        file.write(event.to_text() + '\n')

    print(f'[ReportManager]: Result saved to "{self.config.filename}.txt"')

  def make_report(self, events: list[EventModel]) -> str:
    """ Create report file for given `events` and return created file name"""

    if self.config.make_excel:
      self.make_excel(events)
    else:
      self.make_txt(events)

    return self.config.filename
