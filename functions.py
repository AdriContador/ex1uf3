MSG1 = 'Introdueix el nom del fitxer: '
MSG2 = 'Introdueix el contingut del fitxer: '

def file_name():
  name= input(MSG1)
  if name[-4:] == '.txt':
    namedef = 'files/' + name
  else:
    namedef = 'files/' + name + '.txt'
  return namedef

def file_add_st(fname):
  f = open(fname, "a+")
  str = input(MSG2)
  f.write(str)
  f.close()