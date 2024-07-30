"""
File: my_drawing.py
Name: Jill
----------------------

"""

from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.graphics.gwindow import GWindow

window = GWindow(width=700, height=500, title='Squirtle')


def main():
    """
    Title: My friend Squirtle

    This is my friend Squirtle.
    When I am learning Python diligently, he is always sleeping.

    """
    head1 = GRect(40, 10, x=250, y=50)
    head1.filled = True
    head1.fill_color = (89, 156, 165)
    head1.color = (89, 156, 165)
    window.add(head1)
    head2 = GRect(20, 10, x=290, y=50)
    head2.filled = True
    head2.fill_color = (38, 117, 131)
    head2.color = (38, 117, 131)
    window.add(head2)
    head3 = GRect(20, 10, x=230, y=60)
    head3.filled = True
    head3.fill_color = (89, 156, 165)
    head3.color = (89, 156, 165)
    window.add(head3)
    head4 = GRect(40, 10, x=250, y=60)
    head4.filled = True
    head4.fill_color = (182, 230, 240)
    head4.color = (182, 230, 240)
    window.add(head4)
    head5 = GRect(20, 10, x=290, y=60)
    head5.filled = True
    head5.fill_color = (139, 198, 205)
    head5.color = (139, 198, 205)
    window.add(head5)
    head6 = GRect(20, 10, x=310, y=60)
    head6.filled = True
    head6.fill_color = (38, 117, 131)
    head6.color = (38, 117, 131)
    window.add(head6)
    head7 = GRect(10, 10, x=220, y=70)
    head7.filled = True
    head7.fill_color = (89, 156, 165)
    head7.color = (89, 156, 165)
    window.add(head7)
    head8 = GRect(40, 10, x=230, y=70)
    head8.filled = True
    head8.fill_color = (182, 230, 240)
    head8.color = (182, 230, 240)
    window.add(head8)
    head9 = GRect(60, 10, x=270, y=70)
    head9.filled = True
    head9.fill_color = (139, 198, 205)
    head9.color = (139, 198, 205)
    window.add(head9)
    head10 = GRect(10, 10, x=330, y=70)
    head10.filled = True
    head10.fill_color = (38, 117, 131)
    head10.color = (38, 117, 131)
    window.add(head10)
    head11 = GRect(10, 10, x=210, y=80)
    head11.filled = True
    head11.fill_color = (42, 113, 131)
    head11.color = (42, 113, 131)
    window.add(head11)
    head12 = GRect(40, 10, x=220, y=80)
    head12.filled = True
    head12.fill_color = (182, 230, 240)
    head12.color = (182, 230, 240)
    window.add(head12)
    head13 = GRect(80, 10, x=260, y=80)
    head13.filled = True
    head13.fill_color = (139, 198, 205)
    head13.color = (139, 198, 205)
    window.add(head13)
    head14 = GRect(10, 10, x=340, y=80)
    head14.filled = True
    head14.fill_color = (38, 117, 131)
    head14.color = (38, 117, 131)
    window.add(head14)
    head15 = GRect(10, 20, x=200, y=90)
    head15.filled = True
    head15.fill_color = (38, 117, 131)
    head15.color = (38, 117, 131)
    window.add(head15)
    head16 = GRect(10, 40, x=210, y=90)
    head16.filled = True
    head16.fill_color = (139, 198, 205)
    head16.color = (139, 198, 205)
    window.add(head16)
    head17 = GRect(30, 10, x=220, y=90)
    head17.filled = True
    head17.fill_color = (182, 230, 240)
    head17.color = (182, 230, 240)
    window.add(head17)
    head18 = GRect(100, 10, x=250, y=90)
    head18.filled = True
    head18.fill_color = (139, 198, 205)
    head18.color = (139, 198, 205)
    window.add(head18)
    head19 = GRect(10, 20, x=350, y=90)
    head19.filled = True
    head19.fill_color = (38, 117, 131)
    head19.color = (38, 117, 131)
    window.add(head19)
    head20 = GRect(130, 10, x=220, y=100)
    head20.filled = True
    head20.fill_color = (139, 198, 205)
    head20.color = (139, 198, 205)
    window.add(head20)
    head21 = GRect(10, 10, x=280, y=100)
    head21.filled = True
    head21.fill_color = (89, 156, 165)
    head21.color = (89, 156, 165)
    window.add(head21)
    head22 = GRect(10, 50, x=190, y=110)
    head22.filled = True
    head22.fill_color = (38, 117, 131)
    head22.color = (38, 117, 131)
    window.add(head22)
    head23 = GRect(10, 10, x=200, y=110)
    head23.filled = True
    head23.fill_color = (89, 156, 165)
    head23.color = (89, 156, 165)
    window.add(head23)
    head24 = GRect(130, 10, x=220, y=110)
    head24.filled = True
    head24.fill_color = (139, 198, 205)
    head24.color = (139, 198, 205)
    window.add(head24)
    head25 = GRect(10, 10, x=270, y=110)
    head25.filled = True
    head25.fill_color = (89, 156, 165)
    head25.color = (89, 156, 165)
    window.add(head25)
    head26 = GRect(30, 10, x=290, y=110)
    head26.filled = True
    head26.fill_color = (89, 156, 165)
    head26.color = (89, 156, 165)
    window.add(head26)
    head27 = GRect(10, 10, x=350, y=110)
    head27.filled = True
    head27.fill_color = (89, 156, 165)
    head27.color = (89, 156, 165)
    window.add(head27)
    head28 = GRect(10, 10, x=360, y=110)
    head28.filled = True
    head28.fill_color = (42, 115, 133)
    head28.color = (42, 115, 133)
    window.add(head28)
    l_eye1 = GRect(10, 30, x=200, y=120)
    l_eye1.filled = True
    l_eye1.fill_color = (133, 41, 2)
    l_eye1.color = (133, 41, 2)
    window.add(l_eye1)
    l_eye2 = GRect(10, 10, x=200, y=130)
    l_eye2.filled = True
    l_eye2.fill_color = (255, 255, 255)
    l_eye2.color = (255, 255, 255)
    window.add(l_eye2)
    l_eye3 = GRect(10, 10, x=200, y=150)
    l_eye3.filled = True
    l_eye3.fill_color = 'black'
    l_eye3.color = 'black'
    window.add(l_eye3)
    head29 = GRect(70, 70, x=210, y=120)
    head29.filled = True
    head29.fill_color = (139, 198, 205)
    head29.color = (139, 198, 205)
    window.add(head29)
    head30 = GRect(10, 20, x=210, y=130)
    head30.filled = True
    head30.fill_color = (89, 156, 165)
    head30.color = (89, 156, 165)
    window.add(head30)
    r_eye2 = GRect(30, 50, x=280, y=120)
    r_eye2.filled = True
    r_eye2.fill_color = 'black'
    r_eye2.color = 'black'
    window.add(r_eye2)
    r_eye1 = GRect(10, 10, x=280, y=120)
    r_eye1.filled = True
    r_eye1.fill_color = (89, 156, 165)
    r_eye1.color = (89, 156, 165)
    window.add(r_eye1)
    r_eye3 = GRect(20, 10, x=300, y=120)
    r_eye3.filled = True
    r_eye3.fill_color = (214, 206, 206)
    r_eye3.color = (214, 206, 206)
    window.add(r_eye3)
    r_eye4 = GRect(10, 10, x=310, y=130)
    r_eye4.filled = True
    r_eye4.fill_color = (214, 206, 206)
    r_eye4.color = (214, 206, 206)
    window.add(r_eye4)
    head31 = GRect(40, 60, x=320, y=120)
    head31.filled = True
    head31.fill_color = (89, 156, 165)
    head31.color = (89, 156, 165)
    window.add(head31)
    head32 = GRect(10, 10, x=330, y=120)
    head32.filled = True
    head32.fill_color = (139, 198, 205)
    head32.color = (139, 198, 205)
    window.add(head32)
    head33 = GRect(10, 30, x=320, y=130)
    head33.filled = True
    head33.fill_color = (40, 116, 132)
    head33.color = (40, 116, 132)
    window.add(head33)
    head34 = GRect(10, 60, x=360, y=120)
    head34.filled = True
    head34.fill_color = 'black'
    head34.color = 'black'
    window.add(head34)
    r_eye5 = GRect(10, 30, x=310, y=140)
    r_eye5.filled = True
    r_eye5.fill_color = (133, 41, 2)
    r_eye5.color = (133, 41, 2)
    window.add(r_eye5)
    r_eye6 = GRect(10, 10, x=280, y=150)
    r_eye6.filled = True
    r_eye6.fill_color = 'white'
    r_eye6.color = 'white'
    window.add(r_eye6)
    r_eye7 = GRect(10, 10, x=280, y=160)
    r_eye7.filled = True
    r_eye7.fill_color = (133, 41, 2)
    r_eye7.color = (133, 41, 2)
    window.add(r_eye7)
    head35 = GRect(10, 10, x=180, y=160)
    head35.filled = True
    head35.fill_color = (89, 156, 165)
    head35.color = (89, 156, 165)
    window.add(head35)
    head36 = GRect(20, 10, x=190, y=160)
    head36.filled = True
    head36.fill_color = (182, 230, 240)
    head36.color = (182, 230, 240)
    window.add(head36)
    head37 = GRect(10, 10, x=180, y=170)
    head37.filled = True
    head37.fill_color = 'black'
    head37.color = 'black'
    window.add(head37)
    head38 = GRect(10, 10, x=190, y=170)
    head38.filled = True
    head38.fill_color = (182, 230, 240)
    head38.color = (182, 230, 240)
    window.add(head38)
    head39 = GRect(10, 10, x=200, y=170)
    head39.filled = True
    head39.fill_color = (139, 198, 205)
    head39.color = (139, 198, 205)
    window.add(head39)
    nose1 = GRect(10, 10, x=210, y=170)
    nose1.filled = True
    nose1.fill_color = (89, 156, 165)
    nose1.color = (89, 156, 165)
    window.add(nose1)
    nose2 = GRect(10, 10, x=230, y=170)
    nose2.filled = True
    nose2.fill_color = (89, 156, 165)
    nose2.color = (89, 156, 165)
    window.add(nose2)
    head40 = GRect(20, 10, x=280, y=170)
    head40.filled = True
    head40.fill_color = (139, 198, 205)
    head40.color = (139, 198, 205)
    window.add(head40)
    head41 = GRect(20, 10, x=300, y=170)
    head41.filled = True
    head41.fill_color = (89, 156, 165)
    head41.color = (89, 156, 165)
    window.add(head41)
    head42 = GRect(10, 10, x=190, y=180)
    head42.filled = True
    head42.fill_color = 'black'
    head42.color = "black"
    window.add(head42)
    head43 = GRect(10, 10, x=200, y=180)
    head43.filled = True
    head43.fill_color = (89, 156, 165)
    head43.color = (89, 156, 165)
    window.add(head43)
    head44 = GRect(10, 10, x=280, y=180)
    head44.filled = True
    head44.fill_color = (139, 198, 205)
    head44.color = (139, 198, 205)
    window.add(head44)
    head45 = GRect(60, 10, x=290, y=180)
    head45.filled = True
    head45.fill_color = (89, 156, 165)
    head45.color = (89, 156, 165)
    window.add(head45)
    head46 = GRect(10, 10, x=310, y=180)
    head46.filled = True
    head46.fill_color = (38, 117, 131)
    head46.color = (38, 117, 131)
    window.add(head46)
    head47 = GRect(10, 10, x=350, y=180)
    head47.filled = True
    head47.fill_color = 'black'
    head47.color = 'black'
    window.add(head47)
    head48 = GRect(20, 10, x=200, y=190)
    head48.filled = True
    head48.fill_color = 'black'
    head48.color = 'black'
    window.add(head48)
    head49 = GRect(20, 10, x=220, y=190)
    head49.filled = True
    head49.fill_color = (139, 198, 205)
    head49.color = (139, 198, 205)
    window.add(head49)
    head50 = GRect(10, 10, x=240, y=190)
    head50.filled = True
    head50.fill_color = (89, 156, 165)
    head50.color = (89, 156, 165)
    window.add(head50)
    head51 = GRect(50, 10, x=250, y=190)
    head51.filled = True
    head51.fill_color = (41, 115, 131)
    head51.color = (41, 115, 131)
    window.add(head51)
    head52 = GRect(20, 10, x=300, y=190)
    head52.filled = True
    head52.fill_color = (133, 41, 4)
    head52.color = (133, 41, 4)
    window.add(head52)
    head53 = GRect(30, 10, x=320, y=190)
    head53.filled = True
    head53.fill_color = (89, 156, 165)
    head53.color = (89, 156, 165)
    window.add(head53)
    head54 = GRect(10, 10, x=350, y=190)
    head54.filled = True
    head54.fill_color = (41, 115, 131)
    head54.color = (41, 115, 131)
    window.add(head54)
    head55 = GRect(50, 10, x=190, y=200)
    head55.filled = True
    head55.fill_color = 'black'
    head55.color = 'black'
    window.add(head55)
    head56 = GRect(10, 10, x=210, y=200)
    head56.filled = True
    head56.fill_color = (89, 156, 165)
    head56.color = (89, 156, 165)
    window.add(head56)
    mouth1 = GRect(70, 10, x=240, y=200)
    mouth1.filled = True
    mouth1.fill_color = (133, 41, 4)
    mouth1.color = (133, 41, 4)
    window.add(mouth1)
    mouth2 = GRect(40, 10, x=250, y=200)
    mouth2.filled = True
    mouth2.fill_color = (206, 123, 41)
    mouth2.color = (206, 123, 41)
    window.add(mouth2)
    head57 = GRect(50, 10, x=310, y=200)
    head57.filled = True
    head57.fill_color = (89, 156, 165)
    head57.color = (89, 156, 165)
    window.add(head57)
    head58 = GRect(10, 10, x=340, y=200)
    head58.filled = True
    head58.fill_color = 'black'
    head58.color = 'black'
    window.add(head58)
    head59 = GRect(10, 10, x=210, y=210)
    head59.filled = True
    head59.fill_color = 'black'
    head59.color = 'black'
    window.add(head59)
    head60 = GRect(100, 10, x=220, y=210)
    head60.filled = True
    head60.fill_color = (89, 156, 165)
    head60.color = (89, 156, 165)
    window.add(head60)
    mouth3 = GRect(50, 10, x=240, y=210)
    mouth3.filled = True
    mouth3.fill_color = (133, 41, 4)
    mouth3.color = (133, 41, 4)
    window.add(mouth3)
    head61 = GRect(30, 10, x=320, y=210)
    head61.filled = True
    head61.fill_color = (40, 115, 131)
    head61.color = (40, 115, 131)
    window.add(head61)
    head62 = GRect(10, 10, x=330, y=210)
    head62.filled = True
    head62.fill_color = 'black'
    head62.color = 'black'
    window.add(head62)
    head63 = GRect(100, 10, x=220, y=220)
    head63.filled = True
    head63.fill_color = 'black'
    head63.color = 'black'
    window.add(head63)
    head64 = GRect(10, 10, x=230, y=220)
    head64.filled = True
    head64.fill_color = (38, 117, 131)
    head64.color = (38, 117, 131)
    window.add(head64)
    head65 = GRect(60, 10, x=240, y=220)
    head65.filled = True
    head65.fill_color = (89, 156, 165)
    head65.color = (89, 156, 165)
    window.add(head65)
    head66 = GRect(10, 10, x=320, y=220)
    head66.filled = True
    head66.fill_color = (206, 124, 41)
    head66.color = (206, 124, 41)
    window.add(head66)
    head67 = GRect(10, 10, x=330, y=220)
    head67.filled = True
    head67.fill_color = (215, 206, 206)
    head67.color = (215, 206, 206)
    window.add(head67)
    head68 = GRect(20, 10, x=220, y=230)
    head68.filled = True
    head68.fill_color = (89, 156, 165)
    head68.color = (89, 156, 165)
    window.add(head68)
    head69 = GRect(10, 10, x=240, y=230)
    head69.filled = True
    head69.fill_color = (38, 117, 131)
    head69.color = (38, 117, 131)
    window.add(head69)
    head70 = GRect(50, 10, x=250, y=230)
    head70.filled = True
    head70.fill_color = 'black'
    head70.color = 'black'
    window.add(head70)
    l_hand1 = GRect(10, 10, x=150, y=190)
    l_hand1.filled = True
    l_hand1.fill_color = (89, 156, 165)
    l_hand1.color = (89, 156, 165)
    window.add(l_hand1)
    l_hand5 = GRect(10, 10, x=170, y=190)
    l_hand5.filled = True
    l_hand5.fill_color = (89, 156, 165)
    l_hand5.color = (89, 156, 165)
    window.add(l_hand5)
    l_hand2 = GRect(40, 10, x=150, y=200)
    l_hand2.filled = True
    l_hand2.fill_color = (38, 117, 131)
    l_hand2.color = (38, 117, 131)
    window.add(l_hand2)
    l_hand3 = GRect(10, 10, x=160, y=200)
    l_hand3.filled = True
    l_hand3.fill_color = (139, 198, 205)
    l_hand3.color = (139, 198, 205)
    window.add(l_hand3)
    l_hand4 = GRect(10, 10, x=170, y=200)
    l_hand4.filled = True
    l_hand4.fill_color = (89, 156, 165)
    l_hand4.color = (89, 156, 165)
    window.add(l_hand4)
    l_hand6 = GRect(70, 10, x=140, y=210)
    l_hand6.filled = True
    l_hand6.fill_color = (89, 156, 165)
    l_hand6.color = (89, 156, 165)
    window.add(l_hand6)
    l_hand7 = GRect(40, 20, x=150, y=210)
    l_hand7.filled = True
    l_hand7.fill_color = (139, 198, 205)
    l_hand7.color = (139, 198, 205)
    window.add(l_hand7)
    l_hand8 = GRect(10, 10, x=140, y=220)
    l_hand8.filled = True
    l_hand8.fill_color = (38, 117, 131)
    l_hand8.color = (38, 117, 131)
    window.add(l_hand8)
    l_hand9 = GRect(30, 20, x=190, y=220)
    l_hand9.filled = True
    l_hand9.fill_color = (139, 198, 205)
    l_hand9.color = (139, 198, 205)
    window.add(l_hand9)
    l_hand10 = GRect(10, 10, x=150, y=230)
    l_hand10.filled = True
    l_hand10.fill_color = (38, 117, 131)
    l_hand10.color = (38, 117, 131)
    window.add(l_hand10)
    l_hand11 = GRect(10, 10, x=160, y=230)
    l_hand11.filled = True
    l_hand11.fill_color = (89, 156, 165)
    l_hand11.color = (89, 156, 165)
    window.add(l_hand11)
    l_hand12 = GRect(20, 10, x=170, y=230)
    l_hand12.filled = True
    l_hand12.fill_color = (139, 198, 205)
    l_hand12.color = (139, 198, 205)
    window.add(l_hand12)
    l_hand13 = GRect(10, 10, x=160, y=240)
    l_hand13.filled = True
    l_hand13.fill_color = (38, 117, 131)
    l_hand13.color = (38, 117, 131)
    window.add(l_hand13)
    l_hand14 = GRect(60, 10, x=170, y=240)
    l_hand14.filled = True
    l_hand14.fill_color = (89, 156, 165)
    l_hand14.color = (89, 156, 165)
    window.add(l_hand14)
    l_hand15 = GRect(20, 10, x=170, y=250)
    l_hand15.filled = True
    l_hand15.fill_color = (38, 117, 131)
    l_hand15.color = (38, 117, 131)
    window.add(l_hand15)
    l_hand16 = GRect(30, 20, x=190, y=250)
    l_hand16.filled = True
    l_hand16.fill_color = (89, 156, 165)
    l_hand16.color = (89, 156, 165)
    window.add(l_hand16)
    l_hand17 = GRect(20, 10, x=190, y=260)
    l_hand17.filled = True
    l_hand17.fill_color = 'black'
    l_hand17.color = 'black'
    window.add(l_hand17)
    r_hand1 = GRect(10, 10, x=380, y=180)
    r_hand1.filled = True
    r_hand1.fill_color = (89, 156, 165)
    r_hand1.color = (89, 156, 165)
    window.add(r_hand1)
    r_hand2 = GRect(30, 10, x=390, y=180)
    r_hand2.filled = True
    r_hand2.fill_color = (38, 117, 131)
    r_hand2.color = (38, 117, 131)
    window.add(r_hand2)
    r_hand3 = GRect(50, 10, x=370, y=190)
    r_hand3.filled = True
    r_hand3.fill_color = (89, 156, 165)
    r_hand3.color = (89, 156, 165)
    window.add(r_hand3)
    r_hand4 = GRect(20, 10, x=380, y=190)
    r_hand4.filled = True
    r_hand4.fill_color = (139, 198, 205)
    r_hand4.color = (139, 198, 205)
    window.add(r_hand4)
    r_hand5 = GRect(10, 10, x=420, y=190)
    r_hand5.filled = True
    r_hand5.fill_color = 'black'
    r_hand5.color = 'black'
    window.add(r_hand5)
    r_hand7 = GRect(20, 20, x=380, y=200)
    r_hand7.filled = True
    r_hand7.fill_color = (38, 117, 131)
    r_hand7.color = (38, 117, 131)
    window.add(r_hand7)
    r_hand6 = GRect(30, 10, x=360, y=200)
    r_hand6.filled = True
    r_hand6.fill_color = (139, 198, 205)
    r_hand6.color = (139, 198, 205)
    window.add(r_hand6)
    r_hand8 = GRect(10, 20, x=400, y=200)
    r_hand8.filled = True
    r_hand8.fill_color = (89, 156, 165)
    r_hand8.color = (89, 156, 165)
    window.add(r_hand8)
    r_hand9 = GRect(10, 20, x=410, y=200)
    r_hand9.filled = True
    r_hand9.fill_color = 'black'
    r_hand9.color = 'black'
    window.add(r_hand9)
    r_hand10 = GRect(30, 20, x=350, y=210)
    r_hand10.filled = True
    r_hand10.fill_color = (139, 198, 205)
    r_hand10.color = (139, 198, 205)
    window.add(r_hand10)
    r_hand11 = GRect(10, 10, x=340, y=220)
    r_hand11.filled = True
    r_hand11.fill_color = (89, 156, 165)
    r_hand11.color = (89, 156, 165)
    window.add(r_hand11)
    r_hand12 = GRect(10, 40, x=330, y=230)
    r_hand12.filled = True
    r_hand12.fill_color = (38, 117, 131)
    r_hand12.color = (38, 117, 131)
    window.add(r_hand12)
    r_hand13 = GRect(10, 20, x=320, y=240)
    r_hand13.filled = True
    r_hand13.fill_color = (38, 117, 131)
    r_hand13.color = (38, 117, 131)
    window.add(r_hand13)
    r_hand14 = GRect(50, 20, x=330, y=240)
    r_hand14.filled = True
    r_hand14.fill_color = (89, 156, 165)
    r_hand14.color = (89, 156, 165)
    window.add(r_hand14)
    r_hand15 = GRect(10, 10, x=380, y=240)
    r_hand15.filled = True
    r_hand15.fill_color = (89, 156, 165)
    r_hand15.color = (89, 156, 165)
    window.add(r_hand15)
    r_hand16 = GRect(30, 10, x=340, y=230)
    r_hand16.filled = True
    r_hand16.fill_color = (139, 198, 205)
    r_hand16.color = (139, 198, 205)
    window.add(r_hand16)
    r_hand17 = GRect(10, 10, x=370, y=230)
    r_hand17.filled = True
    r_hand17.fill_color = (89, 156, 165)
    r_hand17.color = (89, 156, 165)
    window.add(r_hand17)
    r_hand18 = GRect(20, 20, x=380, y=220)
    r_hand18.filled = True
    r_hand18.fill_color = (89, 156, 165)
    r_hand18.color = (89, 156, 165)
    window.add(r_hand18)
    r_hand19 = GRect(10, 20, x=400, y=220)
    r_hand19.filled = True
    r_hand19.fill_color = 'black'
    r_hand19.color = 'black'
    window.add(r_hand19)
    r_hand20 = GRect(20, 10, x=340, y=240)
    r_hand20.filled = True
    r_hand20.fill_color = (139, 198, 205)
    r_hand20.color = (139, 198, 205)
    window.add(r_hand20)
    r_hand21 = GRect(10, 10, x=390, y=240)
    r_hand21.filled = True
    r_hand21.fill_color = 'black'
    r_hand21.color = 'black'
    window.add(r_hand21)
    r_hand22 = GRect(10, 10, x=380, y=250)
    r_hand22.filled = True
    r_hand22.fill_color = 'black'
    r_hand22.color = 'black'
    window.add(r_hand22)
    r_hand23 = GRect(10, 10, x=370, y=260)
    r_hand23.filled = True
    r_hand23.fill_color = 'black'
    r_hand23.color = 'black'
    window.add(r_hand23)
    r_hand24 = GRect(30, 10, x=340, y=260)
    r_hand24.filled = True
    r_hand24.fill_color = (89, 156, 165)
    r_hand24.color = (89, 156, 165)
    window.add(r_hand24)
    r_hand25 = GRect(30, 10, x=340, y=270)
    r_hand25.filled = True
    r_hand25.fill_color = 'black'
    r_hand25.color = 'black'
    window.add(r_hand25)
    body1 = GRect(10, 70, x=210, y=270)
    body1.filled = True
    body1.fill_color = (206, 124, 42)
    body1.color = (206, 124, 42)
    window.add(body1)
    body2 = GRect(10, 20, x=220, y=250)
    body2.filled = True
    body2.fill_color = (206, 124, 42)
    body2.color = (206, 124, 42)
    window.add(body2)
    body3 = GRect(10, 20, x=230, y=240)
    body3.filled = True
    body3.fill_color = (206, 124, 42)
    body3.color = (206, 124, 42)
    window.add(body3)
    body4 = GRect(40, 10, x=240, y=260)
    body4.filled = True
    body4.fill_color = (206, 124, 42)
    body4.color = (206, 124, 42)
    window.add(body4)
    body5 = GRect(40, 10, x=280, y=250)
    body5.filled = True
    body5.fill_color = (206, 124, 42)
    body5.color = (206, 124, 42)
    window.add(body5)
    body6 = GRect(30, 10, x=300, y=230)
    body6.filled = True
    body6.fill_color = (230, 174, 91)
    body6.color = (230, 174, 91)
    window.add(body6)
    body7 = GRect(30, 10, x=290, y=240)
    body7.filled = True
    body7.fill_color = (230, 174, 91)
    body7.color = (230, 174, 91)
    window.add(body7)
    body8 = GRect(10, 10, x=240, y=240)
    body8.filled = True
    body8.fill_color = (230, 174, 91)
    body8.color = (230, 174, 91)
    window.add(body8)
    body9 = GRect(40, 10, x=250, y=240)
    body9.filled = True
    body9.fill_color = (254, 214, 108)
    body9.color = (254, 214, 108)
    window.add(body9)
    body10 = GRect(40, 10, x=240, y=250)
    body10.filled = True
    body10.fill_color = (254, 214, 108)
    body10.color = (254, 214, 108)
    window.add(body10)
    body11 = GRect(10, 10, x=230, y=260)
    body11.filled = True
    body11.fill_color = (254, 230, 157)
    body11.color = (254, 230, 157)
    window.add(body11)
    body12 = GRect(20, 30, x=220, y=270)
    body12.filled = True
    body12.fill_color = (254, 230, 157)
    body12.color = (254, 230, 157)
    window.add(body12)
    body13 = GRect(10, 30, x=240, y=280)
    body13.filled = True
    body13.fill_color = (254, 230, 157)
    body13.color = (254, 230, 157)
    window.add(body13)
    body14 = GRect(10, 10, x=240, y=270)
    body14.filled = True
    body14.fill_color = (255, 214, 107)
    body14.color = (255, 214, 107)
    window.add(body14)
    body15 = GRect(10, 10, x=230, y=300)
    body15.filled = True
    body15.fill_color = (255, 214, 107)
    body15.color = (255, 214, 107)
    window.add(body15)
    body16 = GRect(10, 10, x=220, y=300)
    body16.filled = True
    body16.fill_color = (206, 124, 42)
    body16.color = (206, 124, 42)
    window.add(body16)
    body17 = GRect(10, 30, x=250, y=270)
    body17.filled = True
    body17.fill_color = (231, 173, 90)
    body17.color = (231, 173, 90)
    window.add(body17)
    body18 = GRect(10, 30, x=250, y=300)
    body18.filled = True
    body18.fill_color = (206, 124, 42)
    body18.color = (206, 124, 42)
    window.add(body18)
    body19 = GRect(60, 10, x=240, y=310)
    body19.filled = True
    body19.fill_color = (206, 124, 42)
    body19.color = (206, 124, 42)
    window.add(body19)
    body20 = GRect(40, 40, x=260, y=270)
    body20.filled = True
    body20.fill_color = (254, 230, 157)
    body20.color = (254, 230, 157)
    window.add(body20)
    body21 = GRect(10, 10, x=280, y=260)
    body21.filled = True
    body21.fill_color = (231, 173, 90)
    body21.color = (231, 173, 90)
    window.add(body21)
    body22 = GRect(30, 10, x=290, y=260)
    body22.filled = True
    body22.fill_color = (254, 214, 108)
    body22.color = (254, 214, 108)
    window.add(body22)
    body23 = GRect(20, 10, x=300, y=270)
    body23.filled = True
    body23.fill_color = (254, 214, 108)
    body23.color = (254, 214, 108)
    window.add(body23)
    body24 = GRect(10, 20, x=300, y=280)
    body24.filled = True
    body24.fill_color = (254, 214, 108)
    body24.color = (254, 214, 108)
    window.add(body24)
    body25 = GRect(10, 20, x=320, y=260)
    body25.filled = True
    body25.fill_color = (206, 124, 42)
    body25.color = (206, 124, 42)
    window.add(body25)
    body26 = GRect(10, 10, x=330, y=270)
    body26.filled = True
    body26.fill_color = (231, 173, 90)
    body26.color = (231, 173, 90)
    window.add(body26)
    body27 = GRect(40, 10, x=310, y=280)
    body27.filled = True
    body27.fill_color = (231, 173, 90)
    body27.color = (231, 173, 90)
    window.add(body27)
    body28 = GRect(10, 40, x=310, y=290)
    body28.filled = True
    body28.fill_color = (206, 124, 42)
    body28.color = (206, 124, 42)
    window.add(body28)
    body29 = GRect(10, 20, x=320, y=290)
    body29.filled = True
    body29.fill_color = (254, 214, 108)
    body29.color = (254, 214, 108)
    window.add(body29)
    body30 = GRect(20, 20, x=330, y=290)
    body30.filled = True
    body30.fill_color = (231, 173, 90)
    body30.color = (231, 173, 90)
    window.add(body30)
    body30 = GRect(10, 20, x=340, y=310)
    body30.filled = True
    body30.fill_color = (231, 173, 90)
    body30.color = (231, 173, 90)
    window.add(body30)
    body31 = GRect(20, 20, x=320, y=310)
    body31.filled = True
    body31.fill_color = (254, 214, 108)
    body31.color = (254, 214, 108)
    window.add(body31)
    body32 = GRect(10, 20, x=320, y=290)
    body32.filled = True
    body32.fill_color = (254, 214, 108)
    body32.color = (254, 214, 108)
    window.add(body32)
    body33 = GRect(10, 20, x=310, y=300)
    body33.filled = True
    body33.fill_color = (254, 214, 108)
    body33.color = (254, 214, 108)
    window.add(body33)
    body34 = GRect(10, 20, x=300, y=300)
    body34.filled = True
    body34.fill_color = (206, 124, 42)
    body34.color = (206, 124, 42)
    window.add(body34)
    body35 = GRect(10, 10, x=290, y=300)
    body35.filled = True
    body35.fill_color = (254, 214, 108)
    body35.color = (254, 214, 108)
    window.add(body35)
    body36 = GRect(20, 10, x=270, y=310)
    body36.filled = True
    body36.fill_color = (231, 173, 90)
    body36.color = (231, 173, 90)
    window.add(body36)
    body37 = GRect(10, 10, x=230, y=310)
    body37.filled = True
    body37.fill_color = (231, 173, 90)
    body37.color = (231, 173, 90)
    window.add(body37)
    body38 = GRect(10, 10, x=220, y=310)
    body38.filled = True
    body38.fill_color = (254, 230, 157)
    body38.color = (254, 230, 157)
    window.add(body38)
    body39 = GRect(30, 20, x=220, y=320)
    body39.filled = True
    body39.fill_color = (254, 230, 157)
    body39.color = (254, 230, 157)
    window.add(body39)
    body40 = GRect(10, 10, x=220, y=330)
    body40.filled = True
    body40.fill_color = (254, 214, 108)
    body40.color = (254, 214, 108)
    window.add(body40)
    body40 = GRect(10, 20, x=220, y=340)
    body40.filled = True
    body40.fill_color = (206, 124, 41)
    body40.color = (206, 124, 41)
    window.add(body40)
    body43 = GRect(40, 30, x=260, y=320)
    body43.filled = True
    body43.fill_color = (254, 230, 156)
    body43.color = (254, 230, 156)
    window.add(body43)
    body41 = GRect(40, 10, x=230, y=340)
    body41.filled = True
    body41.fill_color = (254, 214, 108)
    body41.color = (254, 214, 108)
    window.add(body41)
    body42 = GRect(10, 20, x=250, y=330)
    body42.filled = True
    body42.fill_color = (231, 173, 90)
    body42.color = (231, 173, 90)
    window.add(body42)
    body44 = GRect(10, 10, x=290, y=320)
    body44.filled = True
    body44.fill_color = (254, 214, 108)
    body44.color = (254, 214, 108)
    window.add(body44)
    body45 = GRect(10, 10, x=300, y=320)
    body45.filled = True
    body45.fill_color = (230, 174, 91)
    body45.color = (230, 174, 91)
    window.add(body45)
    body46 = GRect(10, 20, x=300, y=330)
    body46.filled = True
    body46.fill_color = (254, 214, 108)
    body46.color = (254, 214, 108)
    window.add(body46)
    body47 = GRect(20, 20, x=310, y=330)
    body47.filled = True
    body47.fill_color = (230, 174, 91)
    body47.color = (230, 174, 91)
    window.add(body47)
    body48 = GRect(10, 10, x=320, y=330)
    body48.filled = True
    body48.fill_color = (206, 124, 41)
    body48.color = (206, 124, 41)
    window.add(body48)
    body49 = GRect(10, 10, x=330, y=330)
    body49.filled = True
    body49.fill_color = (230, 174, 91)
    body49.color = (230, 174, 91)
    window.add(body49)
    body50 = GRect(90, 20, x=230, y=350)
    body50.filled = True
    body50.fill_color = (230, 174, 91)
    body50.color = (230, 174, 91)
    window.add(body50)
    body50 = GRect(20, 10, x=250, y=350)
    body50.filled = True
    body50.fill_color = (206, 124, 41)
    body50.color = (206, 124, 41)
    window.add(body50)
    body51 = GRect(20, 10, x=230, y=360)
    body51.filled = True
    body51.fill_color = (206, 124, 41)
    body51.color = (206, 124, 41)
    window.add(body51)
    body52 = GRect(20, 10, x=270, y=360)
    body52.filled = True
    body52.fill_color = (206, 124, 41)
    body52.color = (206, 124, 41)
    window.add(body52)
    body53 = GRect(10, 10, x=240, y=370)
    body53.filled = True
    body53.fill_color = (134, 42, 3)
    body53.color = (134, 42, 3)
    window.add(body53)
    body54 = GRect(20, 10, x=250, y=380)
    body54.filled = True
    body54.fill_color = (134, 42, 3)
    body54.color = (134, 42, 3)
    window.add(body54)
    body58 = GRect(70, 10, x=260, y=390)
    body58.filled = True
    body58.fill_color = 'black'
    body58.color = 'black'
    window.add(body58)
    body55 = GRect(20, 10, x=270, y=390)
    body55.filled = True
    body55.fill_color = (134, 42, 3)
    body55.color = (134, 42, 3)
    window.add(body55)
    body56 = GRect(40, 10, x=250, y=370)
    body56.filled = True
    body56.fill_color = (230, 174, 91)
    body56.color = (230, 174, 91)
    window.add(body56)
    body57 = GRect(40, 10, x=270, y=380)
    body57.filled = True
    body57.fill_color = (230, 174, 91)
    body57.color = (230, 174, 91)
    window.add(body57)
    body59 = GRect(30, 10, x=290, y=370)
    body59.filled = True
    body59.fill_color = (206, 124, 41)
    body59.color = (206, 124, 41)
    window.add(body59)
    body60 = GRect(30, 10, x=290, y=370)
    body60.filled = True
    body60.fill_color = (206, 124, 41)
    body60.color = (206, 124, 41)
    window.add(body60)
    body61 = GRect(10, 10, x=310, y=380)
    body61.filled = True
    body61.fill_color = (206, 124, 41)
    body61.color = (206, 124, 41)
    window.add(body61)
    back1 = GRect(10, 20, x=350, y=280)
    back1.filled = True
    back1.fill_color = (98, 41, 3)
    back1.color = (98, 41, 3)
    window.add(back1)
    back2 = GRect(10, 30, x=350, y=300)
    back2.filled = True
    back2.fill_color = (189, 107, 16)
    back2.color = (189, 107, 16)
    window.add(back2)
    back3 = GRect(10, 10, x=360, y=310)
    back3.filled = True
    back3.fill_color = (189, 107, 16)
    back3.color = (189, 107, 16)
    window.add(back3)
    back4 = GRect(10, 10, x=360, y=320)
    back4.filled = True
    back4.fill_color = (98, 41, 3)
    back4.color = (98, 41, 3)
    window.add(back4)
    back5 = GRect(10, 30, x=360, y=280)
    back5.filled = True
    back5.fill_color = (215, 207, 207)
    back5.color = (215, 207, 207)
    window.add(back5)
    back6 = GRect(10, 60, x=370, y=270)
    back6.filled = True
    back6.fill_color = (215, 207, 207)
    back6.color = (215, 207, 207)
    window.add(back6)
    back7 = GRect(10, 20, x=380, y=320)
    back7.filled = True
    back7.fill_color = (215, 207, 207)
    back7.color = (215, 207, 207)
    window.add(back7)
    back8 = GRect(10, 10, x=380, y=310)
    back8.filled = True
    back8.fill_color = (213, 148, 82)
    back8.color = (213, 148, 82)
    window.add(back8)
    back9 = GRect(20, 50, x=380, y=260)
    back9.filled = True
    back9.fill_color = (189, 107, 16)
    back9.color = (189, 107, 16)
    window.add(back9)
    back10 = GRect(10, 10, x=390, y=300)
    back10.filled = True
    back10.fill_color = 'black'
    back10.color = 'black'
    window.add(back10)
    back11 = GRect(10, 30, x=390, y=310)
    back11.filled = True
    back11.fill_color = (189, 107, 16)
    back11.color = (189, 107, 16)
    window.add(back11)
    back12 = GRect(10, 10, x=390, y=340)
    back12.filled = True
    back12.fill_color = (215, 206, 207)
    back12.color = (215, 206, 207)
    window.add(back12)
    back13 = GRect(10, 10, x=390, y=250)
    back13.filled = True
    back13.fill_color = (98, 41, 3)
    back13.color = (98, 41, 3)
    window.add(back13)
    back14 = GRect(10, 60, x=400, y=260)
    back14.filled = True
    back14.fill_color = (98, 41, 3)
    back14.color = (98, 41, 3)
    window.add(back14)
    back15 = GRect(10, 10, x=400, y=290)
    back15.filled = True
    back15.fill_color = 'black'
    back15.color = 'black'
    window.add(back15)
    back16 = GRect(10, 30, x=400, y=320)
    back16.filled = True
    back16.fill_color = 'black'
    back16.color = 'black'
    window.add(back16)
    tail1 = GRect(60, 20, x=400, y=350)
    tail1.filled = True
    tail1.fill_color = (89, 156, 165)
    tail1.color = (89, 156, 165)
    window.add(tail1)
    tail2 = GRect(40, 10, x=400, y=370)
    tail2.filled = True
    tail2.fill_color = 'black'
    tail2.color = 'black'
    window.add(tail2)
    tail2 = GRect(30, 10, x=440, y=360)
    tail2.filled = True
    tail2.fill_color = 'black'
    tail2.color = 'black'
    window.add(tail2)
    tail3 = GRect(30, 10, x=460, y=350)
    tail3.filled = True
    tail3.fill_color = 'black'
    tail3.color = 'black'
    window.add(tail3)
    tail4 = GRect(80, 10, x=410, y=340)
    tail4.filled = True
    tail4.fill_color = (89, 156, 165)
    tail4.color = (89, 156, 165)
    window.add(tail4)
    tail5 = GRect(10, 10, x=450, y=340)
    tail5.filled = True
    tail5.fill_color = 'black'
    tail5.color = 'black'
    window.add(tail5)
    tail6 = GRect(10, 10, x=490, y=340)
    tail6.filled = True
    tail6.fill_color = 'black'
    tail6.color = 'black'
    window.add(tail6)
    tail7 = GRect(30, 50, x=410, y=290)
    tail7.filled = True
    tail7.fill_color = (89, 156, 165)
    tail7.color = (89, 156, 165)
    window.add(tail7)
    tail8 = GRect(100, 10, x=410, y=280)
    tail8.filled = True
    tail8.fill_color = (40, 115, 133)
    tail8.color = (40, 115, 133)
    window.add(tail8)
    tail9 = GRect(10, 10, x=420, y=280)
    tail9.filled = True
    tail9.fill_color = (89, 156, 165)
    tail9.color = (89, 156, 165)
    window.add(tail9)
    tail10 = GRect(70, 10, x=430, y=280)
    tail10.filled = True
    tail10.fill_color = (142, 197, 197)
    tail10.color = (142, 197, 197)
    window.add(tail10)
    tail11 = GRect(90, 10, x=420, y=270)
    tail11.filled = True
    tail11.fill_color = (40, 115, 133)
    tail11.color = (40, 115, 133)
    window.add(tail11)
    tail12 = GRect(70, 10, x=430, y=270)
    tail12.filled = True
    tail12.fill_color = (89, 156, 165)
    tail12.color = (89, 156, 165)
    window.add(tail12)
    tail13 = GRect(50, 10, x=440, y=270)
    tail13.filled = True
    tail13.fill_color = (142, 197, 197)
    tail13.color = (142, 197, 197)
    window.add(tail13)
    tail14 = GRect(70, 10, x=430, y=260)
    tail14.filled = True
    tail14.fill_color = (40, 115, 133)
    tail14.color = (40, 115, 133)
    window.add(tail14)
    tail15 = GRect(30, 10, x=450, y=260)
    tail15.filled = True
    tail15.fill_color = (142, 197, 197)
    tail15.color = (142, 197, 197)
    window.add(tail15)
    tail16 = GRect(10, 10, x=480, y=260)
    tail16.filled = True
    tail16.fill_color = (89, 156, 165)
    tail16.color = (89, 156, 165)
    window.add(tail16)
    tail17 = GRect(40, 10, x=450, y=250)
    tail17.filled = True
    tail17.fill_color = (40, 115, 133)
    tail17.color = (40, 115, 133)
    window.add(tail17)
    tail18 = GRect(60, 10, x=440, y=290)
    tail18.filled = True
    tail18.fill_color = (142, 197, 197)
    tail18.color = (142, 197, 197)
    window.add(tail18)
    tail19 = GRect(20, 10, x=460, y=290)
    tail19.filled = True
    tail19.fill_color = (40, 115, 133)
    tail19.color = (40, 115, 133)
    window.add(tail19)
    tail20 = GRect(10, 30, x=500, y=290)
    tail20.filled = True
    tail20.fill_color = (89, 156, 165)
    tail20.color = (89, 156, 165)
    window.add(tail20)
    tail21 = GRect(10, 30, x=510, y=290)
    tail21.filled = True
    tail21.fill_color = 'black'
    tail21.color = 'black'
    window.add(tail21)
    tail22 = GRect(60, 20, x=440, y=300)
    tail22.filled = True
    tail22.fill_color = (89, 156, 165)
    tail22.color = (89, 156, 165)
    window.add(tail22)
    tail23 = GRect(40, 10, x=450, y=300)
    tail23.filled = True
    tail23.fill_color = (40, 115, 130)
    tail23.color = (40, 115, 130)
    window.add(tail23)
    tail24 = GRect(10, 10, x=440, y=310)
    tail24.filled = True
    tail24.fill_color = (40, 115, 130)
    tail24.color = (40, 115, 130)
    window.add(tail24)
    tail25 = GRect(20, 10, x=460, y=300)
    tail25.filled = True
    tail25.fill_color = (142, 197, 197)
    tail25.color = (142, 197, 197)
    window.add(tail25)
    tail26 = GRect(10, 10, x=490, y=300)
    tail26.filled = True
    tail26.fill_color = (142, 197, 197)
    tail26.color = (142, 197, 197)
    window.add(tail26)
    tail27 = GRect(30, 10, x=460, y=310)
    tail27.filled = True
    tail27.fill_color = (142, 197, 197)
    tail27.color = (142, 197, 197)
    window.add(tail27)
    tail28 = GRect(70, 20, x=440, y=320)
    tail28.filled = True
    tail28.fill_color = 'black'
    tail28.color = 'black'
    window.add(tail28)
    tail29 = GRect(50, 20, x=450, y=320)
    tail29.filled = True
    tail29.fill_color = (89, 156, 165)
    tail29.color = (89, 156, 165)
    window.add(tail29)
    r_leg1 = GRect(20, 10, x=340, y=330)
    r_leg1.filled = True
    r_leg1.fill_color = (89, 156, 165)
    r_leg1.color = (89, 156, 165)
    window.add(r_leg1)
    r_leg2 = GRect(20, 10, x=360, y=330)
    r_leg2.filled = True
    r_leg2.fill_color = (38, 117, 131)
    r_leg2.color = (38, 117, 131)
    window.add(r_leg2)
    r_leg3 = GRect(50, 10, x=330, y=340)
    r_leg3.filled = True
    r_leg3.fill_color = (89, 156, 165)
    r_leg3.color = (89, 156, 165)
    window.add(r_leg3)
    r_leg4 = GRect(30, 10, x=340, y=340)
    r_leg4.filled = True
    r_leg4.fill_color = (139, 198, 205)
    r_leg4.color = (139, 198, 205)
    window.add(r_leg4)
    r_leg5 = GRect(10, 10, x=380, y=340)
    r_leg5.filled = True
    r_leg5.fill_color = (38, 117, 131)
    r_leg5.color = (38, 117, 131)
    window.add(r_leg5)
    r_leg6 = GRect(70, 30, x=320, y=350)
    r_leg6.filled = True
    r_leg6.fill_color = (89, 156, 165)
    r_leg6.color = (89, 156, 165)
    window.add(r_leg6)
    r_leg7 = GRect(50, 30, x=330, y=350)
    r_leg7.filled = True
    r_leg7.fill_color = (139, 198, 205)
    r_leg7.color = (139, 198, 205)
    window.add(r_leg7)
    r_leg8 = GRect(10, 20, x=320, y=360)
    r_leg8.filled = True
    r_leg8.fill_color = (38, 117, 131)
    r_leg8.color = (38, 117, 131)
    window.add(r_leg8)
    r_leg9 = GRect(10, 30, x=390, y=350)
    r_leg9.filled = True
    r_leg9.fill_color = (38, 117, 131)
    r_leg9.color = (38, 117, 131)
    window.add(r_leg9)
    r_leg10 = GRect(10, 10, x=390, y=360)
    r_leg10.filled = True
    r_leg10.fill_color = 'black'
    r_leg10.color = 'black'
    window.add(r_leg10)
    r_leg11 = GRect(10, 10, x=320, y=380)
    r_leg11.filled = True
    r_leg11.fill_color = 'black'
    r_leg11.color = 'black'
    window.add(r_leg11)
    r_leg12 = GRect(70, 10, x=330, y=380)
    r_leg12.filled = True
    r_leg12.fill_color = (89, 156, 165)
    r_leg12.color = (89, 156, 165)
    window.add(r_leg12)
    r_leg13 = GRect(30, 10, x=340, y=380)
    r_leg13.filled = True
    r_leg13.fill_color = (139, 198, 205)
    r_leg13.color = (139, 198, 205)
    window.add(r_leg13)
    r_leg14 = GRect(10, 10, x=330, y=390)
    r_leg14.filled = True
    r_leg14.fill_color = (38, 117, 131)
    r_leg14.color = (38, 117, 131)
    window.add(r_leg14)
    r_leg15 = GRect(70, 40, x=340, y=390)
    r_leg15.filled = True
    r_leg15.fill_color = (89, 156, 165)
    r_leg15.color = (89, 156, 165)
    window.add(r_leg15)
    r_leg16 = GRect(10, 10, x=330, y=400)
    r_leg16.filled = True
    r_leg16.fill_color = 'black'
    r_leg16.color = 'black'
    window.add(r_leg16)
    r_leg17 = GRect(10, 20, x=340, y=410)
    r_leg17.filled = True
    r_leg17.fill_color = 'black'
    r_leg17.color = 'black'
    window.add(r_leg17)
    r_leg18 = GRect(20, 10, x=350, y=430)
    r_leg18.filled = True
    r_leg18.fill_color = 'black'
    r_leg18.color = 'black'
    window.add(r_leg18)
    r_leg19 = GRect(10, 10, x=370, y=420)
    r_leg19.filled = True
    r_leg19.fill_color = 'black'
    r_leg19.color = 'black'
    window.add(r_leg19)
    r_leg20 = GRect(20, 10, x=380, y=430)
    r_leg20.filled = True
    r_leg20.fill_color = 'black'
    r_leg20.color = 'black'
    window.add(r_leg20)
    r_leg21 = GRect(20, 10, x=400, y=420)
    r_leg21.filled = True
    r_leg21.fill_color = 'black'
    r_leg21.color = 'black'
    window.add(r_leg21)
    r_leg22 = GRect(10, 10, x=410, y=410)
    r_leg22.filled = True
    r_leg22.fill_color = 'black'
    r_leg22.color = 'black'
    window.add(r_leg22)
    r_leg23 = GRect(10, 40, x=400, y=370)
    r_leg23.filled = True
    r_leg23.fill_color = 'black'
    r_leg23.color = 'black'
    window.add(r_leg23)
    r_leg24 = GRect(10, 10, x=350, y=420)
    r_leg24.filled = True
    r_leg24.fill_color = (139, 198, 205)
    r_leg24.color = (139, 198, 205)
    window.add(r_leg24)
    r_leg25 = GRect(10, 10, x=380, y=420)
    r_leg25.filled = True
    r_leg25.fill_color = (139, 198, 205)
    r_leg25.color = (139, 198, 205)
    window.add(r_leg25)
    r_leg26 = GRect(10, 10, x=390, y=420)
    r_leg26.filled = True
    r_leg26.fill_color = (38, 117, 131)
    r_leg26.color = (38, 117, 131)
    window.add(r_leg26)
    l_leg1 = GRect(10, 10, x=200, y=330)
    l_leg1.filled = True
    l_leg1.fill_color = (89, 156, 165)
    l_leg1.color = (89, 156, 165)
    window.add(l_leg1)
    l_leg2 = GRect(30, 40, x=190, y=340)
    l_leg2.filled = True
    l_leg2.fill_color = (139, 198, 205)
    l_leg2.color = (139, 198, 205)
    window.add(l_leg2)
    l_leg3 = GRect(10, 10, x=190, y=340)
    l_leg3.filled = True
    l_leg3.fill_color = (89, 156, 165)
    l_leg3.color = (89, 156, 165)
    window.add(l_leg3)
    l_leg4 = GRect(10, 20, x=180, y=350)
    l_leg4.filled = True
    l_leg4.fill_color = (89, 156, 165)
    l_leg4.color = (89, 156, 165)
    window.add(l_leg4)
    l_leg5 = GRect(60, 40, x=190, y=380)
    l_leg5.filled = True
    l_leg5.fill_color = (89, 156, 165)
    l_leg5.color = (89, 156, 165)
    window.add(l_leg5)
    l_leg6 = GRect(10, 10, x=230, y=370)
    l_leg6.filled = True
    l_leg6.fill_color = (89, 156, 165)
    l_leg6.color = (89, 156, 165)
    window.add(l_leg6)
    l_leg7 = GRect(10, 10, x=250, y=390)
    l_leg7.filled = True
    l_leg7.fill_color = (89, 156, 165)
    l_leg7.color = (89, 156, 165)
    window.add(l_leg7)
    l_leg8 = GRect(10, 10, x=180, y=370)
    l_leg8.filled = True
    l_leg8.fill_color = (38, 117, 131)
    l_leg8.color = (38, 117, 131)
    window.add(l_leg8)
    l_leg9 = GRect(10, 10, x=190, y=400)
    l_leg9.filled = True
    l_leg9.fill_color = (38, 117, 131)
    l_leg9.color = (38, 117, 131)
    window.add(l_leg9)
    l_leg10 = GRect(10, 10, x=180, y=410)
    l_leg10.filled = True
    l_leg10.fill_color = (38, 117, 131)
    l_leg10.color = (38, 117, 131)
    window.add(l_leg10)
    l_leg11 = GRect(10, 10, x=210, y=410)
    l_leg11.filled = True
    l_leg11.fill_color = (38, 117, 131)
    l_leg11.color = (38, 117, 131)
    window.add(l_leg11)
    l_leg12 = GRect(10, 20, x=220, y=360)
    l_leg12.filled = True
    l_leg12.fill_color = (139, 198, 205)
    l_leg12.color = (139, 198, 205)
    window.add(l_leg12)
    l_leg13 = GRect(20, 10, x=200, y=380)
    l_leg13.filled = True
    l_leg13.fill_color = (139, 198, 205)
    l_leg13.color = (139, 198, 205)
    window.add(l_leg13)
    l_leg14 = GRect(10, 10, x=190, y=410)
    l_leg14.filled = True
    l_leg14.fill_color = (139, 198, 205)
    l_leg14.color = (139, 198, 205)
    window.add(l_leg14)
    l_leg15 = GRect(10, 10, x=220, y=410)
    l_leg15.filled = True
    l_leg15.fill_color = (139, 198, 205)
    l_leg15.color = (139, 198, 205)
    window.add(l_leg15)
    l_leg16 = GRect(10, 10, x=180, y=380)
    l_leg16.filled = True
    l_leg16.fill_color = 'black'
    l_leg16.color = 'black'
    window.add(l_leg16)
    l_leg17 = GRect(10, 10, x=190, y=390)
    l_leg17.filled = True
    l_leg17.fill_color = 'black'
    l_leg17.color = 'black'
    window.add(l_leg17)
    l_leg18 = GRect(20, 10, x=190, y=420)
    l_leg18.filled = True
    l_leg18.fill_color = 'black'
    l_leg18.color = 'black'
    window.add(l_leg18)
    l_leg19 = GRect(20, 10, x=220, y=420)
    l_leg19.filled = True
    l_leg19.fill_color = 'black'
    l_leg19.color = 'black'
    window.add(l_leg19)
    l_leg20 = GRect(10, 10, x=240, y=410)
    l_leg20.filled = True
    l_leg20.fill_color = 'black'
    l_leg20.color = 'black'
    window.add(l_leg20)
    l_leg21 = GRect(10, 10, x=250, y=400)
    l_leg21.filled = True
    l_leg21.fill_color = 'black'
    l_leg21.color = 'black'
    window.add(l_leg21)
    l_leg22 = GRect(10, 10, x=260, y=390)
    l_leg22.filled = True
    l_leg22.fill_color = 'black'
    l_leg22.color = 'black'
    window.add(l_leg22)


if __name__ == '__main__':
    main()
