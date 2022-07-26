"""Sphinx configuration."""
project = "Git Archive Deep"
author = "CD Clark III"
copyright = "2022, CD Clark III"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
