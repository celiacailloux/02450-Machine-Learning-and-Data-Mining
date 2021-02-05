# Machine-Learning-and-Data-Mining-Examples

Modified scripts from [ML course 02450](https://kurser.dtu.dk/course/02450) from Technical University of Denmark. The scripts have been modified for custom use (e.g. **automation** of various processes, use of **pandas** rather than numpy arrays and such). See topics in *About* and go to the folder [figures](figures) to get a quick overview of the conducted data analysis and visualization. 

## Course Structure and Content

The course is build in three phases:
1. **Data** Feature extraction and Visualization
2. **Supervised Learning** Classification Regression
3. **Unsupervised Learning** Clustering and Density Estimation

## figures
In the folder [figures](figures) all computed figures from the scripts in the folder [scripts](scripts) are saved. The figures are named after the script name, and are, as for now, in chronilogical order with respect to the ML course 02459 from Technical Univisersity of Denmark. 

- [ ] Rename scripts to mirror contect

## Toolboxes

The apriori method included in the *Tools* is taken from http://www.borgelt.net/apriori.html, for
details of the algorithm see also http://www.borgelt.net/doc/apriori/apriori.

## Packages

- matplotlib (imshow, ...)
- os, sys
- pandas, numpy
- scipy
- sklearn (preprocessing, metrics, decomposition, ...)

## Data

Description of the datasets in the [Data](Data) folder:

- [body.mat](http://www.sci.usq.edu.au/courses/STA3301/resources/Data/) A subset of the dataset on body dimenstions. Described in 
G. Heinz, L. J. Peterson, R. W. Johnson, and C. J. Kerk, “Exploring relationships in body dimensions,” Journal of Statistics Education, vol. 11, no. 2, 2003.
- [faithful.mat and faithful.txt](https://www.jstor.org/stable/2347385?seq=1) Dataset on eruption of the Old Faithful geyser described in
A. Azzalini and A. Bowman, “A look at some data on the old faithful geyser,” Applied Statistics, pp. 357–365, 1990.
W. Härdle, Smoothing techniques: with implementation in S. Springer, 1991
- [female.txt and male.txt](http://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/)
- [iris.xls](http://archive.ics.uci.edu/ml/datasets/Iris) Fisher's Iris data (see [description](http://en.wikipedia.org/wiki/Iris_flower_data_set))
- [nanonose.xls](http://www.nanonose.dk) This data has been taken from the nanonose project, which is described in T. S. Alstrøm, J. Larsen, C. H. Nielsen, and N. B. Larsen, “Data-driven modeling of nano-nose gas sensor arrays,” in SPIE Defense, Security, and Sensing. International Society for Optics and Photonics, 2010, pp. 76 970U–76 970U.
- *StopWords* A txt file of list of common words provided in the TMG toolbox.
- *textDocs.txt* This example of documents for a term-document matrix is taken from L. Eldén, Matrix Methods in Data Mining and Pattern Recognition. Philadelphia, PA, USA: Society for Industrial and Applied Mathematics, 2007.
- [Wine.mat and Wine2.mat](http://archive.ics.uci.edu/ml/datasets/Wine+Quality) P. Cortez, A. Cerdeira, F. Almeida, T. Matos, and J. Reis. Modeling wine preferences by data mining from physicochemical properties. In Decision Support Systems, Elsevier, 47(4):547–553, 2009. Wine2 is same as Wine but with some outliers removed.
- [zipdata.mat and digits.mat](http://www.cad.zju.edu.cn/home/dengcai/Data/MLData.html). USPS handwritten digits, see also J. J. Hull, “A database for handwritten text recognition research,” Pattern Analysis and Machine Intelligence, IEEE Transactions on, vol. 16, no. 5, pp. 550–554,1994.
- [wildfaces.mat and wildfaces_grayscale.mat]( http://tamaraberg.com/faceDataset/) Described in Tamara L. Berg, Alexander C. Berg, Jaety Edwards, David A. Forsyth 
Neural Information Processing Systems (NIPS), 2004. The wildfaces.mat is an extract with 1000 examples of the original dataset and wildfaces_grayscale a gray scale converted version of these 1000 examples taken from the original data.
