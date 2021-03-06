"""Functions to read data from disk.."""

import os
import random

def get_train_test_split(data_dir, train_test_ratio):
    all_files = os.listdir(data_dir)
    random.shuffle(all_files)
    split = int(train_test_ratio*len(all_files))
    return all_files[:split], all_files[split:]

def get_label_lookup(label_filename):
    label_lookup = {}
    with open(label_filename) as inf:
        for line in inf:
            label, filename = line.strip().split()
            label_lookup[filename] = label
    return label_lookup
