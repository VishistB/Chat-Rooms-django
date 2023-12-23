from django.shortcuts import render
from .models import Room,Message
from nltk import word_tokenize, pos_tag

def LangFosFunc(sentence):
    words = word_tokenize(sentence)
    pos_tags = pos_tag(words)

    adjectives = [word for word, tag in pos_tags if tag.startswith('JJ')]
    adverbs = [word for word, tag in pos_tags if tag.startswith('RB')]
    conjunctions = [word for word, tag in pos_tags if tag == 'CC']
    determiners = [word for word, tag in pos_tags if tag == 'DT']
    nouns = [word for word, tag in pos_tags if tag.startswith('NN')]
    numbers = [word for word, tag in pos_tags if tag == 'CD']
    prepositions = [word for word, tag in pos_tags if tag == 'IN']
    pronouns = [word for word, tag in pos_tags if tag.startswith('PR')]
    verbs = [word for word, tag in pos_tags if tag.startswith('VB')]

    result = {
        "Adjectives": adjectives,
        "Adverbs": adverbs,
        "Conjunctions": conjunctions,
        "Determiners": determiners,
        "Nouns": nouns,
        "Numbers": numbers,
        "Prepositions": prepositions,
        "Pronouns": pronouns,
        "Verbs": verbs
    }

    return result



# Create your views here.
def rooms(request):
    rooms=Room.objects.all()
    context={"rooms":rooms}
    return render(request,"rooms.html",context)

def room(request,slug):
    room_name=Room.objects.get(slug=slug).name
    messages=Message.objects.filter(room=Room.objects.get(slug=slug))
    context={"slug":slug,"room_name":room_name,'messages':messages}

    
    return render(request,"room.html",context)



