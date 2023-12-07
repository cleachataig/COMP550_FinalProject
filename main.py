import os

from gutenberg.acquire import load_etext
from gutenberg.cleanup import strip_headers

text = strip_headers(load_etext(2701)).strip()
print(text)  # prints 'MOBY DICK; OR THE WHALE\n\nBy Herman Melville ...'