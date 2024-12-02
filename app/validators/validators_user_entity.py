from app.models.user_entity import UserEntity


class ValidatorsUserEntity:

    @staticmethod
    def validateFields(user_entity: UserEntity):

        if not user_entity.getUsername():
            raise ValueError("Username are required")

        if not user_entity.getPassword():
            raise ValueError("password are required")

        if not user_entity.getRole():
            raise ValueError("role are required")

    @staticmethod
    def validateRoles(user_entity: UserEntity):
        if user_entity.getRole() != "admin" and user_entity.getRole() != "user":
            raise ValueError("role not allowed")

    @staticmethod
    def validateField(field:object, field_name: str):
        if not field:
            raise ValueError(f"{field_name} are required")