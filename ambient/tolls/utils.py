import logging


def notify(text):

    logging.basicConfig(
        handlers=[
            logging.FileHandler(
                filename="./logs/log_records.txt", encoding="utf-8", mode="a+"
            )
        ],
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%F %A %T",
        level=logging.INFO,
    )
    print(text)
    logging.info(text)
