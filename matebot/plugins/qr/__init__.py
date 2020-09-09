# vim:fileencoding=utf-8
#  Plugin qr para matebot: Gera qr code a partir de texto.
#  Copyleft (C) 2016-2020 Desobediente Civil, 2017-2020 Matehackers,
#    2018-2019 Velivery, 2019 Greatful, 2019-2020 Fábrica do Futuro
#  
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import pyqrcode
import tempfile

def cmd_qr(args):
  try:
    return {
      'status': True,
      'type': "image",
      'response': create_qrcode(' '.join(args['command_list'])),
      'debug': u"QR code bem sucedido",
      'multi': False,
      'parse_mode': None,
      'reply_to_message_id': args['message_id'],
    }
  except Exception as e:
    return {
      'status': False,
      'type': "erro",
      'response':  u"Não consegui gerar um qr code com %s\nOs desenvolvedores devem ter sido avisados já, eu acho." % (str(args['command_list'])),
      'debug': u"QR code erro\nExceção: %s" % (e),
      'multi': False,
      'parse_mode': None,
      'reply_to_message_id': args['message_id'],
    }

def create_qrcode(text):
  photo = tempfile.mkstemp(suffix='.png')
  qrcode = pyqrcode.create(str(text), version=10)
  qrcode.png(photo[1], scale=6)
  return {
    'photo': photo, 
    'text': str(text),
  }

## Aiogram
def add_handlers(dispatcher):
  from matebot.aio_matebot.controllers.callbacks import (
    command_callback,
    any_error_callback,
  )
  from aiogram.utils.markdown import escape_md
  
  ## Envia qr code a partir de texto
  @dispatcher.message_handler(
    commands = ['qr', 'qrcode'],
  )
  async def qr_callback(message):
    await command_callback(message, 'qr')
    if message.get_args():
      await message.reply_photo(
        photo = open(str(create_qrcode(message.get_args())['photo'][1]), 'rb'),
        caption = message.get_args(),
      )
    else:
      await message.reply(
        escape_md(u"E o texto? É `/qr texto`"),
        parse_mode = "MarkdownV2",
      )
