from django.shortcuts import render


def main(request):
  #코드 구현
  print(request.POST)
  return render(request, 'index.html')

