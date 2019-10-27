from django.shortcuts import render

from .models import MovieList
import requests
import json

from .models import MovieList,CreateList


# Create your views here.


def index(request):
    return render(request,'movies/index.html')




def Movie_list(request):
       #MovieList.objects.all().delete()
       #return render(request, 'movies/movie_list.html')

       url="https://api.themoviedb.org/3/movie/top_rated?api_key=079adaddf59d973742379f3728da9a94&language=en-US&page=1"
       movie_text = requests.get(url).text
       #print(movie_text)

       movie_result_dict =json.loads(movie_text) # string to python object

       movie_result =  movie_result_dict["results"]  # storing the list of movies


       for movies in movie_result:
           #print(movies['title'])
           #print(movies['vote_average'])
           #print(movies['overview'])
           #print(movies['release_date'])
           title = movies['title']
           vote_average = movies['vote_average']
           overview = movies['overview']
           release_date = movies['release_date']

           movelist= MovieList(title=title,vote_average= vote_average,overview=overview,release_date=release_date )
           movelist.save()

       movelist_final= MovieList.objects.all()
       return render(request,'movies/movie_list.html',{'movielist_final':movelist_final})

       #return render(request, 'movies/movie_list.html')


def Movie_details(request,pk):
    movielist_final = MovieList.objects.filter(id=pk)
    #print(movielist_final[0].title)

    return render(request, 'movies/movie_details.html', {'movielist_final': movielist_final[0]})




def Create_list(request):
    movielist_final = MovieList.objects.all()

    params={'movielist_final':movielist_final}


    if request.method=="POST":
        list_name= request.POST.get('list_name','')
        movie_list = request.POST.get('created_list', '')

        createlist = CreateList(list_name=list_name, movie_list=movie_list)

        createlist.save()

    return render(request,'movies/create_list.html',params)




def View_movie_list(request):
     movie_name = CreateList.objects.all()
     params={'movie_name':movie_name}
     return render(request,'movies/view_movie_list.html',params)



def View_movie_list_details(request,pk):
    movie_name = CreateList.objects.filter(id=pk)

   # movie_name_list1_dict =movie_name[0].movie_list  # for dictionory  object of createlist

    movie_name_dict = movie_name[0].movie_list
    movie_names = MovieList.objects.all()
    movie_name_dict = json.loads(movie_name_dict)
    movie_name_list=[]

    for item in movie_name_dict:
        movie_name_list.append(movie_name_dict[item])

   # print(movie_name_list)

    if request.method=="POST":

        movie_list = request.POST.get('created_list', '')
        #print(movie_list)
        #.update(movie_list=movie_list)
        #movie_name[0].movie_list= movie_list
        #movie_name[0].save()
        #createlist.save()



        new_add=CreateList.objects.get(id=pk)
        new_add.movie_list=movie_list
        new_add.save(update_fields=['movie_list'])
        #new_add.movie_list=movie_list
        #new_add.save()

    vote_average_value_list=[]
    upper_value=0
    lower_value=0
    for item in movie_name_dict:
          title= movie_name_dict[item]
          #print(title)
          vote_average_value=MovieList.objects.filter(id=item)
          #print(vote_average_value)
          vote_average_value = vote_average_value[0].vote_average
          vote_average_value =float(vote_average_value)
          vote_average_value_list.append(vote_average_value)
          vote_average_value_list.sort()
    length=int(len(vote_average_value_list))
    #print(length)
    upper_value=vote_average_value_list[length-1]
    lower_value = vote_average_value_list[0]
    #print(upper_value)
    #print(lower_value)
    #print(vote_average_value_list)
    recommend_movie_list1=[]
    y=0
    check1 = MovieList.objects.all()
    for item in check1:
        if lower_value <= item.vote_average <= upper_value:
            recommend_movie_list1.append(item.title)
            #new_add.recommend_movie_list = item.title
            y=json.dumps(recommend_movie_list1)
            print(y)
    #new_add.recommend_movie_list = y
    new_add = CreateList.objects.get(id=pk)
    new_add.recommend_movie_list = y
    new_add.save(update_fields=['recommend_movie_list'])
    y=json.loads(y)
    params={'movie_name_list':movie_name_list,'movie_names':movie_names,'movie_name_dict':movie_name_dict,'y':y}

    return render (request,'movies/view_movie_list_details.html',params)