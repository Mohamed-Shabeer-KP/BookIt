# BookIt

BookIt is a Django application integrated with DjangoRest Framework for creating and booking slots for appointments.

## Deployed in Heroku

[BookIt Vercel Application](https://book-it-now.vercel.app/)

## Url pattern for API End-points

1. Slot creation  - [https://book-it-now.vercel.app/api/post/](https://book-it-now.vercel.app/api/post/)
1. View all slots - [https://book-it-now.vercel.app/api/list/](https://book-it-now.vercel.app/api/list/)
1. Slot Booking   - ```https://book-it-now.vercel.app/api/book/slot_id/```
1. Slot Remove   -  ```https://book-it-now.vercel.app/api/remove/slot_id/```

```slot_id = The ID of the Slot```

### Postman API Collection : [Link](https://documenter.getpostman.com/view/12165569/T1DqfGCo)

## Sample User data 

For [login](https://book-it-now.vercel.app/login/) in BookIt application.,
```json
{
  "Email": "sam@gmail.com",
  "Password": "sam123"
}
```
For [login](https://book-it-now.vercel.app/api-auth/login/?next=/api/list/) in BookIt API endpoints,
```json
{
  "Username": "sam",
  "Password": "sam123"
}
```
For [Django Admin](https://book-it-now.vercel.app/admin/) page,
```json
{
  "Username": "administrator",
  "Password": "admin"
}
```

## Flow and Bonus points
1. User registration at [link](https://book-it-now.vercel.app/register/).
1. User login and authentication [link](https://book-it-now.vercel.app/login/).
1. User can access API from the UI after login or through API Endpoints.
   1. Create slot  
   1. Book slot 
   1. Update slot  
   1. Remove slot
1. Bonus Points
   1. Unit cases added for API 
        1. single user test
        1. single slot test
        1. single get list test
        
        
## Sample Images
#### Login Page

![index](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/1.png?alt=media&token=236f5c8b-7906-424a-8f41-fe93f8235dec)
---
#### Logged In page

![logged in](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/2.PNG?alt=media&token=bf5136e6-3553-4265-9bfb-878f5f128a3d)
---
#### Create slot API

![create slot api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/3.PNG?alt=media&token=654e1181-e5f7-42fd-9731-f823177fa81d)
---
#### Slot view API

![slot view api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/4.PNG?alt=media&token=fa495ba8-ef63-4fac-970a-fd96f63dd191)
---
#### Book slot API

![book slot api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/5.PNG?alt=media&token=ffe60a93-1171-4eb8-9e7b-b57cf08051c6)
---
#### Remove slot API

![book slot api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/6.PNG?alt=media&token=ad1849b9-ef4c-4305-ad8f-0c43d2ba3248)
---
#### Unauthorized access to api

![unauth api](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/7.PNG?alt=media&token=fb7bae2c-f0aa-4e1d-b0e9-aeaa3318b150)
---
#### Django admin slot model

![admin page slot model](https://firebasestorage.googleapis.com/v0/b/c-dwl-95da6.appspot.com/o/8.PNG?alt=media&token=9ae7e719-ba30-4419-b37d-f383eed9bd85)

