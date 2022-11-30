from textsim.methods import JaroWinkler


jarowinkler = JaroWinkler()
similarity_methods = {
  'jaro_winkler': jarowinkler.get_jaro_winkler
}


class Sim():
  def __init__(self, compared_value: str=None, values: list[float]=[], texts: list[str]=[]):
    self.compared_value = compared_value
    self.values = values
    self.texts = texts
    self.sorted_values = None
    self.sorted_texts = None

  def sort(self):
    self.sorted_values = sorted(self.values, reverse=True)

    self.sorted_texts = []
    for sorted_value in self.sorted_values:
      idx = self.values.index(sorted_value)
      self.sorted_texts.append(self.texts[idx])

    return self

  def __repr__(self): # Pretty print the class
    return f"<textsim.Sim compared_value: '{self.compared_value}', values: {self.values}, texts: {self.texts}, sorted_values: {self.sorted_values}, sorted_texts: {self.sorted_texts}>"

class SimMatrix():
  def __init__(self, compared_value: str=None, values: list[list[float]]=[], texts: list[list[str]]=[]):
    self.compared_value = compared_value
    self.values = values
    self.texts = texts
    self.sorted_values = None
    self.sorted_texts = None

  def new_matrix_layer(self):
    self.values.append([])
    self.texts.append([])

  def sort(self):
    self.sorted_values = []
    self.sorted_texts = []

    for values in self.values:
      self.sorted_values.append(sorted(values, reverse=True))

    for i, sorted_values in enumerate(self.sorted_values):
      self.sorted_texts.append([])
      for sorted_value in sorted_values:
        idx = self.values[i].index(sorted_value)
        self.sorted_texts[i].append(self.texts[idx])

    return self

  def __repr__(self): # Pretty print the class
    return f"<textsim.Sim compared_value: '{self.compared_value}', values: {self.values}, texts: {self.texts}, sorted_values: {self.sorted_values}, sorted_texts: {self.sorted_texts}>"


class TextSim():
  def __init__(self, similarity_method='jaro_winkler'):
    self.similarity_method = similarity_methods[similarity_method]
    self.sim = None

  def similarity(self, text: str, data: list[str]):
    self.sim = Sim(text, [], [])

    for data_text in data:
      sim = self.similarity_method(text, data_text)

      if sim > 0 and sim in self.sim.values:
        sim = sim - 0.0000000001

      self.sim.values.append(sim)
      self.sim.texts.append(data_text)

    self.sim.sort()

    return self

  def generate_matrix(self, data: list[list[str]]) -> list[list[str]]:
    matrix_size = len(max(data, key=len))

    return (matrix_size, [i+ [''] * (matrix_size - len(i)) for i in data])

  def matrix_similarity(self, text: str, data: list[list[str]]):
    self.sim = SimMatrix(text, [], [])
    matrix_size, matrix_data = self.generate_matrix(data)

    for i, list_data in enumerate(matrix_data):
      self.sim.new_matrix_layer()

      for data_text in list_data:
        sim = self.similarity_method(text, data_text)

        if sim > 0 and sim in self.sim.values[i]:
          sim = sim - 0.0000000001

        self.sim.values[i].append(sim)
        self.sim.texts[i].append(data_text)

    self.sim.sort()

    return self

  def most_similar(self, max_: int=1) -> str:
    if type(self.sim) == SimMatrix:
      merged_values = []
      merged_texts = []

      for i in range(0, len(self.sim.values)):
        merged_values.extend([x for x in self.sim.values[i] if x not in ('', 0.0)])
        merged_texts.extend([x for x in self.sim.texts[i] if x not in ('', 0.0)])

      merged_sim = Sim(texts=merged_texts, values=merged_values)
      merged_sim.sort()

      return (merged_sim.sorted_texts[:max_], merged_sim.sorted_values[:max_])
    
    return (self.sim.sorted_texts[:max_], self.sim.sorted_values[:max_])

# textsim = TextSim('jaro_winkler')

# textsim.matrix_similarity('aaa', [['aaa', 'sdbf', 'agads'], ['ahggf'], ['gshdfgh', 'hdtg', 'jryjy', 'dtjjtr']])

# print(textsim.most_similar())
# print(textsim.sim)