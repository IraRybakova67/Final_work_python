import logging

logging.basicConfig(level=logging.INFO, filemode='w', filename='error_float.log', encoding='UTF-8')
logger = logging.getLogger('float_text')


def to_float(num):
    try:
        return float(num)
    except (ValueError, TypeError):
        logger.error("Невозможно преобразовать")
        # print('Невозможно преобразовать')
        return


import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:

        logger.error('Не передан аргумент для преобразования.')

    else:
        arg = sys.argv[1]
        print(to_float(arg))
        logger.info(f'Преобразован агрумент {arg}')
