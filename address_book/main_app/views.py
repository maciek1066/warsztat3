from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import View

from main_app.models import Person, Address, Phone, Email, Group


class ShowPeople(View):
    def get(self, request):
        people = Person.objects.all().order_by("last_name")
        return render(request, "list_of_people.html", {"people": people})


class ModifyPerson(View):
    def get(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        return render(request, "modify_person.html", {"person": person})

    def post(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)

        if "first_name" in request.POST:
            person.first_name = request.POST["first_name"]
        if "last_name" in request.POST:
            person.last_name = request.POST["last_name"]
        if "description" in request.POST:
            person.description = request.POST["description"]

        person.save()

        return render(request, "modify_person.html", {"person": person})


class DeletePerson(View):
    def get(self, request, person_id):
        person = Person.objects.get(id=person_id)
        person.delete()
        return HttpResponseRedirect('/')


class ShowPersonDetails(View):
    def get(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        return render(request, "person_details.html", {"person": person})


class NewPerson(View):
    def get(self, request):
        return render(request, "new_person.html", {})

    def post(self, request):

        if "first_name" in request.POST:
            first_name = request.POST["first_name"]
        if "last_name" in request.POST:
            last_name = request.POST["last_name"]
        if "description" in request.POST:
            description = request.POST["description"]

        Person.objects.create(first_name=first_name, last_name=last_name, description=description)
        person = Person.objects.get(first_name=first_name, last_name=last_name, description=description)
        person_id = person.id

        return HttpResponseRedirect('/show/{}'.format(person_id))


class AddAddress(View):
    def get(self, request, person_id):
        return render(request, "new_address.html", {})

    def post(self, request, person_id):

        if "city" in request.POST:
            city = request.POST["city"]
        if "street" in request.POST:
            street = request.POST["street"]
        if "house_number" in request.POST:
            house_number = request.POST["house_number"]
        if "apartment_number" in request.POST:
            apartment_number = request.POST["apartment_number"]

        Address.objects.create(city=city, street=street, house_number=house_number, apartment_number=apartment_number,
                               person_id=person_id)

        return HttpResponseRedirect('/show/{}'.format(person_id))


class ModifyAddress(View):
    def get(self, request, person_id, address_id):
        person = get_object_or_404(Person, id=person_id)
        address = person.address_set.get(id=address_id)
        return render(request, "modify_address.html", {"person": person, "address": address})

    def post(self, request, person_id, address_id):
        person = get_object_or_404(Person, id=person_id)
        address = person.address_set.get(id=address_id)

        if "city" in request.POST:
            address.city = request.POST["city"]
        if "street" in request.POST:
            address.street = request.POST["street"]
        if "house_number" in request.POST:
            address.house_number = request.POST["house_number"]
        if "apartment_number" in request.POST:
            address.apartment_number = request.POST["apartment_number"]

        address.save()

        return HttpResponseRedirect('/show/{}'.format(person_id))


class DeleteAddress(View):
    def get(self, request, person_id, address_id):
        person = get_object_or_404(Person, id=person_id)
        address = person.address_set.get(id=address_id)
        address.delete()
        return HttpResponseRedirect('/show/{}'.format(person_id))


class AddPhone(View):
    def get(self, request, person_id):
        return render(request, "new_phone.html", {})

    def post(self, request, person_id):

        if "number" in request.POST:
            number = request.POST["number"]
        if "number_type" in request.POST:
            number_type = request.POST["number_type"]

        Phone.objects.create(number=number, number_type=number_type, person_id=person_id)

        return HttpResponseRedirect('/show/{}'.format(person_id))


class ModifyPhone(View):
    def get(self, request, person_id, phone_id):
        person = get_object_or_404(Person, id=person_id)
        phone = person.phone_set.get(id=phone_id)
        return render(request, "modify_phone.html", {"person": person, "phone": phone})

    def post(self, request, person_id, phone_id):
        person = get_object_or_404(Person, id=person_id)
        phone = person.phone_set.get(id=phone_id)

        if "number" in request.POST:
            phone.number = request.POST["number"]
        if "number_type" in request.POST:
            phone.number_type = request.POST["number_type"]

        phone.save()

        return HttpResponseRedirect('/show/{}'.format(person_id))


class DeletePhone(View):
    def get(self, request, person_id, phone_id):
        person = get_object_or_404(Person, id=person_id)
        phone = person.phone_set.get(id=phone_id)
        phone.delete()
        return HttpResponseRedirect('/show/{}'.format(person_id))


class AddEmail(View):
    def get(self, request, person_id):
        return render(request, "new_email.html", {})

    def post(self, request, person_id):

        if "address" in request.POST:
            address = request.POST["address"]
        if "address_type" in request.POST:
            address_type = request.POST["address_type"]

        Email.objects.create(address=address, address_type=address_type, person_id=person_id)

        return HttpResponseRedirect('/show/{}'.format(person_id))


class ModifyEmail(View):
    def get(self, request, person_id, email_id):
        person = get_object_or_404(Person, id=person_id)
        email = person.email_set.get(id=email_id)
        return render(request, "modify_email.html", {"person": person, "email": email})

    def post(self, request, person_id, email_id):
        person = get_object_or_404(Person, id=person_id)
        email = person.email_set.get(id=email_id)

        if "address" in request.POST:
            email.address = request.POST["address"]
        if "address_type" in request.POST:
            email.address_type = request.POST["address_type"]

        email.save()

        return HttpResponseRedirect('/show/{}'.format(person_id))


class DeleteEmail(View):
    def get(self, request, person_id, email_id):
        person = get_object_or_404(Person, id=person_id)
        email = person.email_set.get(id=email_id)
        email.delete()
        return HttpResponseRedirect('/show/{}'.format(person_id))


class ShowGroup(View):
    def get(self, request):
        group = Group.objects.all().order_by("name")
        return render(request, "group_list.html", {"group": group})


class ShowGroupDetails(View):
    def get(self, request, group_id):
        group = get_object_or_404(Group, id=group_id)
        people = group.person.all()
        return render(request, "group_details.html", {"group": group, "people": people})


class NewGroup(View):
    def get(self, request):
        return render(request, "new_group.html", {})

    def post(self, request):

        if "name" in request.POST:
            name = request.POST["name"]

        Group.objects.create(name=name)

        return HttpResponseRedirect('/group/')


class DeleteGroup(View):
    def get(self, request, group_id):
        group = Group.objects.get(id=group_id)
        group.delete()
        return HttpResponseRedirect('/')


class GroupSearch(View):
    def get(self, request):
        people = Person.objects.all()
        people_lst = []
        if request.GET.get("first_name"):
            people_lst = people.filter(first_name__contains=request.GET["first_name"])
        if request.GET.get("last_name"):
            people_lst = people.filter(last_name__contains=request.GET["last_name"])

        return render(request, "search_person.html", {"people": people, "filters": request.GET, "people_lst": people_lst})


class AddToGroup(View):
    def get(self, request, person_id):
        groups = Group.objects.all()
        return render(request, 'add_to_group.html', {'groups': groups})

    def post(self, request, person_id):
        person = get_object_or_404(Person, id=person_id)
        group = Group.objects.get(name=request.POST['name'])
        group.person.add(person)
        group.save()

        return HttpResponseRedirect('/')


class RemoveFromGroup(View):
    def get(self, request, person_id, group_id):
        person = get_object_or_404(Person, id=person_id)
        group = get_object_or_404(Group, id=group_id)
        group.person.remove(person)
        return HttpResponseRedirect('/')
