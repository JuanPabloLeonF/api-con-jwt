from app.models.user_entity import UserEntity
from app.repository.user_entity_repository import UserEntityRepository
from app.validators.validators_user_entity import ValidatorsUserEntity


class UserEntityService:

    @staticmethod
    def getALl() -> list[dict]:
        userListData:list[UserEntity] = UserEntityRepository.getALl()
        return [user.getJSON() for user in userListData]

    @staticmethod
    def create(request: dict) -> dict:

        user_entity: UserEntity = UserEntity(
            username=request.get("username"),
            password=request.get("password"),
            role=request.get("role")
        )

        ValidatorsUserEntity.validateFields(user_entity=user_entity)
        ValidatorsUserEntity.validateRoles(user_entity=user_entity)

        user_create:UserEntity = UserEntityRepository.create(user_entity)

        return user_create.getJSON()

    @staticmethod
    def authenticated(request: dict) -> UserEntity:

        username: str = request.get("username")
        password: str = request.get("password")

        ValidatorsUserEntity.validateField(field=username, field_name="username")
        ValidatorsUserEntity.validateField(field=password, field_name="password")

        user_entity:UserEntity = UserEntityRepository.getByUsernameAndPassword(
            username=username,
            password=password
       )

        return user_entity