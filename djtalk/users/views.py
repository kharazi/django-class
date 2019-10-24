from django.http import HttpResponse
from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError


class Person:

    def __init__(self, firstname, lastname, grade=0):
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade

    def get_name(self):
        return "%s %s" % (self.firstname, self.lastname)

    def __str__(self):
        return "%s %s" % (self.firstname, self.lastname)


    def write_in_file(self):
        f = open('users.txt', 'at')
        f.write(
            "%s,%s,%d\n" % (
                self.firstname,
                self.lastname,
                self.grade
            )
        )
        f.close()


users = []
f = open('users.txt', 'rt')
for l in f:

    userdata = l.split(',')
    p = Person(
        userdata[0],
        userdata[1],
        int(userdata[2])
    )
    users.append(p)
f.close()


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
    except MultiValueDictKeyError:
        return False, 'Grade must not empty', 'grade'
 
    return True, ''


def user_list(request):
    print(request.headers)
    if request.method == 'POST':
        
        validate = validate_user_add_request(request.POST)
        if validate[0]:
            p = Person(
                request.POST['firstname'],
                request.POST['lastname'],
                int(request.POST['grade'])
            )
            users.append(p)
            p.write_in_file()
            return HttpResponse("OK")
        else:
            return HttpResponse("Error", status=400)

    elif request.method == 'GET':
        if request.headers['ACCEPT-LANGUAGE'] == 'fa':
            response = render(
                request,
                'list-fa.html',
                context={
                    'users': users,
                    'title': "لیست کاربران",
                    'test_dict': {
                        "name": "value"
                    }
                }
            )
            response['Server'] = 'PHP'
            return response
        else:
            print("users inja", users)
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
