class MissingRequiredArgumentException(Exception):
  def __init__(self):
    self.message = ''
    super().__init__("""
    The required param `name_or_ip` is missing. 
    Add --name_or_ip=YOUR_VALUE or simply YOUR_VALUE after main.py
    """)
