import allure


@allure.title('Получаем UUID юзера')
def get_user_uuid(user_add_model):
    user_uuid = user_add_model[1].user

    return user_uuid
