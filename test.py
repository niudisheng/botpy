import botpy
from botpy.message import Message
from botpy.ext.command_util import Commands
@Commands("自我介绍")
async def intro_handler(api, message: Message, params=None):
    params = "我是白洲梓，是刘运升的老婆"
    await message.reply(content=params)
    return True



class MyClient(botpy.Client):
    async def on_group_at_message_create(self, message):
        # message.author.username
        await message.reply(content="你好，这里是白洲梓机器人")
    async def on_at_message_create(self, message: Message):
        # 注册指令handler
        handlers = [
            intro_handler
        ]
        for handler in handlers:
            if await handler(api=self.api, message=message):
                return


        name = message.author.username
        # await self.api.post_message(channel_id=message.channel_id, content=f"{name},你好，这里是白洲梓机器人")
        await message.reply(content=f"@{name} ,你好，这里是白洲梓机器人")

# intents = botpy.Intents(public_guild_messages=True,public_messages=True)
intents = botpy.Intents.default()
client = MyClient(intents=intents,is_sandbox=True)
client.run(appid="102465101", secret="9gDlJrPxV3cBkJsR1bBlLvV6hItU5gIu")