REST API for FSTR pereval.online website


The Federation for Sports Tourism in Russia maintains a database of mountain passes that receives tourist contributions. 
A moderator of Federation will verify the information and saves it to the database.

This is an API solution for a mobile app for Andriod and IOS which would simplify the task of tourists sending data about 
the pass when they have internet connection.


Requirements:

When tourist reach a mountain pass he can take a photo and use the mobile app to submit the information. When this 
tourist push the button 'Send', the mobile app calls submitData methode which accepts data in JSON format.

```json
{
  "beauty_title": "пер. ",
  "title": "Пхия",
  "other_titles": "Триев",
  "connect": "", // что соединяет, текстовое поле
 
  "add_time": "2021-09-22 13:18:13",
  "user": {"email": "qwerty@mail.ru", 		
        "fam": "Пупкин",
		 "name": "Василий",
		 "otc": "Иванович",
        "phone": "+7 555 55 55"}, 
 
   "coords":{
  "latitude": "45.3842",
  "longitude": "7.1525",
  "height": "1200"}
 
 
  level:{"winter": "", //Категория трудности. В разное время года перевал может иметь разную категорию трудности
  "summer": "1А",
  "autumn": "1А",
  "spring": ""},
 
   images: [{data:"<картинка1>", title:"Седловина"}, {data:"<картинка>", title:"Подъём"}]
}
```

The result of submission is status and status message. For example:
```json
{ "status": 200, "message": "OK"}
```
Once an object is submitted, it is assigned "new" status. FSTR experts change its status to "pending" meaning an expert 
is working on it, validate the new object, and then change the status either to "accepted" or "rejected".


## API methods

#### GET /submitData/ method

Returns a list of all mountain passes.

#### POST /submitData/ method

Allows for a single mountain pass submission.

#### GET /submitData/{id}

Retrieves data for a particular mountain pass.

#### PATCH /submitData/{id}

Allows to change a mountain pass attribute values. Returns a JSON response with

- state: 1 for successful update and 0 for unsuccessful update
- message: explains why an update has failed

#### GET/submitData/?user__email=<email>

Return a list of all objects that were sent to the system by the user with the specified email address

