import vk_api, os
from vk_api.bot_longpoll import VkBotLongPoll

class Connect:
    VK = vk_api.VkApi(token = os.environ['TOKEN'])
    LONGPOLL = VkBotLongPoll(VK, os.environ['GROUP_ID'])