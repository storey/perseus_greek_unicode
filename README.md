# Perseus Greek Corpus (in Unicode)

Scripts for scraping the raw XML of texts in the [Perseus Greek Collection](http://www.perseus.tufts.edu/hopper/collection?collection=Perseus:collection:Greco-Roman). List correct as of December 2017.

Text is released under the [Creative Commons Attribution-ShareAlike 3.0 United States (CC BY-SA 3.0 US)](https://creativecommons.org/licenses/by-sa/3.0/us/)

Code is released under an MIT License. 

To run, use the command `python downloadTexts.py` (using python 3).

Results are stored in the `perseus_texts` folder . A list of available texts is included in `available.js`, and each file contains a JSON Object with
- The Author's name
- The Text's name
- The number of books
- A list of books with the raw XML (or a concatenation of raw XMLs) for that book.

A zip file of the texts is includes as `perseus_texts.zip`.
