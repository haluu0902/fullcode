# -*- coding: UTF-8 -*-
import csv
import os
from fbchat.models import *
from fbchat import log, Client
from tu_vi import TuVi
import codecs
import pandas as pd


class HaLuuBot(Client):
    clear = lambda: os.system('cls')
    data={'question':'','answer':'','author':''}
    file_dt=pd.read_csv('./data.csv')
    cautl_main=''
    answer=''
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        clear = lambda: os.system('cls')
        log.info('%s from %s in %s'%(message_object.text, thread_id, thread_type.name))
        type_chat = thread_type.name
        if type_chat!='GROUP':
            if author_id != self.uid:
                if message_object.text:
                    a=message_object.text
                    if message_object.text == '/Getid' or message_object.text == '/getid':
                        self.send(Message(text='🤖 *Bot*: \n%s'%(message_object.author)), thread_id=thread_id, thread_type=thread_type)
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                        
                    elif '/tuvi' in message_object.text:
                        tuoi = message_object.text[message_object.text.index('/tuvi') + len('/tuvi'):]
                        tuvi = TuVi()
                        loi_phan = tuvi.con_giap(Cgiap=tuoi)
                        self.send(Message(text='🤖 *Bot*: \n%s'%(loi_phan)), thread_id=thread_id, thread_type=thread_type)
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif '/daybot' in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ /cauhoi + <Câu hỏi bạn muốn thêm> ví dụ: /cauhoi ăn cơm chưa'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif '/cauhoi' in message_object.text:
                        HaLuuBot.data['question']=str(message_object.text[message_object.text.index('/cauhoi') + len('/cauhoi')+1:])
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ /cautl + <Câu trả lời cho câu hỏi của bạn> ví dụ: ăn cơm rồi'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        HaLuuBot.cauhoi=message_object.text
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif '/cautl' in message_object.text:
                        HaLuuBot.data['author']=message_object.author
                        HaLuuBot.data['answer']=str(message_object.text[message_object.text.index('/cautl') + len('/cautl')+1:])
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

                            with open('data.csv' , 'a+', encoding='utf-8') as dt:
                                writer = csv.writer(dt, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
                                writer.writerow([HaLuuBot.data['question'],HaLuuBot.data['answer'],HaLuuBot.data['author']])
                                HaLuuBot.data={'question':'','answer':''}
                    elif '/tl_main' in message_object.text:
                        HaLuuBot.cautl_main=str(message_object.text[message_object.text.index('/tl_main') + len('/tl_main')+1:])
                        with open('answer_main.md' , 'w+', encoding='utf-8') as dt_tl:
                            dt_tl.write(HaLuuBot.cautl_main)
                        self.send(Message(
                            text='🤖 *Bot*: \n- Đã thay thế cau trả lời có sẵn'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif '/menu'  in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Muốn dạy bot trả lời gõ /daybot và làm theo hướng dẫn\n- Nếu muốn thay thế câu trả lời tự động không có kịch bản gõ /tl_main + <Câu cần thay thế> ví dụ: /tl_main Đang bận!\n- Nếu xem tử vi gõ /tuvi + <tuổi>; ví dụ: /tuvi sửu.'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                            
                    else:
                        b=False
                        with open('data.csv', encoding='utf-8') as dt:
                            dt = csv.reader(dt, delimiter=',')
                            for row in dt:
                                try:
                                    if row[0] == str(message_object.text):
                                        self.send(Message(
                                            text='🤖 *Bot*: \n- %s'%(row[1])),
                                            thread_id=thread_id,
                                            thread_type=thread_type
                                        )
                                        HaLuuBot.clear()
                                        b=True
                                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                                except:
                                    pass

                        if b==False:
                            with open('answer_main.md' , 'r', encoding=('utf-8')) as dt_tl:
                                HaLuuBot.cautl_main=dt_tl.read()
                            self.send(Message(
                                text='🤖 *Bot*:\n%s\n - Gõ /menu để hiện ra các câu lệnh có sẵn!\n- Tin nhắn của bạn: %s'%(HaLuuBot.cautl_main,message_object.text)),
                                thread_id=thread_id,
                                thread_type=thread_type
                            )
                            print('---------------https://www.facebook.com/haluu0902----------------------------------------')