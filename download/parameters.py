import enum


class Param(enum.Enum):
    folderData = 'data'    # название корневой  папкп
    folderStacks = 'Stacks'  # папка стаков
    fileSettings = 'settings.txt'  # название файла настроек

    beginPeriod = '80'        # по умолчанию период 80 баров