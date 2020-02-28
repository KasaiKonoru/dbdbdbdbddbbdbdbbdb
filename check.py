import os
import json
from discord.ext import commands


########################################################################################################################
def is_vale():
    def predicate(ctx):
        return ctx.author.id in [359722265430065152, 356037703319683075, ]

    return commands.check(predicate)


########################################################################################################################
def set_channel(sid: str, cid: str):
    if not os.path.isfile("Tatsuka"):
        try:
            os.mkdir("Tatsuka")
        except:
            pass
    if not os.path.isfile("online.json"):
        online = {sid: {}}
        online[sid] = cid
        with open('online.json', 'w') as fp:
            json.dump(online, fp, sort_keys=True, indent=4)
        return 'Der Channel wurde erfolgreich gesetzt'
    else:
        with open('online.json', 'r') as fp:
            online = json.load(fp)
        if sid in online:
            online[sid] = cid
            with open('online.json', 'w') as fp:
                json.dump(online, fp, sort_keys=True, indent=4)
            return 'Der Channel wurde erfolgreich geÃ¤ndert'
        else:
            online = {sid: {}}
            online[sid] = cid
            with open('online.json', 'w') as fp:
                json.dump(online, fp, sort_keys=True, indent=4)
            return 'Der Channel wurde erfolgreich gesetzt'


def request_channel(sid: str):
    if not os.path.isfile("Tatsuka"):
        try:
            os.mkdir("Tatsuka")
        except:
            pass
    if os.path.isfile("online.json"):
        with open('online.json', 'r') as fp:
            online = json.load(fp)
        if sid in online:
            return online[sid]
        else:
            return None
    else:
        return None


def del_channel(sid: str):
    if not os.path.isfile("Tatsuka"):
        try:
            os.mkdir("Tatsuka")
        except:
            pass
    if os.path.isfile("online.json"):
        with open('online.json', 'r') as fp:
            online = json.load(fp)
        if str(sid) in online:
            try:
                del online[sid]
            except:
                pass
            with open('online.json', 'w') as fp:
                json.dump(online, fp, sort_keys=True, indent=4)
            return 'Done'
        else:
            return 'Dein Server ist nicht in der Datenbank'
    else:
        return 'Dein Server ist nicht in der Datenbank'
