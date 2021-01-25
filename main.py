import pytest


# Source Code:

def from_roman(roman: str) -> int:
#  length_roman = len(roman)
  V_number = 0
  I_number = 0

  if 'V' in roman:
    V_indices = roman.index('V')

    if V_indices == 1:
      V_number = 4
    elif V_indices == 0:
      V_number = 5
      I_after_V = roman.count('I', V_indices)
      I_number = I_after_V
  else:  
    I_count = roman.count('I')
    I_number = I_count
    
  number = V_number + I_number
  return number 



# Tests: 

cases = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
  ('IV', 4),
  ('V', 5),
  ('VI', 6),
  ('VII', 7),
  ('VIII', 8)
]
@pytest.mark.parametrize(['num', 'roman'], cases)
def test_roman_1(num: int, roman: str):
  assert from_roman(num) == roman

