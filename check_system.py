"""
This script performs a series of checks on the system to see if everything is
ready to run the analysis pipeline.
"""

import os
import pkg_resources

# Check to see if the python dependencies are fullfilled.
dependencies = []
with open('./requirements.txt') as f:
    for line in f:
        line = line.strip()
        if len(line) == 0 or line.startswith('#'):
            continue
        dependencies.append(line)

# This raises errors of dependencies are not met
pkg_resources.working_set.require(dependencies)

# Check that the data is present on the system
from config import fname
if not os.path.exists(fname.raw_data_dir):
    raise ValueError('The `raw_data_dir` points to a directory that does not exist: ' + fname.raw_data_dir)

# Make sure the output directories exist
os.makedirs(fname.processed_data_dir, exist_ok=True)
os.makedirs(fname.figures_dir, exist_ok=True)
os.makedirs(fname.reports_dir, exist_ok=True)

# Prints some information about the system
import mne
mne.sys_info()

with open(fname.system_check, 'w') as f:
    f.write('System check OK.')

print("\nAll seems to be in order.\nYou can now run the entire pipeline with: python -m doit")
