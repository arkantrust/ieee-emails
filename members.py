# El archivo csv debe tener los siguientes campos:
# Marca temporal,Nombre,Semestre,Carrera,Código,
# Rol,Correo electrónico,Número de teléfono,
# Algo que te gustaría hacer

# Solo Nombre, Rol y Correo electrónico son necesarios

import csv

class Member:
  def __init__(self, name: str, role: str, email: str):
    self.name = name
    self.membership = role.lower() != 'voluntario'
    self.email = email
  def __str__(self):
    return f'{self.name}, {self.membership}, {self.email}'

def get_all() -> list[Member]:
  members: list[Member] = []
  with open('new_members.csv', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
      member = Member(row['Nombre'], row['Rol'], row['Correo electrónico'])
      members.append(member)
  return members