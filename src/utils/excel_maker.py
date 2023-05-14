from src.config.config import Config


class ExcelMaker:
  """
  Class controls the creation of Excel files with results
  """

  # Configuration container
  config: Config = None

  def __init__(self, config: Config) -> None:
    self.config = config

  def make_excel(self) -> None:
    """ Create Excel file for given results """
    pass
