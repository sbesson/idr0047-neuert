#!/usr/bin/env python
# Generate companion files


import glob
import os

BASE_DIRECTORY = os.environ.get(
    "BASE_DIRECTORY",
    "/uod/idr/filesets/idr0047-neuert-yeastmRNA/20181016-ftp")
RAW_IMAGES_DIR = "#1_Raw_Images"
ANALYZED_IMAGES_DIR = "#2_Analyzed_images"

# Based on Table 2: Experimental data sets and conditions
EXPERIMENTS = {
    'Exp1_rep1': [0, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Exp1_rep2': [0, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Exp2_rep1': [0, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Exp2_rep2': [0, 1, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55],
    'Exp2_rep3': [0, 2, 4, 6, 8, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55]
    }
POSITIONS = ['im1', 'im2', 'im3', 'im4']

# Missing raw images as confirmed by the submitters
MISSING_IMAGES = set([
    'Exp1_rep1_50min_im4.tif',
    'Exp1_rep2_50min_im4.tif',
    'Exp2_rep3_40min_im3.tif'])

# Review raw images
raw_images_list = map(
    os.path.basename,
    glob.glob("%s/*/%s/*" % (BASE_DIRECTORY, RAW_IMAGES_DIR)))
expected_images_list = [
    '%s_%gmin_%s.tif' % (x, y, z) for x in EXPERIMENTS for
    y in EXPERIMENTS[x] for z in POSITIONS]
missing_raw_images = set(expected_images_list) - set(raw_images_list)
assert missing_raw_images == MISSING_IMAGES, missing_raw_images
# TODO: check all extra images end with im5.tif to im8.tif
extra_raw_images = set(raw_images_list) - set(expected_images_list)


sd_mRNA_mat_list = map(
    os.path.basename,
    glob.glob("%s/*/%s/SD_mRNA*.mat" % (BASE_DIRECTORY, ANALYZED_IMAGES_DIR)))
expected_mat_list = ['SD_mRNA_%s.mat' % x[:-4] for x in raw_images_list]
assert not sorted(set(expected_mat_list) - set(sd_mRNA_mat_list))
assert not sorted(set(sd_mRNA_mat_list) - set(expected_mat_list))
