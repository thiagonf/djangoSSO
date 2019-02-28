# DjangoSSO

This is repository a study on SSO authentication between Django and Keycloak.


# QuickStart
1. Clone this repository
2. Create a Keycloak docker
```console
docker run --name keycloak -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=password  jboss/keycloak
```
3. Install requeriments
```
pip install -r requirements.txt
```
4. Run migrations Django
```console
python manage.py migrate
```
5. Run application Django
```console
python manage.py runserver
```
## Keycloak server information
* user: admin
* password: password
* url server: http://localhost:8080

