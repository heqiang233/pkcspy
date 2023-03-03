from telethon import events
from .. import jdbot
from ..diy.utils import read, write
import re
import requests,json

try:
    from .login import user
except:
    from .. import user
    
@user.on(events.NewMessage(pattern=r'^jx', outgoing=True))
async def jcmd(event):
    strText=""
    if event.is_reply is True:
        reply = await event.get_reply_message()
        strText=reply.text
    else:    
        msg_text= event.raw_text.split(' ')
        if isinstance(msg_text, list) and len(msg_text) == 2:
            strText = msg_text[-1]
    
    if strText==None:
        await user.send_message(event.chat_id,'请指定要解析的口令,格式: jx 口令 或对口令直接回复jx ')
        return 
        
    jumpUrl=""
    title=""    
    jiexiurl = "http://api.nolanstore.top/JComExchange"    
    data ={"code": strText}
    headers={"Content-Type": "application/json"}
    issuccess=False
    for num in range(10):  
        try:
            res=requests.post(url=jiexiurl,headers=headers,json=data,timeout=3)
            issuccess=True
        except:
            issuccess=False
        if issuccess:
            break
    data=json.loads(res.text)
    
    if  data["code"]=="0":  
        data = data["data"]
        title = data["title"]
        jump_url = data["jumpUrl"]
        activateId = re.findall("activityId=(.*?)&", data['jumpUrl'])
        code = re.findall("code=(.*?)&", data['jumpUrl'])
        if re.findall("https://cjhydz-isv.isvjcloud.com/wxTeam/activity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【CJ组队瓜分变量】\nexport jd_cjhy_activityId="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxTeam/activity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【LZ组队瓜分变量】\nexport jd_zdjr_activityId="{activateId[0]}"'
        elif re.findall("https://cjhydz-isv.isvjcloud.com/microDz/invite/activity/wx/view/index/8882761", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【微定制瓜分变量】\nexport jd_wdz_activityId="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxShareActivity/activity/6432842", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【LZ分享有礼变量】\nexport jd_fxyl_activityId="{activateId[0]}"'
        elif re.findall(".com/wxCollectionActivity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【M加购任务变量】\nexport M_WX_ADD_CART_URL="{jump_url}"'
        elif re.findall("https://lzkj-isv.isvjcloud.com/wxDrawActivity/activity/activity?activityId", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【幸运抽奖变量】\nexport LUCK_DRAW_URL="{jump_url}"\nexport M_WX_LUCK_DRAW_URL="{jump_url}"'
        elif re.findall("https://cjhy-isv.isvjcloud.com/wxDrawActivity/activity/activity?activityId", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【幸运抽奖变量】\nexport LUCK_DRAW_URL="{jump_url}"\nexport M_WX_LUCK_DRAW_URL="{jump_url}"'
        elif re.findall("cjwx/common/entry.html", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【幸运抽奖变量】\nexport LUCK_DRAW_URL="{jump_url}"\nexport M_WX_LUCK_DRAW_URL="{jump_url}"'
        elif re.findall("https://lzkj-isv.isvjcloud.com/wxgame/activity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【通用游戏变量】\nexport WXGAME_ACT_ID="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxShareActivity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【kr分享有礼变量】\nexport jd_fxyl_activityId="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxSecond", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【读秒变量】\nexport jd_wxSecond_activityId="{activateId[0]}"'
        elif re.findall("https://jinggengjcq-isv.isvjcloud.com", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【大牌联合开卡变量】\nexport DPLHTY="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxCartKoi/cartkoi", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【购物车锦鲤变量】\nexport jd_wxCartKoi_activityId="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxCollectCard", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n【集卡抽奖变量】\nexport jd_wxCollectCard_activityId="{activateId[0]}"'
        elif re.findall("https://lzkj-isv.isvjd.com/drawCenter", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n 【LZ刮刮乐抽奖变量】\nexport jd_drawCenter_activityId="{activateId[0]}"'
        elif re.findall("https://lzkjdz-isv.isvjcloud.com/wxFansInterActionActivity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n 【LZ粉丝互动变量】\nexport jd_wxFansInterActionActivity_activityId="{activateId[0]}"'
        elif re.findall("https://prodev.m.jd.com/mall/active/dVF7gQUVKyUcuSsVhuya5d2XD4F", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n 【邀好友赢大礼变量】\nexport yhyauthorCode="{code[0]}"'                   
        elif re.findall("https://lzkj-isv.isvjcloud.com/wxShopFollowActivity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n 【关注抽奖变量】\nexport jd_wxShopFollowActivity_activityId="{activateId[0]}"'                      
        elif re.findall("https://lzkj-isv.isvjcloud.com/wxShopFollowActivity", data['jumpUrl']):
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n 【关注抽奖变量】\nexport jd_wxShopFollowActivity_activityId="{activateId[0]}"'
        
        else:
                   msg = f'【活动名称】 {data["title"]}\n【活动链接】 [长按复制]({data["jumpUrl"]})\n 【温馨提示】未适配 ，手动吧靓仔!'
        await user.send_message(event.chat_id,msg)
    else:
        await user.send_message(event.chat_id,"解析出错:"+data.get("data"))
