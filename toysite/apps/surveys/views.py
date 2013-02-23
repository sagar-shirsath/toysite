
from django.shortcuts import redirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from surveys.models import *
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect


@login_required
def list(request):
    """Shows the list of Surveys """
    surveys = Survey.objects.all()

    return render_to_response("surveys/list.html", {'surveys':surveys}, context_instance=RequestContext(request))

@login_required
def add(request):
    """Adding a survey with Questions and Options"""
    dataDisctionary = {}

    questionDict = {}
    if request.method == 'POST':
        postedData = request.POST.copy();
        surveyTitle = postedData['survey_title']
        for key in postedData:
            checkList = key.split(",")

            if len(checkList) == 2:
                if checkList[1] == '*':
                    questionDict.update({int(checkList[0]) : str(postedData[key])})
#                    dataDisctionary.update({int(checkList[0]):[]})

                else:

                    if dataDisctionary.has_key(int(checkList[0])):
                        dataDisctionary[int(checkList[0])].append(str(postedData[key]))
                    else:
                        dataDisctionary.update({int(checkList[0]):[str(postedData[key])]})




        surveyObj = Survey.objects.create(title=surveyTitle,created_by = request.user)




        for questionId in questionDict:
            questionObj = Question.objects.create(title=questionDict[questionId], survey = surveyObj)
            for option in dataDisctionary[questionId]:
                Option.objects.create(title=option,question=questionObj)

        return HttpResponseRedirect(reverse('survey_list'))




    return render_to_response("surveys/add.html", {}, context_instance=RequestContext(request))

@login_required
def summery(request):
    """Shows the Summery of a Survey"""
    return render_to_response("surveys/summery.html", {}, context_instance=RequestContext(request))

@login_required
def submit(request,id):
    """It shows the form to submit the survey's questions answers """
    survey = Survey.objects.get(pk=id)
    return render_to_response("surveys/submit.html", {'survey':survey}, context_instance=RequestContext(request))




