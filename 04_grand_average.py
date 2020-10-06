"""
Computes the grand average evoked potentials.
"""
import mne

from config import fname, subjects

ev_targets = []
ev_nontargets = []
for subject in subjects:
    ev = mne.read_evokeds(fname.evokeds(subject=subject), condition='target')
    ev_targets.append(ev)
    ev = mne.read_evokeds(fname.evokeds(subject=subject), condition='nontarget')
    ev_nontargets.append(ev)
ga_target = mne.grand_average(ev_targets) 
ga_nontarget = mne.grand_average(ev_nontargets) 
