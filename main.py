from random import randint
from dotenv import load_dotenv
import discord
import os


STATS_BASE = ('STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA')
DND_CLASSES = {'Artificer': ('INT', 'CON', 'STR', 'WIS', 'DEX', 'CHA'),
               'Barbarian': ('STR', 'CON', 'DEX', 'WIS', 'CHA', 'INT'),
               'Bard': ('CHA', 'DEX', 'CON', 'WIS', 'INT', 'STR'),
               'Cleric': ('WIS', 'CON', 'STR', 'CHA', 'INT', 'DEX'),
               'Druid': ('WIS', 'CON', 'CHA', 'DEX', 'STR', 'INT'),
               'Fighter': ('STR', 'CON', 'DEX', 'WIS', 'CHA', 'INT'),
               'Monk': ('DEX', 'WIS', 'CON', 'CHA', 'INT', 'STR'),
               'Paladin': ('STR', 'CHA', 'CON', 'WIS', 'DEX', 'INT'),
               'Ranger': ('DEX', 'WIS', 'CON', 'STR', 'INT', 'CHA'),
               'Rogue': ('DEX', 'WIS', 'CHA', 'CON', 'INT', 'STR'),
               'Sorcerer': ('CHA', 'CON', 'WIS', 'DEX', 'INT', 'STR'),
               'Warlock': ('CHA', 'DEX', 'WIS', 'CON', 'INT', 'STR'),
               'Wizard': ('INT', 'CON', 'CHA', 'DEX', 'WIS', 'STR')}


def good_generator():
    character = {'class': list(DND_CLASSES.keys())[randint(0, 12)]}
    character['lineage'] = list(dnd_lines.keys())[randint(0, len(dnd_lines)-1)]
    stat_list_good = stat_generator()
    stat_list_good.sort(reverse=True)

    character['stats'] = {}
    good_counter = 0
    for stat_key in DND_CLASSES[character['class']]:
        character['stats'][stat_key] = stat_list_good[good_counter]
        good_counter += 1

    for trait_stat in list(dnd_lines[character['lineage']].keys()):
        change_stat = character['stats'][trait_stat] + dnd_lines[character['lineage']][trait_stat]
        character['stats'][trait_stat] = change_stat

    character['stat-boni'] = {}
    for stats in list(character['stats'].keys()):
        stat_boni_value = (character['stats'][stats]-10)//2
        if stat_boni_value > 0:
            character['stat-boni'][stats] = f'+{stat_boni_value}'
        elif stat_boni_value <= 0:
            character['stat-boni'][stats] = str(stat_boni_value)

    output_good = f'Class:\t\t{character["class"]}\n' \
                  f'Lineage:\t{character["lineage"]}\n\n' \
                  f'STR:\t  {character["stats"]["STR"]} ({character["stat-boni"]["STR"]})\n' \
                  f'DEX:\t {character["stats"]["DEX"]} ({character["stat-boni"]["DEX"]})\n' \
                  f'CON:\t{character["stats"]["CON"]} ({character["stat-boni"]["CON"]})\n' \
                  f'INT:\t   {character["stats"]["INT"]} ({character["stat-boni"]["INT"]})\n' \
                  f'WIS:\t {character["stats"]["WIS"]} ({character["stat-boni"]["WIS"]})\n' \
                  f'CHA:\t{character["stats"]["CHA"]} ({character["stat-boni"]["CHA"]})\n'

    return output_good


def bad_generator():
    character = {'class': list(DND_CLASSES.keys())[randint(0, 12)]}
    character['lineage'] = list(dnd_lines.keys())[randint(0, len(dnd_lines)-1)]
    stat_list_bad = stat_generator()
    stat_list_bad.sort()

    character['stats'] = {}
    bad_counter = 0
    for stat_key in DND_CLASSES[character['class']]:
        character['stats'][stat_key] = stat_list_bad[bad_counter]
        bad_counter += 1

    for trait_stat in list(dnd_lines[character['lineage']].keys()):
        change_stat = character['stats'][trait_stat] + dnd_lines[character['lineage']][trait_stat]
        character['stats'][trait_stat] = change_stat

    character['stat-boni'] = {}
    for stats in list(character['stats'].keys()):
        stat_boni_value = (character['stats'][stats] - 10) // 2
        if stat_boni_value > 0:
            character['stat-boni'][stats] = f'+{stat_boni_value}'
        elif stat_boni_value <= 0:
            character['stat-boni'][stats] = str(stat_boni_value)

    output_bad = f'Class:\t\t{character["class"]}\n' \
                  f'Lineage:\t{character["lineage"]}\n\n' \
                  f'STR:\t  {character["stats"]["STR"]} ({character["stat-boni"]["STR"]})\n' \
                  f'DEX:\t {character["stats"]["DEX"]} ({character["stat-boni"]["DEX"]})\n' \
                  f'CON:\t{character["stats"]["CON"]} ({character["stat-boni"]["CON"]})\n' \
                  f'INT:\t   {character["stats"]["INT"]} ({character["stat-boni"]["INT"]})\n' \
                  f'WIS:\t {character["stats"]["WIS"]} ({character["stat-boni"]["WIS"]})\n' \
                  f'CHA:\t{character["stats"]["CHA"]} ({character["stat-boni"]["CHA"]})\n'

    return output_bad


def avg_generator():
    character = {'class': list(DND_CLASSES.keys())[randint(0, 12)]}
    character['lineage'] = list(dnd_lines.keys())[randint(0, len(dnd_lines)-1)]
    stat_list_avg = stat_generator()

    character['stats'] = {}
    avg_counter = 0
    for stat_key in STATS_BASE:
        character['stats'][stat_key] = stat_list_avg[avg_counter]
        avg_counter += 1

    for trait_stat in list(dnd_lines[character['lineage']].keys()):
        change_stat = character['stats'][trait_stat] + dnd_lines[character['lineage']][trait_stat]
        character['stats'][trait_stat] = change_stat

    character['stat-boni'] = {}
    for stats in list(character['stats'].keys()):
        stat_boni_value = (character['stats'][stats] - 10) // 2
        if stat_boni_value > 0:
            character['stat-boni'][stats] = f'+{stat_boni_value}'
        elif stat_boni_value <= 0:
            character['stat-boni'][stats] = str(stat_boni_value)

    output_avg = f'Class:\t\t{character["class"]}\n' \
                  f'Lineage:\t{character["lineage"]}\n\n' \
                  f'STR:\t  {character["stats"]["STR"]} ({character["stat-boni"]["STR"]})\n' \
                  f'DEX:\t {character["stats"]["DEX"]} ({character["stat-boni"]["DEX"]})\n' \
                  f'CON:\t{character["stats"]["CON"]} ({character["stat-boni"]["CON"]})\n' \
                  f'INT:\t   {character["stats"]["INT"]} ({character["stat-boni"]["INT"]})\n' \
                  f'WIS:\t {character["stats"]["WIS"]} ({character["stat-boni"]["WIS"]})\n' \
                  f'CHA:\t{character["stats"]["CHA"]} ({character["stat-boni"]["CHA"]})\n'

    return output_avg


def help_msg():
    help_response = "Hello, I'm Chaos DnD-Bot\n" \
                    "My purpose is to generate random characters with classes, lineages and stats.\n\n" \
                    "You can type in one of the following commands:\n" \
                    "*!dnd-good*\tGenerates a random character with a good stat spread for the drawn class.\n" \
                    "*!dnd-bad*\tGenerates a random character with a bad stat spread for the drawn class.\n" \
                    "*!dnd-random!*\tGenerates a random character without taking the class into consideration for the stat spread.\n\n" \
                    "For all characters the stat bonuses from lineage is added after assigning the stats for the class.\n" \
                    "Have fun!"

    return help_response


def stat_generator():
    stat_counter = 0
    stat_list = []
    while stat_counter < 6:
        temp_stat_list = []
        temp_stat_list.append(randint(1, 6))
        temp_stat_list.append(randint(1, 6))
        temp_stat_list.append(randint(1, 6))
        temp_stat_list.append(randint(1, 6))

        stat_stack = []
        for x in temp_stat_list:
            if len(stat_stack) == 0:
                stat_stack = [x]
            elif len(stat_stack) > 0:
                if x < stat_stack[0]:
                    stat_stack = [x]
                elif x >= stat_stack[0]:
                    pass
                else:
                    print('Error: find lowest die')
            else:
                print('Error: check stack length')

        temp_stat_list.remove(stat_stack[0])

        result_stat = 0
        for y in temp_stat_list:
            result_stat += y

        stat_list.append(result_stat)
        stat_counter += 1
    return stat_list


def main():
    global dnd_lines
    dnd_lines = {}
    lin_raw = open('dnd_lines.txt')
    for line in lin_raw:
        clean_line = line.strip('\n')
        sep_lines = clean_line.split('\t')
        sep_stats = sep_lines[1].split('; ')
        dict_stat = {}
        for stat in sep_stats:
            sep_single_stat = stat.split(':')
            dict_stat[sep_single_stat[0]] = int(sep_single_stat[1])
        dnd_lines[sep_lines[0]] = dict_stat

    load_dotenv()
    TOKEN = os.getenv('DISCORD_TOKEN')

    client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} has connected to discord')

    @client.event
    async def on_guild_join(guild):
        print(f'{client.user} has joined {guild}')

    @client.event
    async def on_guild_remove(guild):
        print(f'{client.user} was removed from {guild}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content =='!dnd-help':
            print('!dnd-help command executed')
            response = help_msg()
            await message.channel.send(response)

        if message.content =='!dnd-hallo':
            print('!dnd-hallo command executed')
            response = 'Hello DnD World'
            await message.channel.send(response)

        if message.content =='!dnd-good':
            print('!dnd-good command executed')
            response = good_generator()
            await message.channel.send(response)

        if message.content =='!dnd-bad':
            print('!dnd-bad command executed')
            response = bad_generator()
            await message.channel.send(response)

        if message.content =='!dnd-random':
            print('!dnd-random command executed')
            response = avg_generator()
            await message.channel.send(response)

    client.run(TOKEN)


if __name__ == '__main__':
    main()
