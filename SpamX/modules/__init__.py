from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "ཽ͡ ⃝𝆺𝅥𝐌ꝛ፝֟ [🖤]❛𝐊ɩŋʛ𝅃꯭᳚𝅃꯭᳚𓄂️𓆪ꪾ"
pic = ALIVE_PIC if ALIVE_PIC else "https://graph.org/file/9a6da16d52fdb628901a6.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "SpamX - by MR KING"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **Master:** {owner_mention}
➠ **Python Version:** `{platform.python_version()}`
➠ **SpamX Version:** `{__version__}`
➠ **Pyrogram Version:** `{pyro_vr}`
➠ **pyMRKING Version:** `{pip_vr}`
➠ **OWNER:** @l_MR_ll_KING_l
━───────╮•╭───────━
➠ **Source Code:** [•Repo•](https://github.com/KING0712/KING_x-SPAM/tree/main)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   All = users_db.get_all_sudos()
   for x in All:
     Sudos.append(x.user_id)
else:
   Sudos = sudoser
