"""
===========
Config file
===========

Configuration parameters for the study.
"""

import os
import getpass
from socket import getfqdn
from fnames import FileNames

###############################################################################
# Determine which user is running the scripts on which machine and set the path
# where the data is stored and how many CPU cores to use.

user = getpass.getuser()  # Username of the user running the scripts
host = getfqdn()  # Hostname of the machine running the scripts

# You want to add your machine to this list
if user == 'wmvan':
    # My laptop
    raw_data_dir = 'C:/Users/wmvan/data/livemeeg2020'
    n_jobs = 6  # My laptop has 6 cores
elif host == 'nbe-024.org.aalto.fi' and user == 'vanvlm1':
    # My workstation
    raw_data_dir = './data'
    n_jobs = 8  # My workstation has 8 cores
else:
    raise RuntimeError('Running on an unknown system. Please add your system '
                       'configuration to the config.py file.')

# For BLAS to use the right amount of cores
os.environ['OMP_NUM_THREADS'] = str(n_jobs)


###############################################################################
# These are all the parameters that either:
#  1) Are used in more than one script
#  2) Need to be reported in the Methods section of the paper

# Subject information
all_subjects = range(1, 72)
bad_subjects = [62, 64, 63, 65, 66, 67, 68, 69, 70, 71]
subjects = [s for s in all_subjects if s not in bad_subjects]

# Bandpass filter
sample_rate = 512.  # Hz
fmin = 0.5  # Hz
fmax = 30.0  # Hz

# Epochs
event_id = dict(nontarget=1, target=2)
tmin, tmax = (-0.2, 1.0)
baseline = (-0.2, 0)


###############################################################################
# Templates for filenames
#
# This part of the config file uses the FileNames class. It provides a small
# wrapper around string.format() to keep track of a list of filenames.
# See fnames.py for details on how this class works.
fname = FileNames()

# Some directories
fname.add('data_dir', raw_data_dir)
fname.add('processed_data_dir', '{data_dir}/processed')
fname.add('figures_dir', './figures')

fname.add('url', 'https://zenodo.org/record/3266223/files/subject_{subject:02d}.zip?download=1')
fname.add('mat', '{data_dir}/subject_{subject:02d}.mat')
fname.add('filtered', '{processed_data_dir}/subject_{subject:02d}_filt_raw.fif')
fname.add('epochs', '{processed_data_dir}/subject_{subject:02d}_epo.fif')
fname.add('evokeds', '{processed_data_dir}/subject_{subject:02d}_ave.fif')

# Grand average analysis
fname.add('ga_evokeds', '{processed_data_dir}/grand_average_evokeds_ave.fif')

# Figures
fname.add('figure_ga_evokeds', '{figures_dir}/grand_average_evokeds_ave.pdf')

# File produced by check_system.py
fname.add('system_check', './system_check.txt')
