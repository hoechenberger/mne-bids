"""MNE software for easily interacting with BIDS compatible datasets."""

__version__ = '0.11.dev0'
from . import commands
from .report import make_report
from .path import (BIDSPath, get_datatypes, get_entity_vals,
                   print_dir_tree, get_entities_from_fname,
                   search_folder_for_text, get_bids_path_from_fname)
from .read import get_head_mri_trans, read_raw_bids
from .utils import get_anonymization_daysback
from .write import (make_dataset_description, write_anat,
                    write_raw_bids, mark_channels,
                    write_meg_calibration, write_meg_crosstalk,
                    get_anat_landmarks, anonymize_dataset)
from .sidecar_updates import update_sidecar_json, update_anat_landmarks
from .inspect import inspect_dataset
from .dig import (template_to_head, convert_montage_to_ras,
                  convert_montage_to_mri)
