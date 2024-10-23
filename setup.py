from setuptools import setup, find_packages


with open(file="requirements.txt", mode="r") as f:
    requirements = f.read().splitlines()

with open(file="README.md", mode="r") as f:
    long_description = f.read()

DESCRIPTION = "Utilizing web scraping and machine learning techniques to accurately predict '(خ5سات)' service prices"

dependency_links = ["https://pypi.org/project/selenium/4.25.0", "https://pypi.org/project/pandas/2.2.3"]

setup(name="Khamsat (خ5سات) Predictor",
      packages=find_packages(),
      dependency_links=dependency_links,
      author="Ismael Mousa",
      author_email="ismaelramzimousa@gmail.com",
      description=DESCRIPTION,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/IsmaelMousa/khamsat-predictor",
      install_requires=requirements,
      python_requires=">=3.10",
      license="MIT", )
