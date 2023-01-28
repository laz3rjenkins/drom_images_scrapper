from bot.drom_scrapper import BotScrapper


def main():
    try:
        with BotScrapper() as bot:
            bot.parse_drom()
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
