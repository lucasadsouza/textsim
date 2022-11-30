# TextSim

A module that offers text similarity tools.

## Features:
- **similarity:** Rates from 0.0 to 1.0 the similarity between a string and a list of strings.
- **matrix similarity**: Rates from 0.0 to 1.0 the similarity between a string and a matrix of strings.
- **most similar:** Returns the most similar text after using similarity or matrix similarity methods.

### Available Methods:
- Jaro Jaro Winkler formula.


## Quick Example:
```python
import textsim


txtsim = textsim.text_similarity.TextSim('jaro_winkler')

texts = ['My dog barked to my neighbour', 'My cat seems to like it', 'I run everyday']

txtsim.similarity('My dog barks', texts)


print(txtsim.sim.values)
# output: [1.0, 0.7700483092, 0.6428571429]

print(txtsim.most_similar())
# output: (['My dog barked to my neighbour'], [1.0])
```

_* It is updated according personal needs._
