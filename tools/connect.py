from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll


VK = VkApi(token="d59d9c293e141282e9888280161eccec554ae2d5d2756e0a2cf046fb9998dc1f25bf654429c292734d03e")
LONGPOLL = VkBotLongPoll(VK, "197296135")
