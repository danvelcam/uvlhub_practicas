from app.modules.notepad.models import Notepad
from core.repositories.BaseRepository import BaseRepository


class NotepadRepository(BaseRepository):
    def __init__(self):
        super().__init__(Notepad)

    def get_all_by_user(self, user_id):
        return Notepad.query.filter_by(user_id=user_id).all()

    def get_by_id_and_user(self, id, user_id):
        return Notepad.query.filter_by(id=id, user_id=user_id).first()
    
    def get_by_id(self, id):
        return Notepad.query.filter_by(id=id).first()
