# Pandas

	import pandas as pd

## CREATING, LOADING, AND SELECTING DATA WITH PANDAS

#### Create a DataFrame

	pd.DataFrame({'column_name': [values]})
	
or by using lists

	df2 = pd.DataFrame([
		['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]],
    columns=['name', 'address', 'age'])
		
## Loading and Saving CSVs

	pd.read_csv('my-csv-file.csv')
	df.to_csv('new-csv-file.csv')
	
The method df.info() gives some statistics for each column.

#### Selecting columns

	df.column
	df['column']
	
#### Selecting Multiple Columns

	df[['column1', 'column2']]
	
#### selecting 2nd row

	df.iloc[2]
	
#### Select Rows with Logic

	df[df.MyColumnName == desired_column_value]
	df[(df.age < 30) | (df.name == 'Martha Jones')]

We could use the isin command to check that df.name is one of a list of values:

	df[df.name.isin(['Martha Jones', 'Rose Tyler', 'Amy Pond'])]
	
If we use the command df.reset_index(), we get a new DataFrame with a new set of indices:
- it’s probably better to use the keyword drop=True so that you don’t end up with that extra column
- If we use the keyword inplace=True we can just modify our existing DataFrame.

	df.reset_index(drop=True)
	
## MODIFYING DATAFRAMES
#### Adding a Column

	df['column_name'] = [values]
	or f.e.
	df['Sales Tax'] = df.Price * 0.075

