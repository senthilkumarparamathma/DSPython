class Utill:
  def __init__(self):
    self.data = {"I":1,"V":5, "X":10,"L":50,"C":100,"D":500,"M":1000}
  def romanToInt(self,word):
    total = 0
    prev = 0
    for char in word:
      current = self.data[char]
      total += current

      if current > prev:
        total -= 2 * prev
      prev = current

    return total

  def printRoman(self, number):
      num = [1, 4, 5, 9, 10, 40, 50, 90,
             100, 400, 500, 900, 1000]
      sym = ["I", "IV", "V", "IX", "X", "XL",
             "L", "XC", "C", "CD", "D", "CM", "M"]
      i = 12
      result = ""
      while number:
          div = number // num[i]

          number %= num[i]
          # print(number)
          while div:
              print(div)
              print("loop")
              # print(sym[i], end = "")
              result += sym[i]
              div -= 1
          i -= 1
      return result