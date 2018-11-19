from django.shortcuts import render
from .models import Lore
from django.shortcuts import redirect, render, get_object_or_404
from .forms import LoreForm
from django.db.models import Q



# Create your views here.

#Exibição de dados
def lore_list(request):
	lores = Lore.objects.filter()
	return render(request, 'wikaldeiraapp/lore_list.html', {'lores': lores})

def lore_detail(request, pk):
	lore = get_object_or_404(Lore, pk=pk)
	return render(request, 'wikaldeiraapp/lore_detail.html', {'lore': lore})

#Edição de dados
def lore_edit(request, pk):
	lore = get_object_or_404(Lore, pk=pk)
	if request.method == "POST":
		form = LoreForm(request.POST, request.FILES, instance=lore)
		if form.is_valid():
			lore = form.save(commit=False)
			lore.save()
			return redirect('lore_detail', pk=lore.pk)
	else:
		form = LoreForm(instance=lore)
	return render(request, 'wikaldeiraapp/lore_edit.html', {'form': form})

def lore_new(request):
	if request.method == "POST":
		form = LoreForm(request.POST, request.FILES)
		if form.is_valid():
			lore = form.save(commit=False)
			lore.save()
			return redirect('lore_detail', pk=lore.pk)
	else:
		form = LoreForm()
	return render(request, 'wikaldeiraapp/lore_edit.html', {'form': form})

def lore_delete(request, pk, template_name='wikaldeiraapp/lore_confirm_delete.html'):
	lore = get_object_or_404(Lore, pk=pk)
	if request.method == 'POST':
		lore.delete()
		return redirect('lore_list')
	return render(request, template_name, {'object': lore})

def lore_search(request):
    if request.method == 'GET':
        query = request.GET.get('search_box', None)
        if query:
            lores = Lore.objects.filter( Q(title__icontains=query) | Q(text__icontains=query))
        else:
            lores = Lore.objects.filter()
        return render(request, 'wikaldeiraapp/lore_list.html', {'lores': lores})






