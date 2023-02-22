from django.shortcuts import render, redirect
from django.views import View

from .forms import QuestboardForm, AddQuestForm, DibsQuestForm
from .models import Questboard, Quest


class HomeView(View):
    def get(self, request):
        questboards = Questboard.objects.all().order_by('id')
        questboardform = QuestboardForm()
        return render(
            request, 'questboard/home.html',
            {'questboards': questboards,
             'questboardform': questboardform}
        )

    def post(self, request):
        questboardform = QuestboardForm(
            request.POST
        )

        if questboardform.is_valid():
            questboard = questboardform.save()
            questboards = Questboard.objects.all()
            return redirect('questboard_detail', pk=questboard.pk)


class QuestboardDetailView(View):
    quest_pk = ''

    def get(self, request, pk):
        questboard = Questboard.objects.get(id=pk)
        questform = DibsQuestForm()
        return render(
            request, 'questboard/questboard_detail.html',
            {'questboard': questboard, 'questform': questform}
        )

    def post(self, request, pk):
        if 'update_questboard' in request.POST:
            questboardform = QuestboardForm(
                request.POST,
                instance=Questboard.objects.get(id=pk)
            )
            if questboardform.is_valid():
                questboard = questboardform.save()

        if 'add_quest' in request.POST:
            questform = AddQuestForm(
                request.POST
            )
            if questform.is_valid():
                quest = questform.save(commit=False)
                quest.questboard_id = pk
                quest.save()

        if 'dibs_quest' in request.POST:
            quest_pk = request.POST.get('dibs_quest')
            instance = Quest.objects.get(id=quest_pk)
            questform = DibsQuestForm(
                request.POST,
                instance
            )
            if questform.is_valid():
                quest = questform.save(commit=False)
                quest.id = quest_pk
                if quest.student_1 is not None:
                    quest.save(update_fields=[
                        'student_1'
                    ])
                if quest.student_2 is not None:
                    quest.save(update_fields=[
                        'student_2'
                    ])
                if quest.student_3 is not None:
                    quest.save(update_fields=[
                        'student_3'
                    ])

        if 'update_quest' in request.POST:
            quest_pk = QuestboardDetailView.quest_pk
            questform = AddQuestForm(
                request.POST,
                instance=Quest.objects.get(id=quest_pk)
            )
            if questform.is_valid():
                quest = questform.save(commit=False)
                quest.id = quest_pk
                quest.save()

        return redirect('questboard_detail', pk=pk)


def edit_questboard(request, pk):
    questboard = Questboard.objects.get(id=pk)
    questboardform = QuestboardForm(instance=questboard)
    return render(
        request, 'questboard/edit_questboard.html',
        {'questboardform': questboardform}
    )


def add_quest(request, pk):
    questform = AddQuestForm()
    return render(
        request, 'questboard/add_quest.html',
        {'questform': questform}
    )


def edit_quest(request, pk):
    quest = Quest.objects.get(id=pk)
    questform = AddQuestForm(instance=quest)
    QuestboardDetailView.quest_pk = pk
    return render(
        request, 'questboard/edit_quest.html',
        {'questform': questform}
    )
