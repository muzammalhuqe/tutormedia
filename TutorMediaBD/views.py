from django.shortcuts import render
from tuitions.models import Tution
from tuitions.models import TutionDetails
from tutor.models import TutorAccount
from django.db.models import Sum

def home(request, book_slug = None):

    # data = TutionDetails.objects.all()
    data = TutionDetails.objects.annotate(total_rating_sum=Sum('comments__rating'))
    if book_slug is not None:
        cat = Tution.objects.get(slug = book_slug)
        data = TutionDetails.objects.filter(tuition = cat)
    categories = Tution.objects.all()
    tutor = TutorAccount.objects.all()
    tution_details = TutionDetails.objects.all()
    return render(request, 'home.html', {'data' : data, 'tutor' : tutor, 'categories' : categories,'tution_details': tution_details})