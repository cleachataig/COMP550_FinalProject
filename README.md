<h2 align="center">COMP550 - Final Project</h2>

## Description

This is the code repository for our final project work for the course COMP550 Natural Language Processing at McGill University. See the final report for detail on the theory and the methodology.

## Data importation
Download the 'books_and_genres.csv' file from https://www.kaggle.com/datasets/michaelrussell4/10000-books-and-their-genres-standardized/data (about 3.6GB).

To use the Gutenberg module, if you are located in Canada, you need to change the Gutenberg mirror. The list of all available mirrors can be found at https://www.gutenberg.org/MIRRORS.ALL. 
This can be done in the terminal, using the following command: 
``` 
export GUTENBERG_MIRROR='http://mirror.csclub.uwaterloo.ca/gutenberg/' 
```
or, if you are using a conda environment,:
``` 
conda env config vars set GUTENBERG_MIRROR='http://mirror.csclub.uwaterloo.ca/gutenberg/' 
``` 
The Gutenberg module is not used so this requirement is not mandatory but it could be useful if you wanted to expand the project.

## Usage

1. You can first install a new virtual environment with the required python packages from `requirements.txt`.
2. Then create an empty directory `data` in the home directory.
3. Download the 'books_and_genres.csv' file in the directory `data`.
4. Then run the whole notebook `data_importation.ipynb`. This will save the necessary X and y files to train the models. We also provided those in a .zip archive because the pre-processing can be quite long to run.
5. Once you have run the importation and pre-processing code, you can analyze the built datasets in the notebook `data_analysis.ipynb`.
6. For the genre prediction task, see the notebook `genre_prediction.ipynb`.
7. For the chapter clustering task, see the notebook `chapter_clustering.ipynb`.
