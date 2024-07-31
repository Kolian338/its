from assertpy import assert_that

from api_tests.tla.schemas.db.disp_shedule import DispSheduleDB
from api_tests.tla.schemas.response.disp_schedule import (
    DispSheduleCreateUpdateResponse
)


# Нужно доработать метод и подумать нужен ли он.
def validate_from_response_to_db_disp_schedule(
        response_data: DispSheduleCreateUpdateResponse,
        db_data_list: list[DispSheduleDB]
):
    """
    Сравнивает данные из ответа API с данными из базы данных и
     проверяет их соответствие.

     Args:
        response_data (DispSheduleCreateUpdateResponse): Объект ответа API,
         содержащий список расписаний.
        db_data_list (list): Список объектов базы данных,
         соответствующих расписаниям из ответа API.
    """
    if not response_data:
        raise ValueError('Пустой ответ от АПИ')
    if not db_data_list:
        raise ValueError('Пустой объект из БД')

    api_infos = sorted(response_data.info, key=lambda x: x.guid)
    db_data_list = sorted(db_data_list, key=lambda x: x.guid)

    if len(api_infos) != len(db_data_list):
        raise ValueError(
            'Количество элементов в ответе API и базе данных не совпадает'
        )

    for api_info, db_data in zip(api_infos, db_data_list):
        assert_that(api_info.guid).is_equal_to(db_data.guid)
        assert_that(api_info.caption).is_equal_to(db_data.caption)
        assert_that(api_info.type).is_equal_to(db_data.type)
        assert_that(api_info.timeon).is_equal_to(str(db_data.time_on))
        assert_that(api_info.timeoff).is_equal_to(str(db_data.time_off))
        # assert_that(api_info.tasks).is_equal_to(db_data.tasks)

        api_objs_sorted = sorted(api_info.objs, key=lambda x: x.guid)
        db_objs_sorted = sorted(db_data.objs, key=lambda x: x.guid)

        assert_that(len(api_objs_sorted)).is_equal_to(len(db_objs_sorted))
        for api_obj, db_obj in zip(api_objs_sorted, db_objs_sorted):
            # assert_that(api_obj.id).is_equal_to(db_obj.id)
            assert_that(api_obj.guid).is_equal_to(db_obj.guid)
            assert_that(api_obj.command).is_equal_to(db_obj.command)
