import argparse
from bs4 import BeautifulSoup
from os import system
from colored import fg, bg, attr
import requests
import sys
import raw_soc


parse = argparse.ArgumentParser()

parse.add_argument('-f', '--file', help="local file")
parse.add_argument('-u', '--url', help="url allow")
parse.add_argument('-p', '--proxy', help="proxy change", action='store_true')


arg = parse.parse_args()

def help():
    print("""
all (to show all element)
clear (clear terminal)
<html tag> (to find element eg. p
--class (to find element with class eg. h1 --class <name>)
--id (to find element with id eg. h1 --id <name>)
exit (to exit program)
    """ % (
      fg(2),
      fg(15)  
        )
    )
    

if arg.file:
    system('clear')
    print(fg(11))
    system('figlet element finder')
    print('{0}{1}{2}local file{3}'.format(fg(9), bg(100), attr(1), bg(0)))
    print(fg(15))

    try:
        with open(arg.file) as file:
            soup = BeautifulSoup(file, 'html.parser')
    except:
        print('%sErro file not found%s' % (
            fg(2),
            fg(15)
        )
        )
        sys.exit()

    while True:
        element = input(fg(3)+'@'+fg(1)+'element_find'+fg(3)+'#'+fg(4)+'shell >'+fg(15))
        el = element.split()
        if '--class' in el:
            ind = el.index('--class')
            for i in soup.find_all(el[0], class_=el[ind+1]):
                if '--text' in el:
                    print(i.text)
                else:
                    print(i.prettify())

        elif '--id' in el:
            ind = el.index('--id')
            for i in soup.find_all(el[0], id=el[ind+1]):
                if '--text' in el:
                    print(i.text)
                else:
                    print(i.prettify())

        elif 'clear' in el:
            system('clear')

        elif 'exit' in el:
            print('%sHave a nice day%s' % (
                fg(2),
                fg(15)
                )
            )
            sys.exit()


        elif 'help' in el:
            help()

        elif 'all' in el:
            for i in soup.find_all('html'):
                print(i.prettify())
                    
        else:
            for i in soup.find_all(element):
                if '--text' in el:
                    print(i.text)
                else:
                    print(i.prettify())



elif arg.url:
    system('clear')
    print(fg(11))
    system('figlet Web scraper')
    print(fg(2))
    print('coded by OzO')
    print(fg(15))
    print('{0}{1}{2}online {3}'.format(fg(9), bg(100), attr(1), bg(0)))
    print(fg(15))
    def error():
        print(
            '%sError%s:%scheck url or make sure you are online :)%s' % (
                fg(1),
                fg(15),
                fg(2),
                fg(15)
            )
        )
        sys.exit()

    ul = ['http://facebook.com']
    
    if arg.proxy:
            req = requests.get(ul[0], proxies={
                    'http':'http://l87.103.202.246:3128',
                    'https':'https://104.207.134.203:3128'})
    else:
        try:
        	req = requests.get(arg.url)
        except:
        	error()
        	sys.exit()

    soup = BeautifulSoup(req.content, 'html.parser')
    spl = arg.url.split('//')
    soc = raw_soc.raw_sock(spl[1])
    soc2 = raw_soc.inter_file(arg.url)
    
    while True:

        element = input(
            """|--[%s]-->
|
|_%s@%selement_find(%sonline%s)%s#%sshell >%s""" % (
                ul[0],
                fg(3),
                fg(9),
                fg(2),
                fg(9),
                fg(2),
                fg(31),
                fg(15)
            )
        )
        el = element.split()
        if '--class' in el:
            ind = el.index('--class')
            for i in soup.find_all(el[0], class_=el[ind+1]):
                if '--text' in el:
                    print(i.text)
                else:
                    print(i.prettify())

        elif 'clear' in el:
            system('clear')

        elif 'exit' in el:
            print('%sHave a nice day%s' % (
                fg(2),
                fg(15)
                )
            )
            sys.exit()

        elif 'help' in el:
            help()
            

        elif 'ip' in el:
            print(soc.ip())

        elif 'raw' in el:
            print(soc.req())


        elif 'all' in el:
            for i in soup.find_all('html'):
                print(i.prettify())

        elif '--id' in el:
            ind = el.index('--id')
            for i in soup.find_all(el[0], id=el[ind+1]):
                print(i.prettify())
                
        elif 'robots' in el:
            print(soc2.find())
            
        elif 'show_robots' in el:
            print(soc2.show())
            
        elif 'write_as' in el:
        	ind = el.index('write_as')
        	file = el[ind+1]
        	with open(file, 'w+') as f:
        		f.write(req.text)
        		
        elif 'help' in el:
        	print("""help command
all (show all element)
ip (show ip)
clear (clear terminal)
<html tag> (to find element eg. p
--class (to find element with class eg. h1 --class <name>)
--id (to find element with id eg. h1 --id <name>)
robots (to check robots.txt exits or not)
show_robots (show text of robots.txt)
raw (show raw requests)
write_as <file name> (write html code in file)
exit (to exit program)""")
  
        else:
            for i in soup.find_all(element):
                print(i.prettify())
    

