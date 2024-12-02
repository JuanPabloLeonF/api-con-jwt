from app.configuration.configuration_database import db
import uuid

class UserEntity(db.Model):

    __tablename__ = 'users'

    def __init__(self, username: str, password: str, role:str):
        self.username = username
        self.password = password
        self.role = role

    id:str = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username:str = db.Column(db.String(100), nullable=False)
    password:str = db.Column(db.String(100), nullable=False)
    role:str = db.Column(db.String(10), nullable=False)

    def getUsername(self) -> str:
        return self.username

    def getPassword(self) -> str:
        return self.password

    def getRole(self) -> str:
        return self.role

    def getJSON(self) -> dict:
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password,
            'role': self.role
        }