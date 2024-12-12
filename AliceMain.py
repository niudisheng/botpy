import botpy
from botpy.message import Message
from botpy.ext.command_util import Commands
import AItest
class MyClient(botpy.Client):
    async def on_group_at_message_create(self, message:Message):
        # name = message
        # print(name)

        content = AItest.get_response(message.content)
        # await self.api.post_message(channel_id=message.channel_id, content=f"{name},你好，这里是白洲梓机器人")
        await message.reply(content=f"{content}")
    async def on_at_message_create(self, message: Message):
        # 注册指令handler
        name = message.author.username
        # content = None
        content = AItest.get_response(message.content)
        # await self.api.post_message(channel_id=message.channel_id, content=f"{name},你好，这里是白洲梓机器人")
        await message.reply(content=f"@{name} ,{content}")

# intents = botpy.Intents(public_guild_messages=True,public_messages=True)
intents = botpy.Intents.default()
client = MyClient(intents=intents,is_sandbox=True)
client.run(appid="102470534", secret="oCb0PoDc2SsIi8YzQrIjAb2UwOqIkCf8")