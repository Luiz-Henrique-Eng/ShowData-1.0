import pandas as pd

class DataProcessor:
    @staticmethod
    def process_data(data):
        df = pd.DataFrame(data)
        # Exemplo de processamento: filtrar e limpar dados
        df = df.dropna()
        return df
