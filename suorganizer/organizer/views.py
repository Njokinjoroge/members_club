from django.http.response import HttpResponse
from .models import Tag,Startup
from django.views.generic import View
from django.shortcuts import get_object_or_404,redirect,render
from django.template import Context, loader
from.forms import TagForm,StartUpForm,NewslinkForm


def tag_list(request):
    return render(request,"organizer/tag_list.html",{"tag_list":Tag.objects.all()})



def tag_detail(request,slug):
    tag=get_object_or_404(Tag,slug__iexact=slug)
    template = loader.get_template("organizer/tag_details.html")
    context ={'tag': tag}
    return HttpResponse(template.render(context))


def startup_list(request):
    return render(request,"organizer/startup_list.html",{'startup_list':Startup.objects.all()})

def startup_details(request,slug):
    startup=get_object_or_404(Startup,slug__iexact=slug)
    return render(request,"organizer/startup_detail.html",{'startup':startup})
    

# def tag_create(request):
#     if request.method == 'POST':
#         form=TagForm(request.POST)
#         if form.is_valid():
#             new_tag=form.save()
#             return redirect(new_tag)
        
#     else:
#         form =TagForm()
#         return render(request,"organizer/tag_form.html",{'form':form})



class ObjectCreateMixing:
    form_class=None
    template_name=''

    def get(self,request):
        return render(request,self.template_name,
                      {'form':self.form_class()})
    def post(self,request):
        form=self.form_class(request.POST)
        if form.is_valid():
            new_object=form.save()
            return redirect(new_object)
        else:
            return render(request,self.template_name,{'form':form})
class TagCreate(ObjectCreateMixing,View):
    form_class=TagForm
    template_name='organizer/tag_form.html'
  
        
class StartUpCreate(ObjectCreateMixing,View):
    form_class=StartUpForm
    template_name='organizer/startup_form.html'    
    


class CreateNewsLink(ObjectCreateMixing,view):
    form_class = NewslinkForm
    template_name = 'organizer/newslink_form'

# class CreateNewsLink(ObjectCreateMixing,View):
#     form_class= NewslinkForm
#     template_name='organizer/newslink_form'
        


# class CreateNewsLink(View):
#     form_class = NewslinkForm
#     template_name='organizer/newslink_form'
#     def get(self,request):
#         return render(request,self.template_name,{'form':self.form_class()})
#     def post(self,request):
#         form= self.form_class(request.POST)
#         if form.is_valid():
#             new_newslink=form.save()
#             return redirect(new_newslink)
#         else:
#             return render(request,self.form_class,{'form':form})