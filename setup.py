import os, re
import setuptools


requirements = []
with open(os.path.join('config', 'requirements.txt')) as f:
  requirements = f.read().splitlines()


constants = ['project', 'version', 'author', 'authoremail', 'url']
constants_values = []
with open(os.path.join('textsim', '__init__.py')) as f:
  file_ = f.read()
  for const in constants:
    match = re.search(r'^__' + const + r'__\s=\s[\'"]([^\'"]*)[\'"]', file_, re.MULTILINE)

    if match is None or match.group(1) is None:
      raise RuntimeError(f'Module {const} constant not found.')

    constants_values.append(match.group(1))

PROJECT = constants_values[0]
VERSION = constants_values[1]
AUTHOR = constants_values[2]
AUTHOREMAIL = constants_values[3]
URL = constants_values[4]


DESCRIPTION = ''
with open(os.path.join('textsim', '__init__.py')) as f:
  file_ = f.readlines()[3]

  DESCRIPTION = file_.replace('\n', '')


LONGDESCRIPTION = ''
with open('README.md') as f:
  LONGDESCRIPTION = f.read()


setuptools.setup(
  name=PROJECT, 
  version=VERSION,
  author=AUTHOR,
  url=URL,
  author_email=AUTHOREMAIL,
  description=DESCRIPTION,
  long_description=LONGDESCRIPTION,
  long_description_content_type='text/markdown',
  packages=[PROJECT],
  package_dir={PROJECT: PROJECT},
  install_requires=requirements
)
