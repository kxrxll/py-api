from VKAPI import Vk_api
from YaDisk import Ya_disk


if __name__ == '__main__':
    vk_api = Vk_api("a67f00c673c3d4b12800dd0ba29579ec56d804f3c5f3bbcef5328d4b3981fa5987b951cf2c8d8b24b9abd")
    ya_disk = Ya_disk("AQAAAAA4K3AyAADLW79VZaDx1kQyjL2smqCwFQE")
    images = vk_api.get_images()
    for image in images:
        ya_disk.upload(f'/Загрузки/{image["id"]}', image["url"])
        print(image)

