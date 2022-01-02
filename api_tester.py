from hospital.models import customUser

for p in customUser.objects.raw('SELECT * FROM hospital_customUser'):
    print(p)