"""
Create figure 1 in the manuscript.
Grand average evoked potentials.
"""

import mne
from matplotlib import pyplot as plt

from config import fname

ga_evokeds = mne.read_evokeds(fname.ga_evokeds)
mne.viz.plot_evoked_topo(ga_evokeds, show=False)
plt.savefig(fname.figure_ga_evokeds)
