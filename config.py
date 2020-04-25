# This file should be included in .gitignore to not store sensitive data in version control
import os
SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

auth0_config = {
    "AUTH0_DOMAIN" : "fsnd-rohit.auth0.com",
    "ALGORITHMS" : ["RS256"],
    "API_AUDIENCE" : "Music"
}

pagination = {
    "example" : 10 # Limits returned rows of API
}

bearer_tokens = {
    "casting_assistant" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhZa3IyTU5fVkhILWMxSEZCUURhdSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtcm9oaXQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTM3NDAwMWNjMWFjMGMxNDYzY2QzMiIsImF1ZCI6Ik11c2ljIiwiaWF0IjoxNTg3NzcyNjMxLCJleHAiOjE1ODc3Nzk4MzEsImF6cCI6Ind3UjhZdkVFQUNyaEl1VXlpc0xHRGNEU1N1UDRNT1FrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.kPNb_ahkcvsy1a7QGbKi7IxQA8gawL8bAIxiJq6IHtQm-iVytJjkjw4iYxF7b1KcYfonlNn__FJHvyJFaeiST0QB9uCbzJZ3fDyk8lJtKUyNfi4waVQVSgyUcD3JAjh2Fk8FQBxNN7cm8eO7dlaqsvS-c0Te5jFVlKXNuKVg9e-TAzXx7Cmo6_t3cdaZTJPwB0_vMTfrg8_ejyzAvJIX38ibQ_608YczqGj_sWEEHnZU1cC1TK0rcr1eXMGMuF2WtJzMHsW_MfTmuwyvqvG0Gwg5bNcpIIvg0Gk_DCqu3z807yY3_zSCL8ue7QP-r5Rgv98nmyifZKLnkugTcMt_6g",
    "executive_producer" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhZa3IyTU5fVkhILWMxSEZCUURhdSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtcm9oaXQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTM3MzgyNmI2OWJjMGMxMmQzNWI0NCIsImF1ZCI6Ik11c2ljIiwiaWF0IjoxNTg3NzczMTEwLCJleHAiOjE1ODc3ODAzMTAsImF6cCI6Ind3UjhZdkVFQUNyaEl1VXlpc0xHRGNEU1N1UDRNT1FrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJjcmVhdGU6YWN0b3JzIiwiY3JlYXRlOm1vdmllcyIsImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZWRpdDphY3RvcnMiLCJlZGl0Om1vdmllcyIsInZpZXc6YWN0b3JzIiwidmlldzptb3ZpZXMiXX0.v0iPh6fXBgS_pStoKE0v5RjrgtEjqoJ2pu-VNVU2HaaxbATzZStHLq10zScbnfnhsye2CfgjXldz8vquMutMZxw9SHaXhWqenfR1ntiKwEkMsmJqbL0QPackTTyghKQpVGNiD_RhuMXKV8AOs0C6L5pUDgfJhvTVjI7pGcwbUaL1vt7gu7TdPvL_dytPOKP1wAIZ5pGOKygGBZ_qNTFFtbJNypQbJAIR3xl2EevOAQ6z-KYjxGSxVDCImT6WP7VMxuzsh0JPelQflYgTe2ibOf2NsxCZSVia5VPxB2YYn2lMcFnQqc_HdjPYCSPF31G1VU9jv-iEauGyxgjxD3vK0A",
    "casting_director" : "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IkhZa3IyTU5fVkhILWMxSEZCUURhdSJ9.eyJpc3MiOiJodHRwczovL2ZzbmQtcm9oaXQuYXV0aDAuY29tLyIsInN1YiI6ImF1dGgwfDVlYTM3M2NlNmI2OWJjMGMxMmQzNWJmMyIsImF1ZCI6Ik11c2ljIiwiaWF0IjoxNTg3NzcyOTQ5LCJleHAiOjE1ODc3ODAxNDksImF6cCI6Ind3UjhZdkVFQUNyaEl1VXlpc0xHRGNEU1N1UDRNT1FrIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJjcmVhdGU6YWN0b3JzIiwiZGVsZXRlOmFjdG9ycyIsImVkaXQ6YWN0b3JzIiwiZWRpdDptb3ZpZXMiLCJ2aWV3OmFjdG9ycyIsInZpZXc6bW92aWVzIl19.DUaiZagsF1ygbVe4NGFnEnEV5NZTP8jSPnTB51pwg-ujFm2CPA4GttRu4yRCSw3Kp-lxDRgYKZwFqZ96PXowcs8gWPd11mdeedrXIUDH_cLuZSfOC5Yh3fkT8l6hd99k6iwXc51-kzEtWSXbrWRHZVh0yCS4fjFTMGnpUkqroUSt57rFXOZyt2Gu2w2poSIIGvS1nNpP-huPfN8KCjVnEgHO9qDyDWdkczL6c66HbOZfOfIvK5cI29pv-yxTy-bI-ztCCTcORNhAPlW_k47v3lBMzqqVivqprMnqBdrzQw1SD7V5CokeCCds-S71oZ515xi0OO9r88YBxekS1ItfZg"
}

# Enable debug mode.
#DEBUG = True

# Connect to the database
SQLALCHEMY_TRACK_MODIFICATIONS = False

# TODO IMPLEMENT DATABASE URL
#SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]
# print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Brilltez@321@localhost/agency"