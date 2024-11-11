[![Typing SVG](https://readme-typing-svg.demolab.com?font=Kode+Mono&size=50&duration=2500&pause=1000&width=435&lines=tilkynntu.is)](https://git.io/typing-svg)



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
    - ⚖️ HTMX: A JavaScript library designed to be an extension of html for creating reactive websites
    - 💨 Tailwind: A css utility class collection for writing css in your html files.

+ **Backend Developers**
  - Developed by: @hinrikfp, @Ingthor06 
 
    - 🐍 Python: The primary programming language used for server-side logic. We picked python because all of us know it and its easy to work with.
    - 📗 Django: A powerful python web framework for creating web apps. We picked Django because of it's many features and to learn something new.
    - 🐘 PostgreSQL Databases: Used for data storage, management, and retrieval.

## Database:
### Tables:

**users**
| Column Name    | Description                                                       |
|----------------|-------------------------------------------------------------------|
| id             | Auto-incrementing unique ID for each user                         |
| username       | Username for the user                                             |
| email          | Email address of the user                                         |
| password       | Hashed password for security                                      |
| first_name     | User's first name                                                 |
| last_name      | User's last name                                                  |
| date_joined    | The date the user joined                                          |

**reports**
| Column Name    | Description                                                       |
|----------------|-------------------------------------------------------------------|
| id             | Auto-incrementing unique ID for each report                       |
| user_id        | Reference to the `users` table (user who reported the issue)     |
| location       | Location of the problem (e.g., address, area)                     |
| description    | Detailed description of the problem                               |
| created_at     | When the report was created                                       |

**images**
| Column Name    | Description                                                       |
|----------------|-------------------------------------------------------------------|
| id             | Auto-incrementing unique ID for each image                        |
| report_id      | Reference to the `reports` table (the report this image is attached to) |
| image_url      | URL or path to the image file                                     |
| uploaded_at    | When the image was uploaded                                       |

**comments**
| Column Name    | Description                                                       |
|----------------|-------------------------------------------------------------------|
| id             | Auto-incrementing unique ID for each comment                      |
| user_id        | Reference to the `users` table (user who made the comment)        |
| report_id      | Reference to the `reports` table (the report this comment is attached to) |
| comment        | Content of the comment                                            |
| created_at     | When the comment was created                                      |

**likes_dislikes**
| Column Name    | Description                                                       |
|----------------|-------------------------------------------------------------------|
| id             | Auto-incrementing unique ID                                        |
| user_id        | Reference to the `users` table (the user who liked/disliked)     |
| report_id      | Reference to the `reports` table (the report being liked or disliked) |
| type           | Either 'like' or 'dislike'                                        |
| created_at     | When the like/dislike was made                                    |




## WireFlows:
![wireframe](https://github.com/user-attachments/assets/195fdf20-d5fb-4a4d-8d84-c1ba9d250ef8)




## Slóð / Path:
```py
tilkynntu.is-repo/
├── .gitignore                
├── LICENSE                   
├── README.md                 
├── backend/                  
│   ├── manage.py             
│   ├── requirements.txt
│   ├── migrations/
│   ├── api/
│   └── tilkynntu_is/            
│       ├── __init__.py       
│       ├── settings.py       
│       ├── urls.py           
│       ├── wsgi.py           
│       └── asgi.py           
│    
└── frontend/                 
    ├── static/               
    │   ├── css/              
    │   │   └── styles.css    
    │   ├── js/               
    │   │   └── scripts.js    
    │   └── assets/
    │       └── images/
    └── templates/            
        └── index.html               
```

