# im2p-tensorflow

I have referred this code from [im2p] (https://github.com/chenxinpeng/im2p)


Refered Paper:  [A Hierarchical Approach for Generating Descriptive Image Paragraphs](http://cs.stanford.edu/people/ranjaykrishna/im2p/index.html)


# im2p
This is draft Version of the code.

## Step 1 : Data preprocess
Download the [VisualGenome dataset](http://visualgenome.org/), we get the two files: VG_100K, VG_100K_2. According to the paper, we download the training, val and test splits json files. These three json files save the image names of train, validation, test data. 

Running the script:
```bash
$ python split_dataset
```
We will get images from [VisualGenome dataset] which the authors used in the paper.We will get three json files: imgs_train_path.json, imgs_val_path.json, imgs_test_path.json. They save the train, val, test images path.

##Step 2 : To extract image feature 

After this, we use `dense caption` to extract features. Deploy the running environment follow by [densecap](https://github.com/jcjohnson/densecap) step by step.

Part 1:
Run the script:
```bash
$ ./download_pretrained_model.sh
```
We should download the pre-trained model: `densecap-pretrained-vgg16.t7`. 
Part 2: Load jsons and run corresponding script 

```bash
$th extract_features.lua -boxes_per_image 50 -max_images -1 -input_txt imgs_train_path.json -output_h5 ./data/im2p_train_output.h5 -gpu 1 -use_cudnn 1

```
Then, according to the paper, we extract **50 boxes** from each image. 

Also, don't forget extract val images and test images features:
```bash
$ th extract_features.lua -boxes_per_image 50 -max_images -1 -input_txt imgs_val_path.json   -output_h5 ./data/im2p_val_output.h5 -gpu 1 -use_cudnn 1                          
$ th extract_features.lua -boxes_per_image 50 -max_images -1 -input_txt imgs_test_path.json  -output_h5 ./data/im2p_test_output.h5 -gpu 1 -use_cudnn 1
```

## Step 3
Run the script:
```bash
$ python parse_json.py
```
In this step, we process the `paragraphs_v1.json` file for training and testing. We get the `img2paragraph` file on curent folder, Move that fiel to  **./data** directory. 
Its structure is like this:
![img2paragraph](https://github.com/chenxinpeng/im2p/blob/master/img/4.png)

## Step 4
Finally, we can train and test model, in the terminal:
```bash
$ CUDA_VISIBLE_DEVICES=0 ipython
>>> import HRNN_paragraph_batch
>>> HRNN_paragraph_batch.train()
```
After training, we can test the model:
```bash
>>> HRNN_paragraph_batch.test()


