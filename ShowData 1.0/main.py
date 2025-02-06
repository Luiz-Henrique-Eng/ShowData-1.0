from api.api_client import APIClient
from data.data_processor import DataProcessor
from data.data_storage import DataStorage
from analysis.data_analysis import DataAnalysis
from visualization.data_visualization import DataVisualization

def main():
    # Exemplo de uso
    api_client = APIClient(base_url='https://api.example.com')
    data = api_client.get_data(endpoint='data')

    processor = DataProcessor()
    df = processor.process_data(data)

    storage = DataStorage()
    storage.save_data(df, table_name='example_data')

    analysis = DataAnalysis()
    summary = analysis.analyze_data(df)
    print(summary)

    visualization = DataVisualization()
    visualization.plot_data(df, x='date', y='value')

if __name__ == '__main__':
    main()
    