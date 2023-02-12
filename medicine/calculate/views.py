from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm

def main(request):
  return render(request, 'index.html')
def medicine(request):
  if request.method == 'POST':
    form = NameForm(request.POST)
    if form.is_valid():
      return render(request, 'index.html')
  else:
      form = NameForm()
  return render(request, 'index.html', {'form': form})
