from EdgeGPT import Chatbot, ConversationStyle

async def crawl_email(value):
    bot = Chatbot('./files/cookie.json')


    dct = await bot.ask(prompt="email of" +value, conversation_style=ConversationStyle.precise)
    print(dct['item']['messages'][1]['text'])
    await bot.close()
    return str(dct)         
# if __name__ == "__main__":

