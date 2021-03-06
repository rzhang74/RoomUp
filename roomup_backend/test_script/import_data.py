from app_basic.models import *

user1 = User(username="user1",first_name="q",last_name="b",email="qb",password="qb")
user2 = User(username="user2",first_name="q",last_name="b",email="qb",password="qb")
user3 = User(username="user3",first_name="q",last_name="b",email="qb",password="qb")
user4 = User(username="user4",first_name="q",last_name="b",email="qb",password="qb")
user5 = User(username="user5",first_name="q",last_name="b",email="qb",password="qb")

user1.save()
user2.save()
user3.save()
user4.save()
user5.save()
# User.objects.all().delete()

advance1 = AdvancedUser(uid=user1)
advance2 = AdvancedUser(uid=user2)
advance3 = AdvancedUser(uid=user3)
advance4 = AdvancedUser(uid=user4)
advance5 = AdvancedUser(uid=user5)

advance1.save()
advance2.save()
advance3.save()
advance4.save()
advance5.save()
# AdvancedUser.objects.all().delete()

apt1 = Apartment(name="Campus Circle", price=635, address="1010 W Univeristy Ave", floorplan="4B4B", occupied=True)
apt2 = Apartment(name="IT", price=650, address="409 E Chalmers St", floorplan="4B1B", occupied=False)

apt1.save()
apt2.save()
# Apartment.objects.all().delete()

group1 = Group(gid=1, group_name="group1", aid=apt1, peopleleft=4, admin_uid=advance1, capacity=4) #134
group2 = Group(gid=2, group_name="group2", aid=apt2, peopleleft=4, admin_uid=advance2, capacity=4) #25

group1.save()
group2.save()
# Group.objects.all().delete()

advance1.gid = group1
advance3.gid = group1
advance4.gid = group1
advance2.gid = group2
advance5.gid = group2

advance1.save()
advance2.save()
advance3.save()
advance4.save()
advance5.save()

pm1 = PotentialMatch(uid=advance1, gid=group2)
pm2 = PotentialMatch(uid=advance2, gid=group1)
pm3 = PotentialMatch(uid=advance5, gid=group1)
pm4 = PotentialMatch(uid=advance3, gid=group2)

pm1.save()
pm2.save()
pm3.save()
pm4.save()
