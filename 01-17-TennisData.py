import pandas as pd
file="C:\\Users\\amac\\Documents\\GoogleDrive\\Washu\\01-17-Dai\\final_data_Katy.dta"
ktfinal = pd.read_stata(file, convert_dates=True, convert_categoricals=True, encoding=None, index=None, convert_missing=False, preserve_dtypes=True, columns=None, order_categoricals=True, chunksize=None, iterator=False)
slice = ktfinal[:5]
#print(slice)

