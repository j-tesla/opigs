from django.shortcuts import render, redirect
from accounts.models import User
from django.contrib.auth.decorators import login_required
from accounts.decorators import student_required, alumni_required
from .models import Feedback

# Create your views here.

@login_required
def get_feedback(request, pk):
    user = User.objects.get(id=pk)
    feedbacks = user.company.feedback_set.all()
    context = {'feedbacks': feedbacks}
    return render(request, 'feedback.html', context=context)

@login_required
@alumni_required
def give_feedback(request, pk):
    if request.method == "POST":
        company = User.objects.get(id=pk).company
        alumni = User.objects.get(id=request.user.id).alumni
        feedback = Feedback(company=company, alumnus=alumni, content=request.POST['feedback_content'])
        feedback.save()

        return redirect(f"/feedbacks/{pk}/")

    return redirect(f'/accounts/profile/{pk}')
    

