import time
from typing import Any, Generator


def typewriter(text: str) -> Generator[None, None, None]:
  for char in text:
    print(char, end='', flush=True)
    time.sleep(0.1)
  print()
