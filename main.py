import pytest


# Source Code:

def from_roman(roman: str) -> int:
#  length_roman = len(roman)

  if 'V' in roman:
    V_indices = roman.index('V')

    if V_indices == 1:
      number = 4
    elif V_indices == 0:
      number = 5
  else:  
    I_count = roman.count('I')
    number = I_count

  return number



# Tests: 

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
  ('IV', 4),
  ('V', 5)
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman

