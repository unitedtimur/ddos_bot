from vk_api import VkApi
from vk_api.bot_longpoll import VkBotLongPoll
from ddos_bot.settings.access import vk

VK = VkApi(token=vk['token'])
LONGPOLL = VkBotLongPoll(VK, vk['group_id'])
