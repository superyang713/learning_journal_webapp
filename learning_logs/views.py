from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from learning_logs.models import Topic, Entry
from learning_logs.forms import TopicForm, EntryForm


def index(request):
    return render(request, 'index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('date_added')
    context = {
        'topic': topic,
        'entries': entries,
    }
    return render(request, 'topic.html', context)


def new_topic(request):
    if request.method != 'POST':
        form = TopicForm()
        context = {'form': form}
        return render(request, 'new_topic.html', context)
    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))


def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST':
        form = EntryForm()
        context = {'form': form, 'topic': topic}
        return render(request, 'new_entry.html', context)
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic', args=[topic_id]))


def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        form = EntryForm(instance=entry)
        context = {'form': form, 'topic': topic, 'entry': entry}
        return render(request, 'edit_entry.html', context)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic', args=[topic.id]))
