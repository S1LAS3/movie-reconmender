from app.services.db_services import create_user, get_users

create_user("Silas")

users = get_users()

for u in users:
    print(u.id, u.name)