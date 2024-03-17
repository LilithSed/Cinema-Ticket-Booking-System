# Cinema Ticket Booking App

## Note
Although in the task description there wasn't a point for docker integration, I decided to use docker-compose to facilitate the setup process.
Due to it you don't need to set up the database, because it will be done automatically after running the docker-compose.

## Installation
Follow the commands below to configure the program:

```bash
docker-compose up --build
```
```bash
docker exec -it web python manage.py createsuperuser
```

## Note
If you face 'permission denied' or other permission related problems while trying to run the Docker, this can come from the 'startup.sh' file.

Just change it's permissions using [chmod] command.

## Usage
1. Run 'http://localhost:8000/' port on the browser.
2. Run 'http://localhost:8000/admin/' for Admin Pannel/Dashboard.

Note: As I am getting the movies dynamically, you have to add movies from the Admin Panel (Movies -> Add Movie). After that you have to add a show for that movie to be able to show it inside the selected room (Shows -> Add Show). Note that the created movie will be shown inside the room that was selected during the movie creation process, not while creating a show.

Note: The Poster can be empty, or you have to provide a real image url taken from the Internet. They must be finished with .jpg/.jpeg or .png formats. (I didn't want to hardcode it.)

--- Example ---
1. Create a Movie

Movie Name: Interstellar  
Poster: https://letsgetoffthisrockalready.files.wordpress.com/2020/05/imax-poster-for-interstellar.jpeg  
Room: Blue

2. Create a Show

Movie: Interstellar  
Start Date: 03/18/2024  
End Date: 03/19/2024  
Ticket Price: 10  
Showtime: 23:00  
Room: Blue  

Note that the format for 'Start Date' and 'End Date' must be M/D/Y.  
Note that 'Start Date' Can't be sooner than the current day.

## Final Tests
Now you can see the movie inside the selected room and book a ticket for it.  
You can create more movies for different days and rooms.

### Important
I know this could have been done better if I had more time, but hope you will like it.

