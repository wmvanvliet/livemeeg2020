"""
===========
Config file
===========

Configuration parameters for the study.
"""

import os
import getpass
from socket import getfqdn
from filename_templates import FileNames

###############################################################################
# Determine which user is running the scripts on which machine and set the path
# where the data is stored and how many CPU cores to use.

user = getpass.getuser()  # Username of the user running the scripts
host = getfqdn()  # Hostname of the machine running the scripts

# You want to add your machine to this list
if user == "wmvan":
    # My laptop
    raw_data_dir = "C:/Users/wmvan/data/livemeeg2020"
    n_jobs = 14  # My laptop has 14 cores
elif host == "nbe-024.org.aalto.fi" and user == "vanvlm1":
    # My workstation
    raw_data_dir = "./data"
    n_jobs = 8  # My workstation has 8 cores
else:
    raise RuntimeError(
        "Running on an unknown system. Please add your system "
        "configuration to the config.py file."
    )

# For BLAS to use the right amount of cores
os.environ["OMP_NUM_THREADS"] = str(n_jobs)


###############################################################################
# These are all the parameters that either:
#  1) Are used in more than one script
#  2) Need to be reported in the Methods section of the paper

# Subject information
all_subjects = range(1, 72)
bad_subjects = [62, 64, 63, 65, 66, 67, 68, 69, 70, 71]
subjects = [s for s in all_subjects if s not in bad_subjects]

# Bandpass filter
sample_rate = 512.0  # Hz
fmin = 0.5  # Hz
fmax = 30.0  # Hz


###############################################################################
# Templates for filenames
#
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

# Some directories
fname.add("data_dir", raw_data_dir)
fname.add("processed", "{data_dir}/processed")

# Original files.
fname.add(
    "url",
    "https://zenodo.org/record/3266223/files/subject_{subject:02d}.zip?download=1",
    as_str=True,
)
fname.add("mat", "{data_dir}/subject_{subject:02d}.mat")

# Processed files.
fname.add("filtered", "{processed}/subject_{subject:02d}_filt_raw.fif", mkdir=True)

# File produced by check_system.py
fname.add("system_check", "./system_check.txt")
