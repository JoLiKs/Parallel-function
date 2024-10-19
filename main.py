async def scheduled_offer():
    while True:
        now = datetime.datetime.now().time()
        #await asyncio.sleep(1)
        if now.minute == 0 and now.second == 1: #делать что-то раз в час
            pass



def main():
 
    loop = asyncio.get_event_loop()
    loop.create_task(scheduled_offer()) #функция, которая будет работать параллельно 
    try:
        loop.run_until_complete(application.run_polling()) #запуск основной функции (например, бот)
    except KeyboardInterrupt:
        pass
    finally:
        loop.close()



if __name__ == '__main__':
    main()
