import pytest


# Source Code:

def from_roman(roman: str) -> int:
  # V_indices = roman.index('V')
  I_count = roman.count('I')

  return I_count



# Tests: 

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3)
  # ('IV', 4),
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman

