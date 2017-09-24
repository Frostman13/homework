from sql_sample import db_session, User

authors = [
    {
        'first_name': 'Василий',
        'last_name': 'Петров',
        'email': 'vasya@example.com',
    },
    {
        'first_name': 'Маша',
        'last_name': 'Иванова',
        'email': 'mari@example.com',
    },
    {
        'first_name': 'Полуэкт',
        'last_name': 'Невоструев',
        'email': 'p@example.com',
    }
]

for author in authors:
    author = User(author['first_name'], author['last_name'], author['email'])
    db_session.add(author)

db_session.commit()