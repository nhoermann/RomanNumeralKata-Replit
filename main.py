import pytest

# Source Code:

def from_roman(roman: str) -> int:
  
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

# Working version:
def from_roman3(roman: str) -> int:
  
  roman_numbers = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }
  rev_roman = roman[::-1]

  number = 0
  last_number = 0

  for roman_number in rev_roman:
    current_number = roman_numbers[roman_number]

    if current_number >= last_number:
      number = number + current_number
    else:
      number = number - current_number

    last_number = current_number

  return number


# Tests: 

cases2 = [
  ('I', 1),
  ('II', 2),
  ('III', 3),
  ('IV', 4),
  ('V', 5),
  ('VI', 6),
  ('VII', 7),
  ('VIII', 8),
  ('IX', 9),
  ('X', 10),
  ('XII', 12),
  ('LXXIX', 79),
  ('MMXXI', 2021)

]

@pytest.mark.parametrize(['num', 'roman'], cases2)
def test_roman_1(num: int, roman: str):
  assert from_roman3(num) == roman


