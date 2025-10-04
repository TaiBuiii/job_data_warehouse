import logging
import os

def setup_logger(name: str):
    """
    Tạo logger đơn giản cho project
    :param name: tên module (vd: 'extract_jobcv')
    :return: logger object
    """
    log_dir = "logs"
    os.makedirs(log_dir, exist_ok=True)  # tạo folder logs nếu chưa có

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # tránh duplicate handler khi import logger nhiều lần
    if not logger.handlers:
        # Ghi ra file
        file_handler = logging.FileHandler(f"{log_dir}/{name}.log", encoding="utf-8")
        file_handler.setLevel(logging.INFO)

        # In ra console
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # Format log
        formatter = logging.Formatter(
            "%(asctime)s | %(name)s | %(levelname)s | %(message)s",
            "%Y-%m-%d %H:%M:%S"
        )
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handler
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger
