import itchat
import json

from requests import NullHandler

auto_reply_list = [
    'Blueflash客服',
    '布瑞斯',
    'Blueflash002',
    '张嘉龙',
    'Alex',
    'zisedexin61',
    '杨卓然6.16',
    '1900',
    '_yangzhuoran',
]

@itchat.msg_register(itchat.content.TEXT, isFriendChat=True)
def auto_reply(msg):

    importantReply = '系统识别中......\n此条信息来源于重要联系人，进行消息推送。\n------------\n我是机器人，主人正在赶due，您的消息已第一时间推送~'
    if msg.user.RemarkName in auto_reply_list:
        return importantReply

    
    reply = get_response(msg['Text'])
    
    return reply

def get_response(msg):
    defaultReply = '主人正在赶due，我是机器人，他回来会找你的 -- 人生苦短，我用python'
    autoReplyDic = '{"在干嘛":"想你", "睡了吗":"真没睡", "打游戏的":"怎么可能，打游戏还能秒回你？", "你真牛逼":"人生苦短，我用python", "机器人？":"你怎么知道，我这么不智能吗？", "起来没":"没呢，机器人回的，你信吗？", "回家了吗":"在路上的"}'
    replyMsg = json.loads(autoReplyDic)
    try:
        return replyMsg[msg]
    except:
        return defaultReply
   
@itchat.msg_register(itchat.content.PICTURE)
def auto_reply(msg):
    msg.download(msg.fileName)
    itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), 
        msg['FromUserName'])
    return '反弹'

itchat.auto_login()
itchat.run()