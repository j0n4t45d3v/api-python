from src.model import user_model

user = user_model.User

db = [
    user(id=1, name='John Doe', age=18),
    user(id=2, name='John Doe2', age=15),
    user(id=3, name='John Doe3', age=28)
]


def get_all_user():
    return db


def get_by_id(identity):
    response = None

    for find_user in db:
        if find_user.id == identity:
            response = find_user
    return response


def insert_user(user_request):
    # pega o ultimo item da lista e adiciona mais 1
    identify = db[-1].id + 1
    new_user = user(identify, user_request['name'], user_request['age'])

    db.append(new_user)


def delete_user(id_user):
    check = False
    for find_user in db:
        if find_user.id == id_user:
            db.remove(find_user)
            check = True

    return check


def update_user(id_user, user_update):
    index_user = None

    for find_user in db:
        if find_user.id == id_user:
            index_user = db.index(find_user)

    if index_user is not None:
        if user_update.name_user is not None:
            db[index_user].name_user = user_update.name_user

        if user_update.age_user is not None:
            db[index_user].age_user = user_update.age_user
