import logging
from telegram.ext import Updater, CommandHandler

updater = Updater(token='1441191988:AAHmB-nacbXnrmnixlBPWhRPjjKoJ15COgs', use_context=True)
dispatcher = updater.dispatcher

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hallo, dies ist der ThOP Bot, der offizielle Telegram Bot von dem Theater im OP Göttingen.")
    
def reike(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hallo Mareike, wie geht es dir heute?")
    
def info(update, context):
	context.bot.send_message(chat_id=update.effective_chat.id, text="PLÄTZE FREI IM SEMINAR: \"Bühnensprechen: Szenisches Sprechen und Rezitation\" Die Anforderungen an die Stimme für das Sprechen auf der (Theater-)Bühne sind besondere - verglichen mit dem Alltagssprechen oder auch in öffentlichen Vorträgen. Auf dem grundlegenden Training (Atem-, Stimm- und Artikulationsübungen sowie Übungen zur Eutonisierung) aufbauend befassen sich die Teilnehmer*innen praktisch damit, \n- wie sie ihre Kraftstimme entwickeln und den Sprechausdruck variieren können\n- wie sie für Rollensprechen und Rezitation text-, rollen- und situationsangemessen ihre Stimme einsetzen können; dabei lernen sie ebenfalls, verschiedene interpretatorische Ideen stimmlich-sprecherisch umzusetzen\n- welche Rolle die Körpersprache dabei spielt, um einen Bühnentext (fürs Rollensprechen) oder einen zu rezitierenden Text lebendig zu gestalten - und wie die Sprechweise davon profitiert\n- wie sie durch Präsenzübungen die genannten Aspekte schärfen und vertiefen können\nDie Teilnehmer*innen können gerne Texte eigener Wahl oder von ihnen selbst verfasste Texte mitbringen, um unter den o.g. Gesichtspunkten praktisch mit ihnen zu arbeiten.\nAnmeldungen bitte über Stud.IP.")
    
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

info_handler = CommandHandler('info', info)
dispatcher.add_handler(info_handler)

reike_handler = CommandHandler('reike', reike)
dispatcher.add_handler(reike_handler)

updater.start_polling()

"""
TO-DO:

mehr befehle einfuegen,
lange Texte auslagern/schoener speichern und verarbeiten,
Profilbild auf thop logo aendern,
rausfinden wie der Bot bilder schicken kann
"""


