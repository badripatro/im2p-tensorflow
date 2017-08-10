#! encoding: UTF-8

import os
import glob
import json
import subprocess


genome_VG_100K_path = "data/genome/VG_100K"
genome_VG_100K_2_path = "data/genome/VG_100K_2"

train_json_path = "data/train_split.json"
val_json_path = "data/val_split.json"
test_json_path = "data/test_split.json"

train_savepath = "data/genome/im2p_train"
val_savepath = "data/genome/im2p_val"
test_savepath = "data/genome/im2p_test"

all_images = glob.glob(genome_VG_100K_path + "/*.jpg")
all_images_2 = glob.glob(genome_VG_100K_2_path + "/*.jpg")

for item in all_images_2:
    all_images.append(item)

with open(train_json_path, "r") as fr1:
    train_names = json.load(fr1)

with open(val_json_path, "r") as fr2:
    val_names = json.load(fr2)

with open(test_json_path, "r") as fr3:
    test_names = json.load(fr3)

print "train images num: {}".format(len(train_names))
print "val images num: {}".format(len(val_names))
print "test images num: {}".format(len(test_names))

im2p_train_json={}
im2p_val_json={}
im2p_test_json={}
im2p_train_json['images_path'] = []
im2p_test_json['images_path'] = []
im2p_val_json['images_path'] = []
for idx, img in enumerate(all_images):
    print "idx: {}  {}".format(idx, img)
    img_name = int(os.path.basename(img).split(".")[0])
    if img_name in train_names:
        im2p_train_json['images_path'].append(img)
        #subprocess.call(["cp", img, train_savepath])
    elif img_name in val_names:
        im2p_val_json['images_path'].append(img)
        #subprocess.call(["cp", img, val_savepath])
    elif img_name in test_names:
        im2p_test_json['images_path'].append(img)
        #subprocess.call(["cp", img, test_savepath])

json.dump(im2p_train_json, open('imgs_train_path.json', 'w'))

json.dump(im2p_test_json, open('imgs_test_path.json', 'w'))

json.dump(im2p_val_json, open('imgs_val_path.json', 'w'))

 
