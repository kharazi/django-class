from django.http import HttpResponse
from django.shortcuts import render


class Person:

    def __init__(self, firstname, lastname, grade=0):
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade

    def get_name(self):
        return "%s %s" % (self.firstname, self.lastname)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)



ali = Person('Ali', 'Alavi', 10)
sara = Person('Sara', 'Saravi', 20)
users = [
    ali, sara
]


def index(request):
    return HttpResponse("<html><title>Salam</title><h1>Salam</h1></html>")


# def user_list(request):
#     user_list_string = ""
#     for u in users:
#         user_list_string += "<li>%s %d</li>" % (u.get_name(), u.grade)

#     print(user_list_string)
#     output = """
#         <html>
#             <title>User List</title>
#             <h1>User List</h1>
#             <ul>
#                 %s
#             </ul>
#         </html>
#     """ % user_list_string
#     return HttpResponse(output)
def validate_user_add_request(data):
    if len(data['firstname']) < 3:
        return False, 'Your firstname must be greater than 3 chars', 'firstname'
    try:
        int(data['grade'])
    except ValueError:
        return False, 'Grade must be an int', 'grade'
    return True, ''


def user_list(request):
    if 'firstname' in request.GET:
        validate = validate_user_add_request(request.GET)
        if validate[0] == True:
            p = Person(
                request.GET['firstname'],
                request.GET['lastname'],
                int(request.GET['grade'])
            )
            users.append(p)
        else:
            return render(
                request,
                'list.html',
                context={
                    'users': users,
                    'title': "List User ha",
                    'test_dict': {
                        "name": "value"
                    },
                    'has_error': True,
                    'error': validate[1],
                    'field': validate[2]
                }
            )
    return render(
        request,
        'list.html',
        context={
            'users': users,
            'title': "List User ha",
            'test_dict': {
                "name": "value"
            }
        }
    )


def user_add(request):
    print(request.GET)
    p = Person(
        request.GET['firstname'],
        request.GET['lastname'],
        int(request.GET['grade'])
    )
    users.append(p)
    print(p)

    return HttpResponse("Ok! saved!")
