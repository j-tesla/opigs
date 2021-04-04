from django.shortcuts import redirect
from accounts.decorators import admin_required
from accounts.models import Company

# Create your views here.
@login_required
@admin_required
def verify_company(request, pk):
  company = Company.objects.get(id=pk)
  company.verified = True
  company.save()

  return redirect("company")
