from app.configuration.configuration_database import db
from app.models.user_entity import UserEntity


class UserEntityRepository:

    @staticmethod
    def getALl():
        return UserEntity.query.all()

    @staticmethod
    def getByUsernameAndPassword(username:str,password:str) -> UserEntity:
        user_find: UserEntity = UserEntity.query.filter_by(
            username=username,
            password=password
        ).first()

        if not user_find:
            raise ValueError("User not found")
        return user_find

    @staticmethod
    def create(user_entity: UserEntity) -> UserEntity:
        db.session.add(user_entity)
        db.session.commit()
        return db.session.merge(user_entity)