# COMP550 FinalProject

## Data importation
Download the 'books_and_genres.csv' file from https://www.kaggle.com/datasets/michaelrussell4/10000-books-and-their-genres-standardized/data 

To use the Gutenberg module, if you are located in Canada you need to change the Gutenberg mirror. The list of all available mirrors can be found at https://www.gutenberg.org/MIRRORS.ALL. 
This can be done in the terminal, using the following command: 
``` 
export GUTENBERG_MIRROR='http://mirror.csclub.uwaterloo.ca/gutenberg/' 
```
or, if you are using a conda environment:
``` 
conda env config vars set GUTENBERG_MIRROR='http://mirror.csclub.uwaterloo.ca/gutenberg/' 
``` 