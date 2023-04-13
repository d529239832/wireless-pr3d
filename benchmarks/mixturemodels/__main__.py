import getopt
import json
import multiprocessing as mp
import multiprocessing.context as ctx
import os
import signal
import sys
from pathlib import Path

import numpy as np
from loguru import logger

from .plot_evaluation import parse_plot_evaluation_args, plot_evaluation_main
from .train import parse_train_args, run_train_processes
from .prep_dataset import parse_prep_dataset_args, run_prep_dataset_processes
from .validate_pred import parse_validate_pred_args, run_validate_pred_processes
from .plot_prepped_dataset import parse_plot_prepped_dataset_args, run_plot_prepped_dataset_processes
from .evaluate_pred import parse_evaluate_pred_args, run_evaluate_pred_processes
from .plot_final_validate import parse_plot_final_validate_args, run_plot_final_validate_processes

# very important line to make tensorflow run in sub processes
ctx._force_start_method("spawn")
# disable GPU
os.environ["CUDA_VISIBLE_DEVICES"] = "-1"


if __name__ == "__main__":

    argv = sys.argv[1:]
    if argv[0] == "prep_dataset":
        validate_gym_args = parse_prep_dataset_args(argv[1:])
        run_prep_dataset_processes(validate_gym_args)
    elif argv[0] == "plot_prepped_dataset":
        validate_gym_args = parse_plot_prepped_dataset_args(argv[1:])
        run_plot_prepped_dataset_processes(validate_gym_args)
    elif argv[0] == "train":
        train_args = parse_train_args(argv[1:])
        run_train_processes(train_args)
    elif argv[0] == "validate_pred":
        validate_args = parse_validate_pred_args(argv[1:])
        run_validate_pred_processes(validate_args)
    elif  argv[0] == "plot_final_validate":
        plot_val_args = parse_plot_final_validate_args(argv[1:])
        run_plot_final_validate_processes(plot_val_args)
    elif argv[0] == "evaluate_pred":
        train_args = parse_evaluate_pred_args(argv[1:])
        run_evaluate_pred_processes(train_args)
    elif argv[0] == "plot_evaluation":
        plot_args = parse_plot_evaluation_args(argv[1:])
        plot_evaluation_main(plot_args)
    else:
        raise Exception("wrong command line option")
