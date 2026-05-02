import os
import sys

# Adiciona o diretório do projeto no path
sys.path.insert(0, os.path.abspath('..'))

# -- Informações do projeto --
project = 'SXML Docs'
copyright = '2026, João'
author = 'João'
release = '0.1.0'

# -- Configurações gerais --
extensions = [
    'sphinx.ext.autodoc',      # puxa docstrings do código
    'sphinx.ext.napoleon',     # suporte a Google/NumPy docstrings
    'sphinx.ext.viewcode',     # mostra código fonte
]

templates_path = ['_templates']
exclude_patterns = []

# -- HTML output --
html_theme = 'alabaster'  # tema padrão (pode trocar depois)
html_static_path = ['_static']
