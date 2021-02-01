import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database


# TODO IMPLEMENT DATABASE URL
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost:5432/capstone'
SQLALCHEMY_TRACK_MODIFICATIONS = False


AUTH0_DOMAIN = 'dev-4dkx4uqj.us.auth0.com'
API_AUDIENCE = 'https://capstone/'
# maxtee
CASTING_DIRECTOR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwNDMzYzY5ZWU4OGIwMDc3NmRiOWVjIiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU0NzQsImV4cCI6MTYxMjIyMTg3NCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIl19.diEVYM2cmsJx3wbl7c7F-mE5GQOcZJtpyRXEbz436uCcwfQcL1bURjr7NfaufQgafNXczCdE2O5er6UeInwH7YYZ9pJPfwIZ28__j47SYr78xzXxT2i4ffotTZS0vcak_C8-b6uSrMQQRgDFfi9e8kGgjG_LKkoT0DMO-Bn42b65jKA7-Ms8FRt7P9zmMs6blMDJJK9rQfprkigvqS73bi3KJeWMADvLM99u34pYmL2KKDMgOw_DMfP7OHtExFLf43tKkODA5yqljsFvPhQxJdpaNVQE5MvdN3yIFlcZsZmB0VNZhACrUPrcvNh6JpnJrh8N89jJD0kI8weK_A__Wg"
# africhoice
CASTING_ASSISTANT_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAwNTQwZjZiMTNlNTcwMDc2ODZlMDhjIiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3MTEsImV4cCI6MTYxMjIyMjExMSwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIl19.kojd7TQm5YdwpazaA1B7IaMsWDEpKFWazQIaHWdk2zcyPpJc9_wZmkbbHt-vB7t2VMRw5o3a83c9kvXJP0UL99Kf26aBD_Zf6B-58pwr3eYeFgKwlRB-SoSY0tG62vKYbufpPVNZfvX5b5kIPpk2q2YJuphFx1b4GdKO910_HDj7nNsEDvRpqX76H59LeOh7lcSn31nUZGpLNN1OCSbRQS5NdMuR4XhlarKMvVdvdgxi8cxS08kwxvjsGUw-pFSBPf-8U83WPGuouQxowYcE1gIGsGQQ2LMFuWAEvfKtZn1IhcqPuYetnd8pJV9rpFP4LqX5L0OJPL-Cz9UKs1IeEQ"
EXECUTIVE_DIRECTOR_TOKEN = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlFTVkY1OTJ5RS14eGFJcTdLdGJtQyJ9.eyJpc3MiOiJodHRwczovL2Rldi00ZGt4NHVxai51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjAxNjMzZThmZmNiZTIwMDZhODkyMTg1IiwiYXVkIjoiaHR0cHM6Ly9jYXBzdG9uZS8iLCJpYXQiOjE2MTIxMzU3OTAsImV4cCI6MTYxMjIyMjE5MCwiYXpwIjoiZEQzaGlZZ1d3WmhXVnBlb3lQRzlYSENtdVNjRmRkbDciLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbImRlbGV0ZTphY3RvcnMiLCJkZWxldGU6bW92aWVzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyIsInBvc3Q6bW92aWVzIl19.oEjGJXWS8PsygU4rtZQnt_Rkss56fwPHC-1T6ZPorBq_-stkdAuuw_qpQMaXMbpbGYZBTACEX6zoOFvJJie_UFiUB6jNZHWgjQOPgZS149G-FTqusLJQS_fwmYtPwKKOaoGpw8SLNRFUoh4DojLEdCAOqqaJGLDVZ8ZSsCQR4fx9JE8yLnUj0daAzcURscH2H-hRTsD4TyUFJ1qbTlggohKxk9jR3sFcB-UsAUWnTNe5dssQ7V4do3ObnrY8FGe2yI5Y9XU5fC98F7XsE9nOGJwC_qT32eu43zJGgfx0lGvsUKESpiyYQBGyXr1gfCqP5xYGtkbGi6obbhUo_e47PQ"
