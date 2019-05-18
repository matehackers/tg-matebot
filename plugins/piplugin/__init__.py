# vim:fileencoding=utf-8
#    Plugin piplugin para matebot: Retorna o valor da constante pi
#    Copyleft (C) 2019 Desobediente Civil, Matehackers

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

import math

def pi(tamanho):
  response = str(math.pi)[:int(tamanho)]
  return {
    'status': True,
    'type': 'mensagem',
    'response': response,
    'debug': 'pi',
    'multi': False,
    'parse_mode': None,
  }
