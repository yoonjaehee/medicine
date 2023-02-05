from django.shortcuts import render


def main(request):
  #코드 구현
  return render(request, "index.html")