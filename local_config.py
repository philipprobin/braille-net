# coding: utf-8
"""
Local settings
"""
from pathlib import Path

# base directory of this repository
root_path = Path(__file__).parent

# path for application data such as weights
data_path = str(root_path)

# location of third party tools if any
global_3rd_party = str(root_path)

# location of labeled data used for training
dataset_path = str(root_path / "AngelinaDataset")

# prefix for liblouis tables, keep empty by default
liblouis_tables_path_prefix = ""
