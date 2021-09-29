# QuizApp
A Quiz App made using Django Rest Framework

## API endpoints can be defined in the following ways : 
- Plain Django views + return JsonResponse
- Use function-based views + @api_view decorator
- Use class-based views + extending the APIView class

## When viewing a list :
- GET - View all objects
- POST - Add a new object

## When viewing an object with given id :
- GET - View object with given id
- PUT - Edit object with given id
- DELETE - Delete object with given id

## Errors : 

1. Invalid base64-encoded string: number of data characters (217) cannot be 1 more than a multiple of 4
 - Solution : Clear your Browser cache and cookies. Delete all old sessions from the DJANGO_SESSION table.

2. serializer call is showing an TypeError: Object of type 'ListSerializer' is not JSON serializable
 - Solution : The problem is that you're sending the serializer itself, rather than the serialized data, to the response. You should change it to:
    self.data = objects.data

3. Django TypeError: argument of type 'PosixPath' is not iterable
 - Solution : A database setting is specified as a Path object. Convert it to str().


## NOTES :
- Django, by defaults gives you a default related_name which is the ModelName (in lowercase) followed by “_set”.    e.g. : Article -> article_set.
