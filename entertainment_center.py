import fresh_tomatoes
import media

#Toy story movie: movie title,storyline,poster image and movie trailer
toy_story = media.Movie(
    "Toy Story", 
    "A story of boy and his toys came to life",
    "https://gfx.videobuster.de/archive/v/c-MvmFJ6r-BNo00ZPIHKOTwcz0lMkawrSUyRjAyJTJGaW1hmSUyRmpwZWclMkZiZjVhNGJjv7bDZN7psTFjYzBj7jBm9jUuanBnJnI9d-84/toy-story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc"
    )

#Avatar movie: movie title,storyline,poster image and movie trailer
avatar = media.Movie(
    "Avatar", 
    "A marine on a alien planet",
    "https://i.pinimg.com/originals/4c/f4/c8/4cf4c8b33be9fae687267067cac3e77c.jpg",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY"
    )

#Deadpool 3 movie: movie title,storyline,poster image and movie trailer
deadpool_3 = media.Movie(
    "Deadpool 3", 
    "Crime's the disease, meet the cure. Okay,Hi, Tom!",
    "https://vignette1.wikia.nocookie.net/xmenmovies/images/f/f0/Deadpool_poster_3.jpg/revision/latest?cb=20160115013939",
    "https://www.youtube.com/watch?v=JBn4x_yrKmo"
    )

#Hulk movie: movie title,storyline,poster image and movie trailer
hulk = media.Movie(
    "Hulk", 
    "Hulk is a 2003 American superhero film based on the fictional Marvel Comics character of the same name",
    "https://i.pinimg.com/originals/bd/cc/1c/bdcc1c51828b8f9d9c12212b98257d56.jpg",
     "https://www.youtube.com/watch?v=xbqNb2PFKKA"
     )

#Wonder Women movie: movie title,storyline,poster image and movie trailer
wonder_women = media.Movie(
    "Wonder Women", 
    "Fighting alongside men in a war to end all wars, she finally discovers her full powers and true destiny",
    "https://cdn.traileraddict.com/content/warner-bros-pictures/wonder-woman-2017-5.jpg", 
    "https://www.youtube.com/watch?v=VSB4wGIdDwo"
    )

#Iron man movie: movie title,storyline,poster image and movie trailer
iron_man = media.Movie(
    "Iron Man",
    "Iron Man, a billionaire industrialist and genius inventor who is kidnapped and forced to build a devastating weapon",
    "http://is4.mzstatic.com/image/thumb/Video2/v4/ae/89/ce/ae89cecd-2f72-6750-fcae-4e9d78e4314a/source/1200x630bb.jpg",
    "https://www.youtube.com/watch?v=8hYlB38asDY"
    )

#Set the movie that will be passed to the media file
movies = [
    toy_story, 
    avatar, 
    deadpool_3, 
    hulk, 
    wonder_women, 
    iron_man
    ]

#Open the HTML file in a webbrowser via the fresh_tomatoes.py file
fresh_tomatoes.open_movies_page(movies)
