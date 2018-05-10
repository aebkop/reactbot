import logging
import discord
import asyncio


logging.basicConfig(level=logging.INFO)

robo_thatcher = discord.Client()
trigger_words = {"linux" : "I'd just like to interject for a moment. What you're referring to as Linux, is in fact, GNU/Linux, or as I've recently taken to calling it, GNU plus Linux. Linux is not an operating system unto itself, but rather another free component of a fully functioning GNU system made useful by the GNU corelibs, shell utilities and vital system components comprising a full OS as defined by POSIX.",
                 "microsoft" : "- Microsoft is running a patent protection racket, threatening to sue users of free software.\n- Microsoft's principal wrong is distributing a nonfree operating system, Microsoft Windows.\n- That system is jam-packed with malicious functionalities, including surveillance of users, DRM, censorship and a universal back door.\n- Microsoft tricked users into 'upgrading' to Windows 10.\n- Microsoft Windows 10 forced software changes can sabotage the user terribly if Microsoft chooses an inconvenient time to do them. Since the article is in the mainstream media, it suggests only to buy another computer that serves a master that doesn't do this particular form of nastiness. It completely ignores the possibility of installing a free operating system in the PC—which doesn't even require buying a new computer.\n- Microsoft tablets and phones impose censorship of applications.\n- Microsoft's chatbot in China threatens people who communicate using prohibited words.\n- Microsoft forced a ridiculous 'open' standard, OOXML (used in DOCX files), through the International Standards Organization by corrupting most of the national standards organizations that voted.\n- The specifications document was so long that it would be difficult for anyone else to implement it properly. When the proposed standard was submitted through the usual track, experienced evaluators rejected it for many good reasons.\n- Microsoft responded using a special override procedure in which its money buy the support of many of the voting countries, thus bypassing proper evaluation and demonstrating that ISO can be bought.\n- Microsoft pressured nearly all manufacturers of PCs to pay for a Windows license for every machine sold, thus charging every purchaser for a Windows license.\n- The fee doesn't force you to run Windows on your PC, but it is an injustice nonetheless. One way to avoid it is to buy hardware that is never sold with Windows."}



@robo_thatcher.event
async def on_ready():
    print('Logged in as')
    print(robo_thatcher.user.name)
    print(robo_thatcher.user.id)
    print('------')

@robo_thatcher.event
async def on_message(message):
    if message.author == robo_thatcher.user:
        return
    for key in  trigger_words:
        if key in message.content.lower():
            print("found message")
            await robo_thatcher.send_message(message.channel,trigger_words[key])

robo_thatcher.run('NDQzOTA1MzA2Mzc3MDYwMzUy.DdUbYQ.zokQMbnOzT5npCBhS2VVOIB_42E')
