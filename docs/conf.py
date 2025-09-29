# -*- coding: utf-8 -*-
"""Sphinx configuration file."""
import time
import sphinx_rtd_theme

author = "Pitasc Team"
project = "pitasc"
release = "master"
version = "master"
copyright = "{}, {}".format(time.strftime("%Y"), author)

html_theme = "sphinx_rtd_theme"
html_theme_options = {
}
html_last_updated_fmt = "%c"
master_doc = "index"
pygments_style = "friendly"
templates_path = ["_templates"]
extensions = [
    "sphinx_rtd_theme",
    "sphinx_multiversion",
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_copybutton",
]

smv_tag_whitelist = r'^\d+\.\d+\.\d+$' # all version tags
smv_branch_whitelist = r'^master$' # 'master' branch only
smv_remote_whitelist = None # local branches only
smv_released_pattern = r'tags/^\d+\.\d+\.\d+$' # only version tags are released
