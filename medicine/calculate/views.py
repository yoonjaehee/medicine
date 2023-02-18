from django.shortcuts import render
from django.http import HttpResponseRedirect
import pandas as pd
def main(request):
  return render(request, 'index.html')

def find(ins):
  data4 = (df[df['처방명'] == ins])  ## 이름 맞는거 데이터 프레임 찾아버림 + 데이터프레임화
  data5 = (df[df['별명'] == ins])  ## 별명 맞는거 데이터 프레임 찾아버림 + 데이터프레임화
  if (data5.empty):  ## 별명에만 있을때 이름에만 있을때 구분
    if (data4.empty):
      ##없음
      return 0
    data6 = data4
  else:
    data6 = data5
  if ((data6['구성'].iloc[-1])[-1].isdigit()):  ## 맨끝이 숫자일때는
    result = data6['구성'].str.split('/').tolist()
    for i in result:
      for t in i:
        rep = t.split(':')[0]  ## 갯수전까지
        rep2 = t.split(':')[1]  ## 갯수
        confirm = res.get(rep)
        if (confirm != None):
          if (float(res[rep]) >= float(rep2)):
            continue
          else:
            res[rep] = rep2
        else:
          res[rep] = rep2
  else:
    result = data6['구성'].str.split('+').tolist()
    for i in result:
      for t in i:
        find(t)
def show():
  tex = ""
  total = 0
  res1 = dict(sorted(res.items()))
  print(res1)
  for i in res1:
    tex += i + ':' + res1[i] + '\n'
    total += float(res1[i])
  ##label['text'] = tex
  ##label2['text'] = total
def fid(value):
  data4 = (df[df['처방명'] == value]) ## 이름 맞는거 데이터 프레임 찾아버림 + 데이터프레임화
  data5 = (df[df['별명'] == value])  ## 별명 맞는거 데이터 프레임 찾아버림 + 데이터프레임화
  if (data5.empty):  ## 별명에만 있을때 이름에만 있을때 구분
    if (data4.empty):
      ## 없음 띄우기
      return 0
    data6 = data4
  else:
    data6 = data5
  if ((data6['구성'].iloc[-1])[-1].isdigit()):  ## 찾은 데이터의 끝까지
    result = data6['구성'].str.split('/').tolist()  ## 찾은데이터의 문자열끝까지
    for i in result:
      for t in i:
        rep = t.split(':')[0]  ## 갯수전까지
        rep2 = t.split(':')[1]  ## 갯수
        confirm = res.get(rep)
        if (confirm != None):
          if (float(res[rep]) >= float(rep2)):
            continue
          else:
            res[rep] = rep2
        else:
          res[rep] = rep2
  else:
    result = data6['구성'].str.split('+').tolist()
    for i in result:
      for t in i:
        find(t)
  show()

def medicine(request):
  if request.method == 'POST':
    ins = request.POST['medicine_name']
    data = pd.read_csv("./medicine.csv")  ## csv 에서 부름
    global df
    df = pd.DataFrame(data)  ## dataframe 만듦
    global res
    res={}
    fid(ins)


  return render(request, 'index.html')
##def print(request):


