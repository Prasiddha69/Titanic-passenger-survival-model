from django.shortcuts import render
import pickle

# Create your views here.
def home(request):
    survived_result=None
    if request.method =='GET':
        return render(request,'home.html')
    else:
        gender=int(request.POST['gender'])
        age=int(request.POST['age'])


        with open(r'/Users/prasiddha/Desktop/Survived/prediction/survived.pkl','rb') as f:
            model=pickle.load(f)

            result=model.predict([[age,gender]])

            if result[0]==0:
                survived_result="Dead"
            else:
                survived_result="Survived"

        return render(request,'home.html',{'result': survived_result})  




  
      
