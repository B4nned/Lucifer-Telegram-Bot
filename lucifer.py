#!/usr/bin/env python
# coding: utf-8
######################
# Lucifer Bot - BETA #
#    @PirateSec      #
#   #PirateSexy      #
######################

# imports
import os
import socket
import sock
import re
import random
from functools import partial
import subprocess
import telepot
from telepot.namedtuple import InlineQueryResultArticle
from pprint import pprint
import time
import sys
# end imports


################################
os.system("clear")             #
                               # Limpa o cmd e define a codificação
reload(sys)                    #
sys.setdefaultencoding('utf8') #
################################

# função para adcionar/remover estrelas do registro
def write_register(add_star, user_id, user):
    added = False
    with open('registro.txt', 'r') as file:
        line = 0
        conteudo = file.read()
        x = conteudo.split('\n')
        line_count = 0
        for line in x:
            line_count += 1
            if line.split('|')[0] == str(user_id):
                estrelas_count = int(line.split('|')[2])
                added = True
                break
        file.close()
        if not added:
            with open('registro.txt', 'a') as file:
                file.write(str(user_id) + '|' + user + '|0\n')
                file.close()
                return

    with open('registro.txt', 'w') as file:
        if add_star == True:
            estrelas_count += 1
        else:
            estrelas_count -= 1
        line_count1 = 0
        for line in x:
            line_count1 += 1
            if line_count == line_count1:
                print(line)
                print(line.split('|')[:-1])
                x[line_count1 - 1] = str(line.split('|')[0]) + '|' + str(line.split('|')[1]) + '|' + str(estrelas_count)
                content = ''
                for item in x:
                    content += item + '\n'
                file.write(content)
# end função register

# função handle
def handle(msg):
    # função para reply
    def response(id, response):
        bot.sendMessage(id, response, reply_to_message_id=chat_msgid, parse_mode='Markdown')

    # Welcome msg
    usr = '@' + msg['from']['username']
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == "new_chat_member":
        if (chat_id == -1001071202103):
            bot.sendMessage(chat_id, open('welcome.txt', 'rb') % (usr), reply_to_message_id=True)
        elif (chat_id == -1001098199154):
            bot.sendMessage(chat_id, '%s, seja bem vindo ao I N F E R N O!' % (usr), reply_to_message_id=True)
        else:
            bot.sendMessage(chat_id, '%s, seja bem vindo!' % (usr), reply_to_message_id=True)
    # end welcome msg

     # Variaveis 1
    stars = 'registro.txt'
    id = msg['from']['id']
    chat_msgid = msg['message_id']
    chat_id = msg['chat']['id']
    message = msg['text'].split()
    command = re.sub('\@lucif_bot$', '', message[0])
    len_msg = len(message)
    user_user = '@' + msg['from']['username']
    username = msg['from']['first_name']
    username1 = "@" + username
    adm_id  =  [174766155, 215451257, 275659644,
                327848798, 275659644, 307138341,
                187826755, 234365262, 206525832]
    commands =['/id', '/help', '/afk', '/link',
               '/ping', '/chatid', '/id', '/rules',
               '/ranking', '/rank_clear', '/github', '/admins',
               '/src', '/pull', '/lib', '/check',
               '/shodan', '/tcp', '/whois', '/rt',
               '/cc', '!exploit', '/onion', '/telnet',
               '/dns_base', '/mx', '/dev', '/axfr',
               '/soa_record']

    inv = re.compile(r'[<>/{}[\]~>|;]')
    # end variaveis 1

    # Comandos
    if command in commands:
        if command == '/help':
            try:
                opn = open('help.txt', 'r')
                opn_read = opn.read()
                bot.sendMessage(chat_id, '%s' % (opn_read))
                opn.close()
            except:
                bot.sendMessage(chat_id,"[!]Mensagem desabilitada temporariamente")

        elif command == '/id':
            bot.sendMessage(chat_id, '%s |ID > %s' % (user_user, id))

        elif command == '/chatid':
            if (id in adm_id):
                bot.sendMessage(chat_id, '%s' % (chat_id))
            else:
                bot.sendMessage(chat_id, 'Você não tem permissão para isso!')

        elif command == '/link':
            if (chat_id == -1001071202103):
                bot.sendMessage(chat_id, 'https://telegram.me/joinchat/DNeGeT_ZPzd17eQb8se8lA')
            elif (chat_id == -1001098199154):
                bot.sendMessage(chat_id, 'https://t.me/joinchat/AAAAAEF1MHLddqCACjGkfg')
            elif (chat_id == -1001112510856):
                bot.sendMessage(chat_id, 'https://t.me/joinchat/AAAAAEJPkYhK4rPq898UiA')
            else:
                bot.sendMessage(chat_id, 'Link indisponível!')

        elif command == '/afk':
            bot.sendMessage(chat_id, 'Usuário %s está AFK!' % (user_user), reply_to_message_id=True)


        elif command == '/dev':
            dev = open('dev.txt', 'r')
            dev1 = dev.read()
            bot.sendMessage(chat_id, '%s' % (dev1))
            dev.close()

        elif command == '/ping':
            if (id in adm_id):
                bot.sendMessage(chat_id, 'pong')
            else:
                bot.sendMessage(chat_id, 'Você não tem permissão para isso!')

        elif command == '/rules':
            if (chat_id == -1001092885502):
                bot.sendMessage(chat_id, 'Regras:\n\n- Proibido OffTopic.\n\n-Proibido desrespeito.\n\n- Proibido ameaças.\n\n- Proibido envio de arquivos maliciosos.\n\nEspero que gostem do grupo e que respeitem as regras.')
            elif (chat_id == -1001071202103):
                bot.sendMessage(chat_id, '%s, me inicie e te enviarei as regras do grupo no privado :)' % (user_user))
                opn = open('regras.txt', 'r')
                opn_read = opn.read()
                bot.sendMessage(id, '%s' % (opn_read))
                opn.close()

        elif command == '/ranking':
            opn = open(stars, 'r')
            opn_read = opn.read()
            bot.sendMessage(chat_id, 'Stars Ranking:\n%s' % (opn_read))
            opn.close()

        elif command == '/rank_clear':
            if (id == 174766155):
                os.system("rm registro.txt && echo '\n' > registro.txt")
                bot.sendMessage(chat_id, 'Rank esvaziado!')
            else:
                bot.sendMessage(chat_id, 'Você não tem permissão para isso!')

        elif command == '/github':
            bot.sendMessage(chat_id, 'Nosso Github:\nhttp://github.com/JacquesFernandes/pirate-security')

        elif command == '/admins':
            if (chat_id == -1001071202103):
                opn = open('admins', 'r')
                opn_read = opn.read()
                bot.sendMessage(chat_id, '%s' % (opn_read))
                opn.close()
            else:
                bot.sendMessage(chat_id, 'Admins não setados!')

        elif command == '/src':
            if (id in adm_id):
                bot.sendMessage(chat_id, '[+] Source enviado no grupo de desenvolvimento!')
                bot.sendDocument(-185766487, open('lucifer.py', 'rb'))
            else:
                bot.sendMessage(chat_id, 'Você não tem permissão para isso!')

        elif command == '/pull':
            r = random.randint(0,3)
            if r == 0:
                bot.sendMessage(chat_id, 'BOOSTED!\nUsuário %s foi banido!' % user_user)
                bot.kickChatMember(chat_id, user_user)
            else:
                bot.sendMessage(chat_id, '*Click!*')

        elif command == '/lib':
            bot.sendMessage(chat_id, """[*] Bot programado com a lib Telepot.
            Docs: http://telepot.readthedocs.io/en/latest/
            Github: https://github.com/nickoala/telepot\
            """) #leo lindo

        elif command == '/check':
            if len_msg > 1:
                host = msg['text'].split(' ', 1)[1]
                dominio = host.split('.')
                print dominio
                if dominio[1] != 'onion':
                    bot.sendMessage(chat_id, '[*] Pinging %s' % host)
                    checkr = socket.gethostbyname('%s' % host)
                    bot.sendMessage(chat_id, 'IP: %s' % checkr)
                else:
                    onion = msg['text'].split(' ', 1)[1]
                    print "Onion> " + str(onion)
                    if len(onion) == 22:
                        if not inv.search(onion):
                            bot.AXFsendMessage(chat_id, '[*] Checking if %s is alive...' % onion)
                            onion_check = os.system("torsocks curl -s "+onion+" >/dev/null 2>/dev/null")
                            if onion_check == 0:
                                bot.sendMessage(chat_id, '[+] Host %s online!' % onion)
                            elif onion_check > 0:
                                bot.sendMessage(chat_id, '[-] Host %s offline!' % onion)
                        else:
                            bot.sendMessage(chat_id, 'Hoje não serei ownado.')
                    else:
                        bot.sendMessage(chat_id, '[-] Invalid host!')
            else:
                bot.sendMessage(chat_id, '[!] Digite um host após o comando e eu o verificarei!')

        elif command == '/shodan':
            if len_msg > 1:
                service = msg['text'].split(' ', 1)[1]
                if inv.search(service):
                    bot.sendMessage(chat_id, 'Hoje não serei ownado.')
                else:
                    bot.sendMessage(chat_id, '[*] Crawling %s IPs...' % service)
                    os.system("python ssh.py "+service+" > ips.txt")
                    bot.sendMessage(chat_id, '[+] Done!')
                    bot.sendDocument(chat_id, open('ips.txt', 'rb'))
            else:
                bot.sendMessage(chat_id, '[!] Digite o serviço que você deseja > /shodan <service> | Ex: /shodan openssh')

#        elif command == '/traceroute':
#            if len_msg > 1:
#                tracer = msg['text'].split(' ', 1)[1]
#                bot.sendMessage(chat_id, '[*] Tracing route %s...' % tracer)
#                os.system("traceroute "+tracer+" > tracer.txt")
#                opn = open('tracer.txt', 'r')
#                opn_read = opn.read()
#                bot.sendMessage(chat_id, '[+] Done!')
#                bot.sendMessage(chat_id, '%s' % (opn_read))
#                opn.close()

        elif command == '/cc':
            if len_msg > 1 :
                number = msg['text'].split(' ', 1)[1]
                def d(string):
                    l = len(string)
                    oS = 0
                    eS = 0

                    if (l == 0):
                        return 0
                    else:
                        if (l % 2 == 0 ):
                            la = int(string[-1])
                            eS += la
                            return eS + d(string[:-1])
                        else:
                            la = int(string[-1])
                            la = 2 * la
                            ps = la // 10 + la % 10
                            oS += ps

                            return oS + d(string[:-1])
                def lunhs():
                    string = '%s' % number
                    t = d(string)

                    if(t % 10 == 0):
                        bot.sendMessage(chat_id, '[+] Valid Card!')
                        x = number[0:2]
                        master = ['51', '53', '55']
                        visa = ['40', '44', '45', '47']
                        discover = ['60']
                        american = ['34', '37']

                        if x in master:
                            bot.sendMessage(chat_id, '[+] Possible CC Type > Mastercard')
                        elif x in visa:
                            bot.sendMessage(chat_id, '[+] Possible CC Type > Visa')
                        elif x in discover:
                            bot.sendMessage(chat_id, '[+] Possible CC Type > Discover')
                        elif x in american:
                            bot.sendMessage(chat_id, '[+] Possible CC Type > American Express')
                    else:
                        bot.sendMessage(chat_id, '[-] Invalid Card!')
                def main():
                    lunhs()
                main()
            else:
                bot.sendMessage(chat_id, '[!] Digite o número do cc após o comando e eu verificarei se é válido!')

        elif command == '/onion':

            if len_msg > 1:
                onion = msg['text'].split(' ', 1)[1]
                if len(onion) == 22:
                    if not inv.search(onion):
                        bot.sendMessage(chat_id, '[*] Checking if %s is alive...' % onion)
                        onion_check = os.system("torsocks curl -s "+onion+" >/dev/null 2>/dev/null")
                        if onion_check == 0:
                            bot.sendMessage(chat_id, '[+] Host %s online!' % onion)
                        elif onion_check > 0:
                            bot.sendMessage(chat_id, '[-] Host %s offline!' % onion)
                    else:
                        bot.sendMessage(chat_id, 'Hoje não!')
                else:
                    bot.sendMessage(chat_id, '[-] Invalid host!')
            else:
                bot.sendMessage(chat_id, '[!] Digite o host após o comando e eu verificarei se ele está online!')

        elif command == '/dns_base':
            if len_msg > 1:
                dns_base = msg['text'].split(' ', 1)[1]
                bot.sendMessage(chat_id, '[*] Checking %s dns base...' % (dns_base))
                os.system('host -t ns %s > dns_base.txt' % (dns_base))
                dns_base1 = open('dns_base.txt', 'r')
                dns_base2 = dns_base1.read()
                #teste de segurança
                if not inv.search(dns_base):
                    bot.sendMessage(chat_id, '%s' % (dns_base2))
                    dns_base1.close()
                else:
                    bot.sendMessage(chat_id, 'Hoje não!')
            else:
                bot.sendMessage(chat_id, '[!] Digite o host após o comando e eu verificarei seu DNS BASE!')

        elif command == '/axfr':
            if len_msg > 1:
                dns_base = msg['text'].split(' ', 1)[1]

                bot.sendMessage(chat_id, '[*] Checking %s AXFR...' % (dns_base))
                os.system('host -l %s > dns_base.txt' % (dns_base))
                dns_base1 = open('dns_base.txt', 'r')
                dns_base2 = dns_base1.read()
                bot.sendMessage(chat_id, '%s' % (dns_base2))
                dns_base1.close()

        elif command == '/soa_record':
            if len_msg > 1:
                dns_base = msg['text'].split(' ', 1)[1]

                bot.sendMessage(chat_id, '[*] Checking %s SOA Records...' % (dns_base))
                os.system('host -C %s > dns_base.txt' % (dns_base))
                dns_base1 = open('dns_base.txt', 'r')
                dns_base2 = dns_base1.read()
                bot.sendMessage(chat_id, '%s' % (dns_base2))
                dns_base1.close()

        elif command == '/mx':
        	if len_msg > 1:
        		mx = msg['text'].split(' ', 1)[1]
        		bot.sendMessage(chat_id, '[*] Checking %s MX register' % (mx))
        		os.system('host -t mx %s > mx.txt' % (mx))
        		mx1 = open('mx.txt', 'r')
        		mx2 = mx1.read()
        		bot.sendMessage(chat_id, '%s' % (mx2))
        		mx1.close()
       		else:
        		bot.sendMessage(chat_id, '[!] Digite o host após o comando e eu verificarei seu registro MX!')

#        elif command == '/tcp':
#            if len_msg > 1:
#                tcp = msg['text'].split(' ', 1)[1]
#                bot.sendMessage(chat_id, '[*] Checking tcp ports from %s' % tcp)
#                nm.scan(hosts='%s/24' % tcp, arguments='-n -sP -PE -PA21,23,80,3389')
#                hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
#                for host, status in hosts_list:
#                    bot.sendMessage(chat_id, '{0}:{1}'.host)
#            else:
#                bot.sendMessage(chat_id, '[-] Digite um host após o comando e eu o verificarei!')

#        elif command == '/whois':
#            if len_msg > 1:
#                host = msg['text'].split(' ', 1)[1]
#                bot.sendMessage(chat_id, '[+] Whois %s...' % host)
#                whois = os.system("whois "+host+" | grep -Ei 'owner|ownerid|responsible|person|e-mail' > whois.txt")
#                opn = open('whois.txt', 'r')
#                opn_read = opn.read()
#                bot.sendMessage(chat_id, '[*] Done!')
#                bot.sendMessage(chat_id, '%s' % (opn_read))
#                opn.close()

    # end commands


    # Variaveis 2 [reply]
    reply_to_message = message
    sender = msg['from']['id']
    try:
        reply_id = msg['reply_to_message']['from']['id']
        reply = '@' + msg['reply_to_message']['from']['username']
    except:
        inutil_command = ""
    command_reply = ['/star+', '/star-', '/report', '/expurgar', '/unban', '/rt' ]
    commands_rp = ['/star+', '/star-', '/report', '/expurgar', '/unban', '/rt', '/id_user']
    # end variaveis 2

    # Comandos reply
    if sender:
        if command in commands_rp:

            if command == '/star+':
                if (sender != reply_id):
                    s = bot.sendMessage(chat_id, 'Usuário %s recebeu 1 star! :) | id: %s' % (reply, reply_id))
                    write_register(True, reply_id, reply)
                elif (sender == reply_id):
                    bot.sendMessage(chat_id, 'Impossível dar stars para sí mesmo | id: %s' % reply_id)

            elif command == '/star-':
                if (sender != reply_id):
                    bot.sendMessage(chat_id, 'Usuário %s recebeu 1 star negativa! :( | id: %s' % (reply, reply_id))
                    write_register(False, reply_id, reply)
                elif (sender == reply_id):
                    bot.sendMessage(chat_id, 'Impossível dar stars para sí mesmo | id: %s' % reply_id)

            elif command == '/report':
                if reply_id not in adm_id and sender != reply_id:
                    bot.sendMessage(chat_id, '[*] Usuário %s reportado para os administradores. | ID: %s' % (reply, reply_id))
                    reply_msg = msg['reply_to_message']['text']
                    bot.sendMessage(-185766487, '[*] Usuário %s foi reportado | ID: %s ' % (reply, reply_id))
                    bot.sendMessage(-185766487, 'Mensagem reportada de %s:\n\n%s' % (reply, reply_msg))
                else:
                    bot.sendMessage(chat_id, 'Você não pode reportar administradores ou sí mesmo!')

            elif command == '/expurgar':
                if (sender in adm_id):
                    if (reply_id not in adm_id):
                        bot.sendMessage(chat_id, 'Usuário %s agora queimará no fogo do inferno!' % (reply))
                        bot.kickChatMember(chat_id, reply_id)
                    elif (reply_id in adm_id):
                        bot.sendMessage(chat_id, 'Voce nao pode banir administradores!')
                    elif (chat_id == -1001063955731) and (sender == 206525832):
                        bot.sendMessage(chat_id, 'Usuário %s agora queimará no fogo do inferno!' % (reply))
                        bot.kickChatMember(chat_id, reply_id)

                    elif (reply_id == 307138341):
                        bot.sendMessage(chat_id, 'Você não pode me banir, eu sou a lei.')
                elif (sender not in adm_id):
                    bot.sendMessage(chat_id, 'Você não tem permissão para isso!')

            elif command == '/unban':
                if (sender in adm_id):
                    bot.unbanChatMember(chat_id, reply_id)
                    bot.sendMessage(chat_id, 'Usuário %s desbanido!' % (reply))
                else:
                    bot.sendMessage(chat_id, 'Você não tem permissao para isso!')
            elif command == '/rt':
                reply_msg = msg['reply_to_message']['text']
                if (chat_id == -1001098199154):
                    bot.sendMessage(chat_id, '[+] Mensagem encaminhada para o grupo de on-topic!')
                    bot.sendMessage(-1001071202103, 'Mensagem encaminhada de %s:\n\n%s' % (reply, reply_msg))
                elif (chat_id == -1001071202103):
                    bot.sendMessage(chat_id, '[+] Mensagem encaminhada para o grupo de off-topic!')
                    bot.sendMessage(-1001098199154, 'Mensagem encaminhada de %s:\n\n%s' % (reply, reply_msg))

            elif command == '/id_user':
                bot.sendMessage(chat_id, 'Usuário: %s | id: %s' % (reply, reply_id))
    # end comandos reply

    # IA BETA

    elif command == 'Lucifer' or 'lucifer':
        if len_msg > 1:
            msg['text'].split(' ', 1)[1]
            bot.sendMessage(chat_id, 'Sim?')




    # printa o comando enviado no terminal
    print 'Comando enviado por %s > %s' % (user_user, command)
    # end print

# end função handle

# API + Start
bot = telepot.Bot("") # Telegram API token
bot.message_loop(handle)
print 'Online!'
# end

# mantem o bot rodando
while 1:
    pass
# end
