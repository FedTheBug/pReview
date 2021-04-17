<h1 align="center"> pReview </h1>
<h3 align="center"> Simple Microservice based product reviewing application </h3>

#### Clone the project : 
```
git clone https://github.com/FedTheBug/pReview/
```
 #### Admin: 
 - Go the admin folder of the project and run: ``` docker-compose up -d ```
 - Keep the container running and on a different tab run: 
   ```docker-compose exec backend sh ```
   After that, run the following commands: 
      ```python manage.py makemigrations``` &
        ```python manage.py migrate```

##### API Endpoint:
- [Create a Product](#Create-a-Product)
- [List of Products](#List-of-Products)
- [Retrieve a Product](#Retrieve-a-Product)
- [Update a Product](#Update-a-Product)
- [Delete a Product](#Delete-a-Product)
