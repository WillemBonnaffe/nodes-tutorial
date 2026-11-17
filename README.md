# NODEs Tutorial

---
## Setup

Setup the repository in Google Colab:
* (1) Open Google Colab (`https://colab.research.google.com/`).
* (2) Sign into your Google account.
* (3) Select File > Open notebook > GitHub and enter the URL of the repository (`https://github.com/WillemBonnaffe/nodes-tutorial`).
* (4) Open the notebook `ì2_NODE_time_dependent.ipynb`.
* (5) To use GPU acceleration switch to a GPU runtime by selecting Runtime > Change runtime type > T4 GPU (you may have to click the `Connect` button in the top right corner).
* (6) Follow the instructions in the notebook.

---
## Challenge: Can we forecast ecosystem dynamics?

### Context:

It is not clear to what extent dynamics of natural systems are predictable.
Replicated experiments offer the chance to assess the consistency of our predictions across multiple time series.
The experiment by Hiltunen et al. (2013) provides time series of population counts of three replicated microcosms (tiny ecosystems).
Each microcosm contains a population of algae, flagellates (a bacteria that feeds on the algae), and rotifers (a tiny animal that feeds on both the algae and the flagellate).
They observed that the dynamics the populations in these replicates exhibited very similar oscillations.
This is a chance to assess if we can learn a deterministic process from these data that is generalisable.

### Goal of the practical: 

Train a forecasting model on replicate A and B, then forecast the dynamics of replicate C.
Most accurate predictions win.

### Data:

The data consists of time series of normalised counts of rotifer (noted R), algae (G), and flagellate (B).
There three replicates:`data_rotifer_A.csv`, `data_rotifer_B.csv`, and `data_rotifer_C_hidden.csv`.
Only the two first time steps of time series C are provided.

### Logistics:

The practical spans two work sessions:
* In the first session you may look at the code to fit and train a two-dimensional neural ODE or neural difference equation model (NDEs) to predict hare and lynx prey-predator oscillations. See notebooks `i2_NODE_time_dependent.ipynb` and `i2_NDE_time_dependent.ipynb`.
* In the second session you will have to adapt the code of the two-dimension models to fit the algae-flagellate-rotifer time series that have three species. 

Those are just indicative, you may organise your work as you please. 
Similarly, while this is a good opportunity to learn about Neural ODEs and NDEs, you may also use another forecasting framework if you feel confident.

### Submitting the forecast:

By 4pm on the second session, you should submit your forecast for the predicted density of rotifer algae and flagellates in replicate C.
The forecast should be submitted as a .csv file in the format specified below to allow for fast comparison and identification of the winner.
The winner will be determined by computation of the mean squared error (MSE) of the predictions vs the real values.

Submit your file at the following link: 
https://drive.google.com/drive/folders/1j5EtftD9GBql88rxwTcKPga8_k9k3RQZ?usp=sharing

### Submission format:

The prediction file should be a .csv named after your team name, e.g. `team-rotifire.csv`.
The predictions should have the same format as the `data_rotifer_C_hidden.csv` file.
That is, for each time step between 29 and 69, your model should produce 3 values, i.e. one for each species. 
For example:

t; R; G; B   
29; ...; ...; ...   
30; ...; ...; ...   
31; ...; ...; ...   
.   
.   
.   
69; ...; ...; ...   

