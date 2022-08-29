import harperdb
from django.conf import settings

url = settings.HARPERDB_URL

db = harperdb.HarperDB(url=url, username=settings.HARPERDB_USERNAME, password=settings.HARPERDB_PASSWORD)

SCHEMA = "accounts"
TABLE = "user"

DATA = [
  {
    "email": "cherryanthony@anivet.com",
    "first_name": "Reyes",
    "last_name": "Marshall",
    "profile_image": "https://freesvg.org/img/Faceless-Male-Avatar-In-Suit.png",
    "title_tag": "Fullstack Developer",
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ante ipsum, consequat vitae mattis volutpat, facilisis iaculis metus. Nullam ligula elit, porttitor quis lacinia et, commodo vel elit. Duis justo enim, aliquet non sem venenatis, rutrum eleifend ligula. Quisque vitae sodales dui. Donec id porta ligula. Nulla elementum pellentesque sapien, vehicula luctus velit volutpat in. Duis ut velit sapien. Aenean ornare faucibus nulla. Sed velit odio, rutrum sed libero eu, gravida iaculis augue. Sed commodo, dui et varius ultricies, risus mi rhoncus lectus, malesuada sollicitudin turpis nisl eget diam. Suspendisse mattis felis felis, et facilisis nunc varius eget. Duis eu molestie urna.",
    "skills": [
      "Python",
      "FastAPI",
      "Javascript",
      "PHP",
      "HTML",
      "CSS"
    ],
    "country": "Nepal",
    "is_looking": "Remote Job",
    "experience_years": "1-3",
    "expertise_levels": "Intermediate",
    "degree": "Bachelor",
    "is_hirable": "False",
    "username": "marshallreyes"
  },
  {
    "email": "reyesmarshall@anivet.com",
    "first_name": "Grace",
    "last_name": "Chang",
    "profile_image": "https://freesvg.org/img/Faceless-Male-Avatar-In-Suit.png",
    "title_tag": "Game Developer",
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ante ipsum, consequat vitae mattis volutpat, facilisis iaculis metus. Nullam ligula elit, porttitor quis lacinia et, commodo vel elit. Duis justo enim, aliquet non sem venenatis, rutrum eleifend ligula. Quisque vitae sodales dui. Donec id porta ligula. Nulla elementum pellentesque sapien, vehicula luctus velit volutpat in. Duis ut velit sapien. Aenean ornare faucibus nulla. Sed velit odio, rutrum sed libero eu, gravida iaculis augue. Sed commodo, dui et varius ultricies, risus mi rhoncus lectus, malesuada sollicitudin turpis nisl eget diam. Suspendisse mattis felis felis, et facilisis nunc varius eget. Duis eu molestie urna.",
    "skills": [
      "Java",
      "C#",
    ],
    "country": "Australia",
    "is_looking": "Part Time Job",
    "experience_years": "3-5",
    "expertise_levels": "Intermediate",
    "degree": "Master",
    "is_hirable": "True",
    "username": "changgrace"
  },
  {
    "email": "gracechang@anivet.com",
    "first_name": "Norma",
    "last_name": "Miller",
    "profile_image": "https://freesvg.org/img/Faceless-Male-Avatar-In-Suit.png",
    "title_tag": "Python Developer",
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ante ipsum, consequat vitae mattis volutpat, facilisis iaculis metus. Nullam ligula elit, porttitor quis lacinia et, commodo vel elit. Duis justo enim, aliquet non sem venenatis, rutrum eleifend ligula. Quisque vitae sodales dui. Donec id porta ligula. Nulla elementum pellentesque sapien, vehicula luctus velit volutpat in. Duis ut velit sapien. Aenean ornare faucibus nulla. Sed velit odio, rutrum sed libero eu, gravida iaculis augue. Sed commodo, dui et varius ultricies, risus mi rhoncus lectus, malesuada sollicitudin turpis nisl eget diam. Suspendisse mattis felis felis, et facilisis nunc varius eget. Duis eu molestie urna.",
    "skills": [
      "Python",
      "Javascript",
      "HTML",
      "CSS"
    ],
    "country": "India",
    "is_looking": "Full Time Job",
    "experience_years": "0-1",
    "expertise_levels": "Beginner",
    "degree": "Bachelor",
    "is_hirable": "True",
    "username": "millernorma"
  },
  {
    "email": "normamiller@anivet.com",
    "first_name": "Marian",
    "last_name": "Rowland",
    "profile_image": "https://freesvg.org/img/Faceless-Male-Avatar-In-Suit.png",
    "title_tag": "Fullstack Developer",
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ante ipsum, consequat vitae mattis volutpat, facilisis iaculis metus. Nullam ligula elit, porttitor quis lacinia et, commodo vel elit. Duis justo enim, aliquet non sem venenatis, rutrum eleifend ligula. Quisque vitae sodales dui. Donec id porta ligula. Nulla elementum pellentesque sapien, vehicula luctus velit volutpat in. Duis ut velit sapien. Aenean ornare faucibus nulla. Sed velit odio, rutrum sed libero eu, gravida iaculis augue. Sed commodo, dui et varius ultricies, risus mi rhoncus lectus, malesuada sollicitudin turpis nisl eget diam. Suspendisse mattis felis felis, et facilisis nunc varius eget. Duis eu molestie urna.",
    "skills": [
      "Python",
      "Java",
      "Go",
      "C#",
      "C++",
    ],
    "country": "India",
    "is_looking": "Remote Job",
    "experience_years": "10+",
    "expertise_levels": "Expert",
    "degree": "PhD",
    "is_hirable": "False",
    "username": "rowlandmarian"
  },
  {
    "email": "marianrowland@anivet.com",
    "first_name": "Sabrina",
    "last_name": "Carpenter",
    "profile_image": "https://freesvg.org/img/Faceless-Male-Avatar-In-Suit.png",
    "title_tag": "Backend Developer",
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ante ipsum, consequat vitae mattis volutpat, facilisis iaculis metus. Nullam ligula elit, porttitor quis lacinia et, commodo vel elit. Duis justo enim, aliquet non sem venenatis, rutrum eleifend ligula. Quisque vitae sodales dui. Donec id porta ligula. Nulla elementum pellentesque sapien, vehicula luctus velit volutpat in. Duis ut velit sapien. Aenean ornare faucibus nulla. Sed velit odio, rutrum sed libero eu, gravida iaculis augue. Sed commodo, dui et varius ultricies, risus mi rhoncus lectus, malesuada sollicitudin turpis nisl eget diam. Suspendisse mattis felis felis, et facilisis nunc varius eget. Duis eu molestie urna.",
    "skills": [
      "Python",
      "Django",
      "FastAPI",
      "Javascript",
      "PHP",
    ],
    "country": "Belgium",
    "is_looking": "Part Time Job",
    "experience_years": "5-10",
    "expertise_levels": "Expert",
    "degree": "Master",
    "is_hirable": "False",
    "username": "carpentersabrina"
  },
  {
    "email": "sabrinacarpenter@anivet.com",
    "first_name": "Calhoun",
    "last_name": "Carroll",
    "profile_image": "https://freesvg.org/img/Faceless-Male-Avatar-In-Suit.png",
    "title_tag": "Fullstack Backend Developer",
    "about": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam ante ipsum, consequat vitae mattis volutpat, facilisis iaculis metus. Nullam ligula elit, porttitor quis lacinia et, commodo vel elit. Duis justo enim, aliquet non sem venenatis, rutrum eleifend ligula. Quisque vitae sodales dui. Donec id porta ligula. Nulla elementum pellentesque sapien, vehicula luctus velit volutpat in. Duis ut velit sapien. Aenean ornare faucibus nulla. Sed velit odio, rutrum sed libero eu, gravida iaculis augue. Sed commodo, dui et varius ultricies, risus mi rhoncus lectus, malesuada sollicitudin turpis nisl eget diam. Suspendisse mattis felis felis, et facilisis nunc varius eget. Duis eu molestie urna.",
    "skills": [
      "Python",
      "Javascript",
      "PHP",
      "HTML",
      "CSS"
    ],
    "country": "USA",
    "is_looking": "Full Time Job",
    "experience_years": "1-3",
    "expertise_levels": "Intermediate",
    "degree": "Bachelor",
    "is_hirable": "True",
    "username": "carrollcalhoun"
  }
]

def create_schema():
    db.create_schema(SCHEMA)

def create_table():
    db.create_table(SCHEMA, TABLE, "id")

def insert_data():
    db.insert(SCHEMA, TABLE, DATA)

def get_all_users():
    try:
        users = db.sql("SELECT * FROM {}.{}".format(SCHEMA, TABLE))
        if users:
            return users
        else:
            insert_data()
            return get_all_users()
    except Exception as e:
        if e.args[0] == f"Schema '{SCHEMA}' does not exist":
            create_schema()
            create_table()
            insert_data()
        if e.args[0] == f"Table '{SCHEMA}.{TABLE}' does not exist":
            create_table()
            insert_data()
        return get_all_users()

def get_user_by_id(id):
    user = db.search_by_hash(SCHEMA, TABLE, [id], get_attributes=['*'])
    return user[0] if user else None
