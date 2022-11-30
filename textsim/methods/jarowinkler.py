class JaroWinkler():
  def jaro (self, text1: str, text2: str):
    if text1 == '':
      return 0.0

    m = 0
    s1 = len(text1)
    s2 = len(text2)
    t = 0
    dFactor = max(s1, s2) / 2 - 1
    match = ''
    dMatch = ''
    clone1 = ''
    clone2 = ''
    inputList = ''
    matchList = ''

    if text1 == text2:
      return 1.0

    clone1 = text2
    inputList = list(text1)

    for current in inputList:
      if current in clone1:
        clone1 = clone1.replace(current, '', 1)

        match += current
        m += 1

    if m == 0:
      return 0.0

    clone1 = text1
    clone2 = text2
    matchList = list(match)

    for current in matchList:
      if clone1[clone1.find(current)] != clone2[clone2.find(current)]:
        clone1.replace(current, '', 1)
        clone2.replace(current, '', 1)

        dMatch += current

    clone1 = text1
    clone2 = text2
    matchList = list(dMatch)

    for current in matchList:
      if clone1.find(current) > clone2.find(current):
        if (clone1.find(current) - clone2.find(current)) > dFactor:
          clone1.replace(current, '', 1)
          clone2.replace(current, '', 1)

          t += 1

        elif (clone2.find(current) - clone1.find(current)) > dFactor:
          clone1.replace(current, '', 1)
          clone2.replace(current, '', 1)

          t += 1

    return (m / s1 + m / s2 + (m - t) / m) * 1 / 3


  def jaro_winkler (self, text1: str, text2: str):
    text1 = text1.lower()
    text2 = text2.lower()

    simJ = self.jaro(text1, text2)

    if simJ == 0.0:
      return 0.0
    
    elif simJ == 1.0:
      return 1.0

    p = 0.1
    l = 0

    if len(text2) < len(text1):
      comparison = text2
    
    else:
      comparison = text1

    for i in range(0, len(comparison)):
      if text2[i] != text1[i]:
        break

      l += 1
      
    simW = simJ + ((l * p) * (1 - simJ))

    if simW >= 1.0:
      return 1.0

    return simW

  def get_jaro_winkler(self, text1: str, text2: str):
    return round(self.jaro_winkler(text1, text2), 10)
