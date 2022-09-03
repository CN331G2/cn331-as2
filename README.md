Software Engineering CN331
=====================

Assignment #2 - Create Django Web App
---------------------

### Requirements
- ระบบรองรับการเข้าสู่ระบบโดยแยกเป็น admin และ students (user ทั่วไป)
- Admin สามารถจัดการกับรายวิชาได้ผ่าน admin interface ของ Django โดยรายวิชาประกอบด้วย **รหัส ชื่อ ภาคการศึกษา และปีิการศึกษา จํานวนที่นั่งที่รับได้ และสามารถกําหนดสถานะว่าเปิดหรือปิดรับการขอโควต้าอยู่**
- Students สามารถเลือกดูรายวิชาที่เปิดให้ขอโควต้า และกดขอโควต้าได้หากยังมีที่นั่งว่าง
- Students สามารถดูรายชื่อวิชาที่ขอโควต้าได้สําเร็จ และสามารถยกเลิกการขอโควต้าได้ (ในกรณีนี้จะมีที่ว่างให้คนอื่นสามารถลงเพิ่มได้)
- (optionals) สามารถเพิ่มฟังก์ชันการทํางานอื่นได้ตามต้องการ เช่น Admin สามารถดูรายชื่อนักเรียนที่ขอโควต้าในแต่ละรายวิชาได้

> Group member
>> |    Name         |  Student ID  |
>> |-----------------|--------------|
>> |  ศุภกฤต นืธิเกตุกุล  |  6410615139  |
>> |  ณธิพร จันทร์เพ็ชร  |  6410615030  |

### System ability
They are . folder in this repository
1. .venv 
    - set versual environment
    - create **requirement.txt text file**
        - **requirements.txt text file** is for note this project environment.

2. DjangoWeb 
    - staring project folder
    - including **manage.py pythonfile**
        - **manage.py pythonfile** is for interact with the project
        <details open>
        <summary> such as</summary>

        * runserver
        * startapp
        * makemigrates
        * migrate
        * shell
        * createsupperuser
        
        </details>

    1. DjangoWeb
        1. \__init__.py
        2. settings.py
            - update more app
            - change time zone
        
        3. urls.py
            - declare urls 
            - connect urls from app to project
        4. asgi.py
        5. wsgi.py

    2. courses
        - app for ...   
        1. \__init__.py
        2. admin.py
        3. apps.py
        4. migrations
            - update migration 
            1. \__init__.py
        5. models.py
        6. tests.py
        7. views.py
            - mapping 
        8. urls.py
            - connect urls in project to app
            - 





[GitHub repo url](https://github.com/CN331G2/cn331-as2.git) 

[Vedio link]()

