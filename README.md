# Introduction
This repo allows a quick image classification with the tensorflow inception model through transfer learning.

All you need are pictures you want to classify and put them in the folder `train_images`. You need to put the pictures of each class into its own folder. See below.

## Requirements

**Software**
- NVidia Driver + CUDA
- Docker
- nvidia-docker

**Other**
- 200 more images per class in jpg format
  + e.g. To distinguish between dogs and cats, 200 images each (the more the better) should suffice to achieve acceptable results.
- Some images to test our image classification on (also in jpg format)

## Folder structure 
Fill the folder train\_images with images you want to classify. Each class gets its own folder with the images who belong to that class


### Example

We have 2 classes, puppies and kitties with 200 pictures each:


```
./kitty
           /kitty001.jpg
           /kitty002.jpg
           /kitty003.jpg
       ...
           /kitty198.jpg
           /kitty199.jpg
           /kitty200.jpg

./puppy
           /puppy001.jpg
           /puppy002.jpg
           /puppy003.jpg
       ...
           /puppy198.jpg
           /puppy199.jpg
           /puppy200.jpg

```


# Training

To train the images in `train_images` just execute:

```
./train_gpu.sh # if you have a gpu
./train_cpu.sh # when you only have a cpu
```

# Testing
After the training put some images you want to classify into the `test_images` folder, this folder requires no subfolders. 

Execute:
```
./guess.sh # uses cpu, we dont require that much computing power
```
