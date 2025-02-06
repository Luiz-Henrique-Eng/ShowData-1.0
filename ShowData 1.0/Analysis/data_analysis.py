import pandas as pd

class DataAnalysis:
    @staticmethod
    def analyze_data(df):
        # Exemplo de análise: calcular média e desvio padrão
        summary = df.describe()
        return summary
