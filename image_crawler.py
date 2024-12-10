from icrawler.builtin import BingImageCrawler


def download_images(keyword: str, save_dir: str, num_images: int) -> None:
    """
    Загрузка изображений с помощью Bing Image Crawler.
    
    Args:
        keyword (str): поисковый запрос
        save_dir (str): директория для сохранения изображений
        num_images (int): количество изображений для загрузки
    """
    crawler = BingImageCrawler(
        storage={'root_dir': save_dir},
        feeder_threads=4,
        parser_threads=4,
        downloader_threads=4
    )
    
    crawler.crawl(
        keyword=keyword,
        max_num=num_images,
        filters={'type':'photo'},
        file_idx_offset=0,
        min_size=(200,200),
        max_size=None
    )
