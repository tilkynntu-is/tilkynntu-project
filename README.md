# tilkynntu.is

![Taekniskolinn](https://img.shields.io/badge/Taekniskolinn-blue?style=for-the-badge&logo=https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQqTwAaMeKxCyPqZWQFVSrB3ifYAiyyDOn1HQ&s&logoColor=white)

![GitHub stars](https://img.shields.io/github/stars/tilkynntu-is/tilkynntu-project?style=social)
![GitHub forks](https://img.shields.io/github/forks/tilkynntu-is/tilkynntu-project?style=social)
![Viewers](https://img.shields.io/badge/viewers-0-%23000000?style=flat-square&logo=GitHub&logoColor=white)
![GitHub contributors](https://img.shields.io/github/contributors/tilkynntu-is/tilkynntu-project)
![License](https://img.shields.io/github/license/tilkynntu-is/tilkynntu-project)

![Python](https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white)
![HTML](https://img.shields.io/badge/HTML-5-orange?logo=html5&logoColor=white)
![CSS](https://img.shields.io/badge/CSS-3-blue?logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-ES6-yellow?logo=javascript&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4B8BBE?style=flat-square&logo=PostgreSQL&logoColor=white)
![Django](https://img.shields.io/badge/Django-3.2%2B-green?style=flat&logo=django&logoColor=white)


### Íslenska:

**tilkynntu.is** er sérhæfð vefsíða fyrir skráningu á staðbundnum vandamálum og áhyggjum í þínu samfélagi. Hvort sem um er að ræða lítil vandamál, eins og brotin götuljós, eða alvarlegri áhyggjur sem hafa áhrif á öryggi í hverfinu, veitir **tilkynntu.is** íbúum möguleika á að koma áhyggjum sínum á framfæri og stuðla að jákvæðum breytingum. Vefsvæðið okkar er notendavænt og gerir notendum kleift að skrá tilkynningar, bæta við myndum og fylgjast með stöðu hvers máls á auðveldan hátt. Með því að vinna saman getum við byggt upp sterkara og árangursríkara samfélag, þar sem hverju vandamáli er veitt athygli og leitað lausna. Við bjóðum þig velkominn til að taka þátt í því að gera þitt hverfi að betri stað til að búa.


### English:

**tilkynntu.is** is a dedicated platform for reporting local problems and concerns in your community. Whether it’s minor issues like broken streetlights or more serious concerns affecting neighborhood safety, **tilkynntu.is* empowers residents to voice their concerns and contribute to positive change. Our website is user-friendly, allowing users to easily submit reports, attach photos, and track the status of each issue. By working together, we can build a stronger and more effective community where every problem is acknowledged and solutions are sought. We invite you to join us in making your neighborhood a better place to live.



> [!NOTE]
> This project is developed and designed by students in Tækniskólinn Iceland. This website is for educational purposes only.


### User Stories:
_As a Resident, I want to be able to report local issues quickly so they can be resolved by the city.
This allows residents to contribute to the upkeep and safety of their community, promoting a sense of involvement._

### User Scenarios:
_**Who:** A resident sees a large pothole on a busy road.
**What:** They open the tilkynntu.is app, go to "Report an Issue," select "Road Issue," upload a photo, tag the location, and submit the report with a short description.
**Why:** They want the city to address the hazard quickly to improve road safety for all residents._


## Hlutverk / Roles:

+ **Frontend Developers**
  - Developed by: @tryggvi321, @Ingthor06
  
    - 👷‍♂️ HTML: The structure of the web pages, defining the content and layout.
    - 🎨 CSS: The styling of the web pages, ensuring a responsive and visually appealing user interface.
    - 📝 JavaScript: The dynamic elements of the web application, enhancing user interactions and functionality.

+ **Backend Developers**
  - Developed by: @hinrikfp, @Ingthor06 
 
    - 🐍 Python: The primary programming language used for server-side logic.
    - 📗 Django: A micro web framework that simplifies the development of web applications.
    - 🐘 PostgreSQL Databases: Used for data storage, management, and retrieval.


## WireFlows:
![wireframe](https://github.com/user-attachments/assets/195fdf20-d5fb-4a4d-8d84-c1ba9d250ef8)




## Slóð / Path:
```py
tilkynntu.is/
├── .gitignore                # Specifies files and directories to ignore in version control
├── LICENSE                   # License for your project
├── README.md                 # Documentation and instructions for your project
├── backend/                  # Directory for the backend code
│   ├── manage.py             # Command-line utility for managing the Django project
│   ├── requirements.txt      # List of dependencies for the backend
│   ├── myproject/            # Main Django project package
│   │   ├── __init__.py       # Marks the directory as a package
│   │   ├── settings.py       # Django settings file
│   │   ├── urls.py           # URL configurations for the project
│   │   ├── wsgi.py           # WSGI entry point for deployment
│   │   └── asgi.py           # ASGI entry point for deployment
│   └── migrations/           # Directory for database migrations
│        └── __init__.py      # Marks the migrations directory as a package
└── frontend/                 # Directory for the frontend code
    ├── static/               # Static files (CSS, JS, images)
    │   ├── css/              # CSS files
    │   │   └── styles.css     # Main stylesheet
    │   ├── js/               # JavaScript files
    │   │   └── scripts.js      # Main script
    │   └── images/           # Directory for images
    └── templates/            # HTML templates
        ├── index.html        # Main landing page
        └── layout.html       # Base layout for other templates
```

### Step By Step Setup: 

1. Open Git Bash or Command Prompt
     + Launch Git Bash on your computer.

2. Navigate to Your Desired Directory
```
$ cd path\to\your\directory
```

3. Clone the Repository
```
$ git clone https://github.com/tilkynntu-is/tilkynntu.is-repo.git
```

4. Change Directory into the Cloned Repository
```
$ cd tilkynntu.is-repo\
```

5. Pull the Latest Changes
```
$ git pull
```

> [!IMPORTANT]
> This command should be executed by moderators only, as it establishes the directory path structure for our website.
