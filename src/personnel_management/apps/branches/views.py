from django.shortcuts import render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Branch
from .forms import BranchCreateForm

# Create your views here.
def branch_list_view(request, *args,**kwargs):
	branch_list = Branch.objects.all()
	page = request.GET.get('page',1)
	paginator = Paginator(branch_list,10)
	try:
		branches = paginator.page(page)
	except PageNotAnInteger:
		branches = paginator.page(1)
	except EmptyPage:
		branches = paginator.page(paginator.num_pages)
	context = {"branches": branches, 
				"total_branch_amount": paginator.count
			  }
	return render(request, "branches/branch_list.html",context)

def branch_create_view(request, *args, **kwargs):
	form = BranchCreateForm(request.POST or None) 

	if request.method == 'POST':
		pass
	return render(request, 'branches/branch_create.html', {"form": form})