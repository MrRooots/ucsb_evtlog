from datetime import datetime


class Timer:
  @staticmethod
  def timeit(func):
    def wrapper(*args, **kwargs):
      start = datetime.now()
      res = func()
      time = datetime.now() - start

      d = {}
      d["hours"], rem = divmod(time.seconds, 3600)
      d["minutes"], d["seconds"] = divmod(rem, 60)

      print('Completed in {minutes} min {seconds} sec'.format(**d))

      return res

    return wrapper
