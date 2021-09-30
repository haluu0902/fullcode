# -*- coding: UTF-8 -*-
import os
from fbchat.models import *
from fbchat import log, Client
from tu_vi import TuVi
import codecs
import json
import random


class HaLuuBot(Client):
    clear = lambda: os.system('cls')
    data={'question':'','answer':'','author':''}
    action = ""
    cautl_main=''
    answer=''
    with open(r'setting.json', 'r', encoding='utf-8') as ac:
        action = json.load(ac)
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        clear = lambda: os.system('cls')
        log.info('"%s" from "%s" in "%s"'%(message_object.text, thread_id, thread_type.name))
        type_chat = thread_type.name
        if type_chat!='GROUP':
            if author_id != self.uid:
                if message_object.text:
                    if message_object.text == HaLuuBot.action["getid"]:
                        print("ok")
                        self.send(Message(text='🤖 *Bot*: \n%s'%(message_object.author)), thread_id=thread_id, thread_type=thread_type)
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                        
                    elif HaLuuBot.action["tuvi"] in message_object.text:
                        tuoi = message_object.text[message_object.text.index(HaLuuBot.action["tuvi"]) + len(HaLuuBot.action["tuvi"]):]
                        tuvi = TuVi()
                        loi_phan = tuvi.con_giap(Cgiap=tuoi)
                        self.send(Message(text='🤖 *Bot*: \n%s'%(loi_phan)), thread_id=thread_id, thread_type=thread_type)
                        print('---------------Tử vi được tạo bởi Youtube: Nguyễn Mạnh----------------------------------------')
                        print('---------------https://www.youtube.com/channel/UCEY3DBfSDupbSG96jfcSDwQ/about--------------------------------')

                    elif HaLuuBot.action["daybot"] in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ %s + <Câu hỏi bạn muốn thêm> ví dụ: %s ăn cơm chưa'%(HaLuuBot.action["cauhoi"],HaLuuBot.action["cauhoi"])),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action["cauhoi"] in message_object.text:
                        HaLuuBot.data['question']=str(message_object.text[message_object.text.index(HaLuuBot.action["cauhoi"]) + len(HaLuuBot.action["cauhoi"])+1:])
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ %s + <Câu trả lời cho câu hỏi của bạn> ví dụ: %s ăn cơm rồi'%(HaLuuBot.action["cautl"],HaLuuBot.action["cautl"])),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        HaLuuBot.cauhoi=message_object.text
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action["cautl"] in message_object.text:
                        HaLuuBot.data['author']=message_object.author
                        HaLuuBot.data['answer']=str(message_object.text[message_object.text.index(HaLuuBot.action["cautl"]) + len(HaLuuBot.action["cautl"])+1:])
                        if HaLuuBot.data['question']=='' or HaLuuBot.data['answer']=='':
                            self.send(Message(
                            text='🤖 *Bot*: \n- Nhập thiếu dữ liệu câu hỏi hoặc câu trả lời vui lòng nhập lại!'),
                            thread_id=thread_id,
                            thread_type=thread_type
                            )
                            HaLuuBot.data={'question':'','answer':''}
                            print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                        else:
                            self.send(Message(
                                text='🤖 *Bot*: \n- Cảm ơn bạn đã dạy Bot nhé!'),
                                thread_id=thread_id,
                                thread_type=thread_type
                            )
                            HaLuuBot.cautl=message_object.text
                            HaLuuBot.clear()
                            print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                            with open(r'data.json' , 'r', encoding='utf-8') as dt:
                                dataQA = json.load(dt)
                                dataQA.append({
                                        "question" : HaLuuBot.data['question'],
                                        "answer" : HaLuuBot.data['answer'],
                                        "author" : HaLuuBot.data['author']
                                    })
                            with open(r'data.json' , 'w', encoding='utf-8') as dt:
                                json.dump(dataQA,dt, ensure_ascii=False)
                            HaLuuBot.data={'question':'','answer':'','author':''}
                    elif HaLuuBot.action["tlmain"] in message_object.text:
                        HaLuuBot.action["answer_main"]=str(message_object.text[message_object.text.index(HaLuuBot.action["tlmain"]) + len(HaLuuBot.action["tlmain"])+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                        self.send(Message(
                            text='🤖 *Bot*: \n- Đã thay thế cau trả lời có sẵn'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action["menu"]  in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Muốn dạy bot trả lời gõ %s và làm theo hướng dẫn\n- Nếu muốn thay thế câu trả lời tự động không có kịch bản gõ %s + <Câu cần thay thế> ví dụ: %s Đang bận!\n- Nếu xem tử vi gõ %s + <tuổi>; ví dụ: %s sửu.\n -Muốn thay đổi câu lệnh phần setting gõ: %s'%(HaLuuBot.action["daybot"],HaLuuBot.action["tlmain"],HaLuuBot.action["tlmain"],HaLuuBot.action["tuvi"],HaLuuBot.action["tuvi"],HaLuuBot.action["setting"])),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action["setting"] in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ /getid_change, /tuvi_change, /daybot_change, /cauhoi_change, /cautl_change, /tl_main_change, /menu_change, /setting_change + <câu lệnh cần đổi>\n- Ví dụ: /setting_change !setting'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )

                    elif '/getid_change' in message_object.text:
                        HaLuuBot.action["getid"]=str(message_object.text[message_object.text.index('/getid_change') + len('/getid_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                    
                    elif '/tuvi_change' in message_object.text:
                        HaLuuBot.action["tuvi"]=str(message_object.text[message_object.text.index('/tuvi_change') + len('/tuvi_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                    
                    elif '/daybot_change' in message_object.text:
                        HaLuuBot.action["daybot"]=str(message_object.text[message_object.text.index('/daybot_change') + len('/daybot_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                    
                    elif '/cautl_change' in message_object.text:
                        HaLuuBot.action["cautl"]=str(message_object.text[message_object.text.index('/cautl_change') + len('/cautl_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)

                    elif '/tl_main_change' in message_object.text:
                        HaLuuBot.action["cautl"]=str(message_object.text[message_object.text.index('/tl_main_change') + len('/tl_main_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)                            
                    
                    elif '/cauhoi_change' in message_object.text:
                        HaLuuBot.action["tlmain"]=str(message_object.text[message_object.text.index('/cauhoi_change') + len('/cauhoi_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                    
                    elif '/menu_change' in message_object.text:
                        HaLuuBot.action["menu"]=str(message_object.text[message_object.text.index('/menu_change') + len('/menu_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                    
                    elif '/setting_change' in message_object.text:
                        HaLuuBot.action["setting"]=str(message_object.text[message_object.text.index('/setting_change') + len('/setting_change')+1:])
                        with open(r'setting.json','w+', encoding='utf-8') as st:
                            json.dump(action , st)
                            
                    else:
                        result=False
                        with open(r'data.json', 'r', encoding='utf-8') as dt:
                            dataQA = json.load(dt)
                            cauhoi=False
                            cautl=""
                            for dataLine in dataQA:
                                if type(dataLine["question"]) == list:
                                    for question in dataLine["question"]:
                                        if question.lower() in message_object.text.lower():
                                            print('Câu hỏi có Data')
                                            cauhoi=True
                                else:
                                    if dataLine["question"].lower() in message_object.text.lower():
                                        print('Câu hỏi có Data')
                                        cauhoi=True
                                if cauhoi==True:
                                    if type(dataLine["answer"]) == list:
                                        size = len(dataLine["answer"])
                                        num = random.randint(0,size-1)
                                        cautl = dataLine["answer"][num]
                                        cauhoi=False
                                    else:
                                        cautl = dataLine["answer"]
                                        cauhoi=False
                                    self.send(Message(
                                        text='🤖 *Bot*: \n- %s'%(cautl)),
                                        thread_id=thread_id,
                                        thread_type=thread_type
                                    )
                                    HaLuuBot.clear()
                                    result=True                                            
                                    print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                                    
                        if result==False:
                            print('Câu hỏi không có Data')
                            HaLuuBot.cautl_main= HaLuuBot.action["answer_main"]
                            if type(HaLuuBot.cautl_main) == list:
                                HaLuuBot.cautl_main = HaLuuBot.cautl_main[random.randrange(len(HaLuuBot.cautl_main))]
                            self.send(Message(
                                text='🤖 *Bot*:\n%s\n- Tin nhắn của bạn: %s'%(HaLuuBot.cautl_main,message_object.text)),
                                thread_id=thread_id,
                                thread_type=thread_type
                            )
                            print('---------------https://www.facebook.com/haluu0902----------------------------------------')