from app.modules.notepad.repositories import NotepadRepository
from core.services.BaseService import BaseService


class NotepadService(BaseService):
    def __init__(self):
        super().__init__(NotepadRepository())

    def get_all_by_user(self, user_id):
        return self.repository.get_all_by_user(user_id)

    def get_by_id(self, id):

        patata = "patata"

        return self.repository.get_by_id(id)

    def sumarValores(a, b):
        return a + b


def restaValores(a, b):
    resultado = a - b
    return resultado


print(sumarValores(5, 3))
print(restaValores(10, 2))
