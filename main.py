from VKAPI import Vk_api
from YaDisk import Ya_disk
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")
    vk_api = Vk_api(config["VK"]["token"])
    ya_disk = Ya_disk(config["YaDisk"]["token"])
    images = vk_api.get_images()
    for image in images:
        ya_disk.upload(f'/Загрузки/{image["id"]}', image["url"])
        print(image)

