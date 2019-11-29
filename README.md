# Django Course

## User app

/user/login


POST 
   - username
   - password

/user/signup


POST 

   - username
   - password
   - first_name
   - last_name
   - email

/user/profile


PUT: edit profile

   - first_name
   - last_name

GET

/user/list
GET: get users list


# Chat app

/chat/conversation

POST

   - conversation_name
   - members (list of user ids)

GET: list of all conversation

/chat/message

POST

   - text
   - conversation_id
 
PUT

   - message_id
   - text

GET: return all messages of conversation_id

   - conversation_id

