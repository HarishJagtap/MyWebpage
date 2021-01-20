## Setup Python Virtual Environment
`python -m virtualenv . -p python3`<br>
`start Scripts\activate`<br>
`pip install -r requirements.txt` <br><br>

## Setup Django and start Server
Enter these commands from the Virtual Environment<br><br>
`cd mywebsite` <br>
`set SECRET_KEY="---Your Secret Key Here---"` <br>
`python manage.py collectstatic` <br>
`python manage.py makemigrations` <br>
`python manage.py migrate --run-syncdb` <br>
`python manage.py createsuperuser` <br>
`python manage.py runserver` <br><br>

## Setup Webpage and customize
Go to admin page ("127.0.0.1:8000/admin/") and add "Item" (Title=Home, link=home) <br>
The webpage requires "Home" item as bare minimum to run. <br>

To add Social profile links, go to admin page and add "Detail". <br>
To add Subpages, go to admin page and add "Item". <br>
To add Posts in any Subpage, go to admin page and add "Post". <br>
This creates your custom webpage. <br>

Now, you can continue to add posts and modify the webpage without getting into html/css. <br>
`Note: The body of the posts support html, and require html tags like <br> for newline, etc.` <br>

The webpage is mobile-responsive. <br>
I have only created the Django part of this project, the html/css were taken from a template. <br><br>


![alt text](sample/sample.png)
![alt text](sample/sample_edited.png)
