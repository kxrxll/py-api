from VKAPI import Vk_api
from YaDisk import Ya_disk
import configparser

if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read("settings.ini")
    owner = input("Enter ID please: ")
    vk_api = Vk_api(config["VK"]["token"], owner)
    ya_disk = Ya_disk(config["YaDisk"]["token"])
    images = vk_api.get_images()
    for image in images:
        stars = ""
        for i in range(image["likes"]):
            stars += "⭐"
        ya_disk.upload(f'/Загрузки_VK/{image["date"]} {stars}', image["url"])

