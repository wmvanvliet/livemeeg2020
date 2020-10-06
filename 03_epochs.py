"""
Cut epochs and compute the evoked potential.
"""
import mne
from argparse import ArgumentParser

from config import fname, event_id, tmin, tmax, baseline

parser = ArgumentParser()
parser.add_argument('subject', type=int, help='The subject to process [1-71]')
args = parser.parse_args()

filtered = mne.io.read_raw_fif(fname.filtered(subject=args.subject))
events = mne.find_events(filtered, stim_channel='Target')
epochs = mne.Epochs(filtered, events, event_id, tmin, tmax, baseline)

ev_target = epochs['target'].average()
ev_nontarget = epochs['nontarget'].average()

epochs.save(fname.epochs(subject=args.subject), overwrite=True)
mne.write_evokeds(fname.evokeds(subject=args.subject), [ev_target, ev_nontarget])
