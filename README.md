# DjangoSSO

This is repository a study on SSO authentication between Django and Keycloak.


# QuickStart
1. Clone this repository
2. Create a Keycloak docker
```console
docker run --name keycloak -p 8080:8080 -e KEYCLOAK_USER=admin -e KEYCLOAK_PASSWORD=password  jboss/keycloak
```
3. Configure Keycloak server

    See how to configuration Keycloak server on wiki [Keyclaok Configuration]()

4. Install requeriments
```
pip install -r requirements.txt
```

5. Configuration Django-Keycloak

    See how to configuration Django-Keycloak lib on wiki [Django-Keyclaok Configuration](#)

6. Run migrations Django
```console
python manage.py migrate
```
7. Run application Django
```console
python manage.py runserver
```
## Keycloak server information
* user: admin
* password: password
* url server: http://localhost:8080

## References
* [Django-Keycloak](https://django-keycloak.readthedocs.io/en/latest/#)
* [Keycloak](https://www.keycloak.org/documentation.html)
* [Keycloak Container](https://hub.docker.com/r/jboss/keycloak/)
