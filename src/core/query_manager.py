from src.config.config import Config


class QueryManager:
  @staticmethod
  def _get_computer_query(computer_name: str) -> str:
    """ Build query for ComputerName filtration """
    if computer_name is None:
      return ''

    return f"(Computer='{computer_name}') and "

  @staticmethod
  def _get_date_query(start: str, end: str) -> str:
    if not start and not end:
      return ''

    query = ''
    both = start and end

    if start:
      query += f"""
        TimeCreated[@SystemTime >= '{start}']
      """

    if end:
      query += f"""
        {'and' if both else ''}
        TimeCreated[@SystemTime <= '{end}']
      """

    return f'and ({query})'

  @staticmethod
  def _get_sid_query(sid: str) -> str:
    """ Build query for SID filtration """
    if sid is None:
      return ''

    return f"""
      and
      EventData[
        Data[@Name='SubjectUserSid'] = '{sid}'
      ]
    """

  @staticmethod
  def build_xml_query_from_config(config: Config) -> str:
    """
    Complete query format

    *[
      System[
        Computer='COMPUTER_NAME'
        and
        (EventID=4688 or EventID=4689)
        and
        (
          TimeCreated[@SystemTime >= 'START_DATE']
          and
          TimeCreated[@SystemTime <= 'END_DATE']
        )
      ]
      and
      EventData[
        Data[
          @Name='SubjectUserSid'
        ] = 'USER_SID {FORMAT: S-1-5-21-KKKKKKKKKK-ZZZZZZZZZZ-XXXXXXXXX-YYYY}'
      ]
    ]
    """

    query = f"""
    *[
      System[
        {QueryManager._get_computer_query(config.remote_computer_name)}
        (EventID=4688 or EventID=4689)
        {QueryManager._get_date_query(config.start_date, config.end_date)}
      ] 
      {QueryManager._get_sid_query(config.sid)}
    ]
    """

    return query
