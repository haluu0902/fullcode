# -*- coding: UTF-8 -*-
import os
from fbchat.models import *
from fbchat import log, Client
from tu_vi import TuVi
import codecs


class HaLuuBot(Client):
    clear = lambda: os.system('cls')
    data={'question':'','answer':'','author':''}
    cautl_main=''
    answer=''
    with open('setting.md', encoding='utf-8') as st:
        count_main = 0
        for line_main in st:          
            if count_main==0:
                action_getid=line_main.replace('\n','')
            if count_main==1:
                action_tuvi=line_main.replace('\n','')
            if count_main==2:
                action_daybot=line_main.replace('\n','')
            if count_main==3:
                action_cauhoi=line_main.replace('\n','')
            if count_main==4:
                action_cautl=line_main.replace('\n','')
            if count_main==5:
                action_tlmain=line_main.replace('\n','')
            if count_main==6:
                action_menu=line_main.replace('\n','')
            if count_main==7:
                action_setting=line_main.replace('\n','')
            count_main+=1
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        clear = lambda: os.system('cls')
        log.info('"%s" from "%s" in "%s"'%(message_object.text, thread_id, thread_type.name))
        type_chat = thread_type.name
        if type_chat!='GROUP':
            if author_id != self.uid:
                if message_object.text:
                    if message_object.text == HaLuuBot.action_getid:
                        print("ok")
                        self.send(Message(text='🤖 *Bot*: \n%s'%(message_object.author)), thread_id=thread_id, thread_type=thread_type)
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                        
                    elif HaLuuBot.action_tuvi in message_object.text:
                        tuoi = message_object.text[message_object.text.index(HaLuuBot.action_tuvi) + len(HaLuuBot.action_tuvi):]
                        tuvi = TuVi()
                        loi_phan = tuvi.con_giap(Cgiap=tuoi)
                        self.send(Message(text='🤖 *Bot*: \n%s'%(loi_phan)), thread_id=thread_id, thread_type=thread_type)
                        print('---------------Tử vi được tạo bởi Youtube: Nguyễn Mạnh----------------------------------------')
                        print('---------------https://www.youtube.com/channel/UCEY3DBfSDupbSG96jfcSDwQ/about--------------------------------')

                    elif HaLuuBot.action_daybot in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ %s + <Câu hỏi bạn muốn thêm> ví dụ: %s ăn cơm chưa'%(HaLuuBot.action_cauhoi,HaLuuBot.action_cauhoi)),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action_cauhoi in message_object.text:
                        HaLuuBot.data['question']=str(message_object.text[message_object.text.index(HaLuuBot.action_cauhoi) + len(HaLuuBot.action_cauhoi)+1:])
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ %s + <Câu trả lời cho câu hỏi của bạn> ví dụ: %s ăn cơm rồi'%(HaLuuBot.action_cautl,HaLuuBot.action_cautl)),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        HaLuuBot.cauhoi=message_object.text
                        HaLuuBot.clear()
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action_cautl in message_object.text:
                        HaLuuBot.data['author']=message_object.author
                        HaLuuBot.data['answer']=str(message_object.text[message_object.text.index(HaLuuBot.action_cautl) + len(HaLuuBot.action_cautl)+1:])
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

                            with open('data.md' , 'a+', encoding='utf-8') as dt:
                                dt.write(('%s\n%s\n')%(HaLuuBot.data['question'],HaLuuBot.data['answer']))
                            with open('author.md' , 'a+', encoding='utf-8') as at:
                                at.write(('Câu hỏi: %s-Câu trả lời: %s\nTác giả: %s')%(HaLuuBot.data['question'],HaLuuBot.data['answer'],HaLuuBot.data['author']))
                            HaLuuBot.data={'question':'','answer':'','author':''}
                    elif HaLuuBot.action_tlmain in message_object.text:
                        HaLuuBot.cautl_main=str(message_object.text[message_object.text.index(HaLuuBot.action_tlmain) + len(HaLuuBot.action_tlmain)+1:])
                        with open('answer_main.md' , 'w+', encoding='utf-8') as dt_tl:
                            dt_tl.write(HaLuuBot.cautl_main)
                        self.send(Message(
                            text='🤖 *Bot*: \n- Đã thay thế cau trả lời có sẵn'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action_menu  in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Muốn dạy bot trả lời gõ %s và làm theo hướng dẫn\n- Nếu muốn thay thế câu trả lời tự động không có kịch bản gõ %s + <Câu cần thay thế> ví dụ: %s Đang bận!\n- Nếu xem tử vi gõ %s + <tuổi>; ví dụ: %s sửu.\n -Muốn thay đổi câu lệnh phần setting gõ: %s'%(HaLuuBot.action_daybot,HaLuuBot.action_tlmain,HaLuuBot.action_tlmain,HaLuuBot.action_tuvi,HaLuuBot.action_tuvi,HaLuuBot.action_setting)),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )
                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')

                    elif HaLuuBot.action_setting in message_object.text:
                        self.send(Message(
                            text='🤖 *Bot*: \n- Gõ /getid_change, /tuvi_change, /daybot_change, /cauhoi_change, /cautl_change, /tl_main_change, /menu_change, /setting_change + <câu lệnh cần đổi>\n- Ví dụ: /setting_change !setting'),
                            thread_id=thread_id,
                            thread_type=thread_type
                        )

                    elif '/getid_change' in message_object.text:
                        HaLuuBot.action_getid=str(message_object.text[message_object.text.index('/getid_change') + len('/getid_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==0:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))
                    
                    elif '/tuvi_change' in message_object.text:
                        HaLuuBot.action_tuvi=str(message_object.text[message_object.text.index('/tuvi_change') + len('/tuvi_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==1:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))
                    
                    elif '/daybot_change' in message_object.text:
                        HaLuuBot.action_daybot=str(message_object.text[message_object.text.index('/daybot_change') + len('/daybot_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==2:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))
                    
                    elif '/cautl_change' in message_object.text:
                        HaLuuBot.action_cautl=str(message_object.text[message_object.text.index('/cautl_change') + len('/cautl_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==3:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))

                    elif '/tl_main_change' in message_object.text:
                        HaLuuBot.action_cautl=str(message_object.text[message_object.text.index('/tl_main_change') + len('/tl_main_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==4:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))
                    
                    elif '/cauhoi_change' in message_object.text:
                        HaLuuBot.action_tlmain=str(message_object.text[message_object.text.index('/cauhoi_change') + len('/cauhoi_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==5:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))
                    
                    elif '/menu_change' in message_object.text:
                        HaLuuBot.action_menu=str(message_object.text[message_object.text.index('/menu_change') + len('/menu_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==6:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))
                    
                    elif '/setting_change' in message_object.text:
                        HaLuuBot.action_setting=str(message_object.text[message_object.text.index('/setting_change') + len('/setting_change')+1:])
                        with open('setting.md','w+', encoding='utf-8') as st:
                            count_getid = 0
                            for line in st:
                                if count_getid==7:
                                    st.write("%s\n%s\%s\n%s\%s\n%s\%s"%(HaLuuBot.action_getid,HaLuuBot.action_tuvi,HaLuuBot.action_daybot,HaLuuBot.action_cauhoi,HaLuuBot.action_cautl,HaLuuBot.action_tlmain,HaLuuBot.action_menu,HaLuuBot.action_setitng))

                            
                    else:
                        result=False
                        with open('data.md', encoding='utf-8') as dt:
                            count = 0
                            cauhoi=False
                            cautl=''
                            for line in dt:
                                if count%2==0:
                                    count+=1
                                    if line.replace('\n','') in message_object.text:
                                        print('Câu hỏi có Data')
                                        cauhoi=True
                                else:
                                    count+=1
                                    if cauhoi==True:
                                        cautl=line
                                        self.send(Message(
                                            text='🤖 *Bot*: \n- %s'%(cautl)),
                                            thread_id=thread_id,
                                            thread_type=thread_type
                                        )
                                        HaLuuBot.clear()
                                        cauhoi=False
                                        cautl=''
                                        result=True                                            
                                        print('---------------https://www.facebook.com/haluu0902----------------------------------------')
                                        break

                        if result==False:
                            print('Câu hỏi không có Data')
                            with open('answer_main.md' , 'r', encoding=('utf-8')) as dt_tl:
                                HaLuuBot.cautl_main=dt_tl.read()
                            self.send(Message(
                                text='🤖 *Bot*:\n%s\n- Tin nhắn của bạn: %s'%(HaLuuBot.cautl_main,message_object.text)),
                                thread_id=thread_id,
                                thread_type=thread_type
                            )
                            print('---------------https://www.facebook.com/haluu0902----------------------------------------')