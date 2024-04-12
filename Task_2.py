"""Напишите функцию принимающую на вход только ключевые параметры и возвращающую словарь,
 где ключ — значение переданного аргумента, а значение — имя аргумента.
  Если ключ не хешируем, используйте его строковое представление."""
import typing


def change_param(*, a, b) -> dict:
    """Функция меняет местами имя параметра и значение."""
    params = locals()
    dict = {}
    for k, v in params.items():
        if isinstance(v, typing.Hashable):
            dict[v] = k
        else:
            dict[str(v)] = k
    return dict


if __name__ == '__main__':
    print(change_param(a=[1, 2], b=3))
