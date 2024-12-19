import pandas as pd


def create_dataframe(annotation_path: str) -> pd.DataFrame:
    """
    Создает DataFrame из файла аннотации.
    
    Args:
        annotation_path (str): путь к файлу аннотации
    
    Returns:
        pd.DataFrame: DataFrame с путями к изображениям
    """
    df = pd.read_csv(annotation_path)
    df.columns = ['Относительный путь', 'Абсолютный путь']
    return df 