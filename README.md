# PCInternQuiz
PicCollage Intern Quiz


## Dependency

This project is dependent on Python 

- keras == 2.2.0
- numpy == 1.14.0
- pandas == 0.22.0
- matplotlib == 2.1.2

## Usage

### Folder and Dataset

To start this project we have to download dataset from Kaggle and put those file to `./input/audio_train` and `./input/audio_test` .
 
    .
    ├── ..
    ├── PrePro.py                           # preprocessing 
    ├── Train_Generator.ipynb               # training using data generator
    ├── Train_Resize.ipynb                  # resize the images before training
    ├── data 
    │   ├── train_responses.csv             # training list
    |   └── train_imgs                     
    |       ├── *.png                       # training images
    |       └── ...                   
    └── ...

### Data Preprocessing 

Before training:

```shell
python3 PrePro.py 
```

### Training

To train a model, you could choose one of the ipython-notebook to do so.


## Reference

- [Guess The Correlation](http://guessthecorrelation.com/)


  ​
