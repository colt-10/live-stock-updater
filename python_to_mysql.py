import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:Alfa@123@localhost:3306/pivottrading')
data = pd.DataFrame(df)
data.to_sql('details', con = engine, if_exists = 'append', chunksize = 1000,index = False)

