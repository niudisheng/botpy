#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os.path

import botpy
from botpy.core.util.yaml_util import YamlUtil
from botpy.model.announce import (
    RecommendChannel,
    CreateAnnounceRequest,
    RecommendChannelRequest,
    CreateChannelAnnounceRequest,
)
from botpy.model.ws_context import WsContext

test_config = YamlUtil.read(os.path.join(os.path.dirname(__file__), "config.yaml"))


async def _announce_handler(context: WsContext, message: botpy.Message):
    msg_api = botpy.AsyncMessageAPI(t_token, False)
    announce_api = botpy.AsyncAnnouncesAPI(t_token, False)

    botpy._log.info("event_type %s" % context.event_type + ",receive message %s" % message.content)

    # 先发送消息告知用户
    message_to_send = botpy.MessageSendRequest("command received: %s" % message.content)
    await msg_api.post_message(message.channel_id, message_to_send)

    # 输入/xxx后的处理
    message_id = "088de19cbeb883e7e97110a2e39c0138d401"
    if "/建公告" in message.content:
        create_announce_request = CreateAnnounceRequest(message.channel_id, message_id)
        await announce_api.create_announce(message.guild_id, create_announce_request)

    elif "/删公告" in message.content:
        await announce_api.delete_announce(message.guild_id, message_id)

    elif "/建子频道公告" in message.content:
        create_channel_announce_request = CreateChannelAnnounceRequest(message_id)
        await announce_api.create_channel_announce(message.channel_id, create_channel_announce_request)

    elif "/删子频道公告" in message.content:
        await announce_api.delete_channel_announce(message.channel_id, message_id)

    elif "/设置推荐子频道" in message.content:
        channel_list = [RecommendChannel(message.channel_id, "introduce")]
        request = RecommendChannelRequest(0, channel_list)
        await announce_api.post_recommended_channels(message.guild_id, request)


if __name__ == "__main__":
    t_token = botpy.Token(test_config["token"]["appid"], test_config["token"]["token"])
    # 注册机器人被@后的事件
    qqbot_handler = botpy.Handler(botpy.HandlerType.AT_MESSAGE_EVENT_HANDLER, _announce_handler)
    botpy.async_listen_events(t_token, False, qqbot_handler)