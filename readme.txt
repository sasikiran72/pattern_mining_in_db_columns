This project utilizes the ECLAT algorithm to perform association rule mining on the column names present in SQL queries, identifying frequent itemsets of column names. The pyECLAT library is employed for efficient ECLAT analysis.

How to get the code:
1. Clone the repository:

   ```bash
   git clone <repository_url>

Files Structure:
	The repo has two folders and a readme file
		1. src - inside which there is a pattern_mining.ipynb and a pattern_mining.py file with detailed comments added.
		2. datafiles - inside which we have three csv files that consist of test, train and validation data respectively.

Usage:
Running the Code in Google Colab:
	Open the Jupyter Notebook (pattern_mining.ipynb) in Google Colab:
		Open Google Colab (https://colab.research.google.com/).
		Click on "File" > "Open notebook" > "GitHub".
		Paste the URL of your GitHub repository (<repository_url>) and press Enter.
		Select the pattern_mining.ipynb notebook.
		OR
		Directly download the pattern_mining.ipynb notebook from the git link.
		Click on "File" > "Upload notebook".
		Upload the notebook from local.
		(The uploaded notebook does not have the data files. make sure you upload the data files for every runtime establishment.)
	
	Execute the Code Blocks:
		Run each code block in the notebook sequentially by clicking on the play button next to each cell or by pressing Shift + Enter.
	
	View Output:
		After executing the code blocks, you'll see the output below each cell, including frequent itemsets and support values.
