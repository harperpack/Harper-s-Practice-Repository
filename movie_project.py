import media
import fresh_tomatoes

docstring = media.Movie.__doc__
name = media.Movie.__name__
source = media.Movie.__module__

print ("As part of our Python education, we have built a class called "
	+ name + ", which helped us in our 'Movie Center' project.")
print ("\n" + docstring + "\n")
print ("We imported this Class from a program we built called " + source)

the_matrix = media.Movie("The Matrix", ("A computer hacker learns from" 
	" mysterious rebels about the true nature of his reality and his "
	"role in the war against its controllers."),( 
	"https://en.wikipedia.org/wiki/The_Matrix#/media/File:The_Matrix_"
	"Poster.jpg"), "http://www.youtube.com/watch?v=a94b1yZOBes")
	
inception = media.Movie("Inception", ("A thief, who steals corporate "
	"secrets through the use of dream-sharing technology, is given the "
	"inverse task of planting an idea into the mind of a CEO."), (
	"https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010"
	"%29_theatrical_poster.jpg"), ("https://www.youtube.com/watch?"
	"v=d3A3-zSOBT4"))

paprika = media.Movie("Paprika", ("When a machine that allows "
	"therapists to enter their patients' dreams is stolen, all hell "
	"breaks loose. Only a young female therapist, Paprika, can stop it."), (
	"https://en.wikipedia.org/wiki/Paprika_(2006_film)#/media/File:Papr"
	"ikaposter.jpg"), ("https://www.youtube.com/watch?v=jJzEW_eE1G0"))

furious_7 = media.Movie("Furious 7", ("Deckard Shaw seeks revenge "
	"against Dominic Toretto and his family for his comatose brother."), (
	"https://en.wikipedia.org/wiki/Furious_7#/media/File:Furious_7_post"
	"er.jpg"), ("https://www.youtube.com/watch?v=Skpu5HaVkOc"))

live_free_die_hard = media.Movie("Live Free or Die Hard", ("John McClane"
	" and a young hacker join forces to take down master cyber-terrorist"
	"  Thomas Gabriel in Washington D.C."), ("https://en.wikipedia.org/"
	"wiki/Live_Free_or_Die_Hard#/media/File:Live_Free_or_Die_Hard.jpg"), (
	"https://www.youtube.com/watch?v=8Jz-8UcCiws"))

bourne_ultimatum = media.Movie("The Bourne Ultimatum", ("Jason Bourne "
	"dodges a ruthless CIA official and his agents from a new "
	"assassination program while searching for the origins of his life "
	"as a trained killer."), ("https://en.wikipedia.org/wiki/The_Bourn"
	"e_Ultimatum_(film)#/media/File:The_Bourne_Ultimatum_(2007_film_pos"
	"ter).jpg"), "https://www.youtube.com/watch?v=ZT2ZxjUjSo0")

movies = [the_matrix, inception, paprika, furious_7, live_free_die_hard, bourne_ultimatum]
fresh_tomatoes.open_movies_page(movies)

