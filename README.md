# Game theory applied to cancer cells
 
This folder contains the code for a study that was carried out as part of my undergraduate thesis, which consisted of predicting, by means of game theory, how the cells of a cancerous organism would evolve according to the tumor suppressor alleles they had (two, one or none).

To do this, formulas obtained from a previous article that had already raised this idea were followed and a simplex was used to represent the evolution of these cells according to the formulas of the aforementioned article.

The code was made using the python programming language whose objective was to identify the type of cells found in an image (made by hand where the pixels were of three colors, red for cells that did not have tumor suppressor alleles, yellow for those that had only one allele and green for those that had both) that represented possible real tumors. Once these cells and their disposition were identified, the probability with which they could transform into cancer cells or recover their healthy state was calculated.

However, as this was a final degree project, the results were manually altered so that the formulas would give a more attractive result and different evolutions of the cells towards the different vertices of the triangle could be seen. Also, as this was a final degree project, the code and the memory are in Spanish.
