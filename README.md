# Personal Blog Platform

This is a fully functional personal blog platform built with Django. It allows users to create, tag, view, and comment on blog posts, save posts to a "read later" list, and upload images as post thumbnails. This project demonstrates key Django features, including ORM for database management, session handling, slugs for clean URLs, and media file handling, providing a robust content management experience.

<br>

## Project overview

<div align="center">
  <img src='https://raw.githubusercontent.com/abdrrahim2002/Personal-Blog/refs/heads/main/project%20images/home.png' alt='home'>

  <br>

  <img src='https://raw.githubusercontent.com/abdrrahim2002/Personal-Blog/refs/heads/main/project%20images/all%20posts.png' alt='all posts'>

  <br>

  <img src='https://raw.githubusercontent.com/abdrrahim2002/Personal-Blog/refs/heads/main/project%20images/detail%20post.png' alt='post detail'>

  <br>

  <img style='align-self:center;' src='https://raw.githubusercontent.com/abdrrahim2002/Personal-Blog/5fbe29452a5ce49e8d5b72553163aefb8a633a9e/project%20images/database%20structure.svg' alt='database'>
  
</div>




## Features

- **Create, edit, update, and delete** blog posts via the admin panel
- **Tagging system** to categorize posts by topic
- **User commenting system** for interacting with blog posts
- **"Read Later" functionality** allowing users to save posts for future reading
- **Image upload** for adding visuals to blog posts
- **Slugs** for clean URLs to improve SEO and user experience
- **Session management** to store and manage users' "Read Later" lists

<br>

## Technologies Used
- Django 4.2
- Python 3.11
- HTML5, CSS3
- SQLite (default Django database)

<br>

## Installation

1. Clone the repository:
   ```
   https://github.com/abdrrahim2002/Personal-Blog.git
   ```

2. Navigate into the project directory:
   ```
   cd Personal-Blog
   ```

3. Create virtual environment:

   ```
   virtualenv venv
   source venv/bin/activate
   ```

4. Install the dependencies:
   ```
   cd my_site
   pip install -r requirements.txt
   ```

5. Run migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```

6. Create a superuser:
   ```
   python manage.py createsuperuser
   ```

7. Run the development server:
   ```
   python manage.py runserver
   ```

8. Access the site in your browser at:
   ```
   http://127.0.0.1t:8000
   ```
9. For creating posts and manage them use the admin panel go to :
   
  ```
  http://127.0.0.1:8000/admin/
  ```

<br>


## Acknowledgements
This project was created by following a comprehensive tutorial from [Maximilian Schwarzmüller](https://github.com/maxschwarzmueller), All credit for the structure and functionality of this project goes to the original author. I implemented the project to deepen my understanding of Django's core features, including ORM, sessions, slugs, and file handling.

**Special Thanks**

A special thanks to Tutorial **Maximilian Schwarzmüller** for creating such an informative and well-structured tutorial. Your guidance has been invaluable in helping me understand Django.

<br>

## Final Thoughts

Thanks for taking the time to explore my project!


