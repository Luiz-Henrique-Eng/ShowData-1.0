from sqlalchemy import create_engine
from config.settings import DATABASE_URL

class DataStorage:
    def __init__(self):
        self.engine = create_engine(DATABASE_URL)

    def save_data(self, df, table_name):
        df.to_sql(table_name, self.engine, if_exists='replace', index=False)
