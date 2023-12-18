from typing import Any, NoReturn


def void(*args: Any, **kwargs: Any) -> None:
  """Synchronous voider: take any arguments and do nothing, useful in functions that require an argument when nothing is needed to be done."""


async def avoid(*args: Any, **kwargs: Any) -> None:
  """Asynchronous voider: take any arguments and do nothing, useful in functions that require an argument when nothing is needed to be done."""


def raiser(e: Exception) -> NoReturn:
  """With decorator-like structure return a synchronous callable which raises specified exception on call, no matter what (with *args, **kwargs which are ignored)."""
  def inner_raiser(*args, **kwargs):
    raise e
  return inner_raiser

async def araiser(e: Exception) -> NoReturn:
  """With decorator-like structure return a synchronous callable which raises specified exception on call, no matter what (with *args, **kwargs which are ignored)."""
  async def inner_raiser(*args, **kwargs):
    raise e
  return inner_raiser
