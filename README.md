#Follow this guide to run and check this project

#Step 1:
- Install all requirements from requirements.txt using command "pip install -r requirements.txt"

#Step 2:
- Go to the directory where manage.py exists, you will find it inside SoulSkill Folder

#Step 3:
- Start the server by running the following command "python manage.py runserver".
  The default port is 8000, you can either open http://localhost:8000/admin or http://05257e38.ngrok.io/admin
  Enter  Username: admin
         Password: admin123

#Steps to test the project:
1. To Add a user:
-  curl -X POST http://127.0.0.1:8000/tenant/adduser/ -d '{"Name":"Abhishek Kumar Piyush","Email":"akpiyush437@gmail.com","Contact":8939420437,"Address":"patna","IpAddress": "192.168.0.3","Token":"SoUlSkIl_AsSiNmEnT","TenantName":"Student"}' -H "Content-Type: application/json"

2. To edit a user details:
- curl -X POST http://127.0.0.1:8000/tenant/edituser/ -d '{"Name":"Piyush","Email":"akpiyush437@gmail.com","Contact":8939420437,"Address":"patna","IpAddress": "192.168.0.3","Token":"SoUlSkIl_AsSiNmEnT","TenantName":"Student"}' -H "Content-Type: application/json"

3. To delete a user:
- curl -X POST http://127.0.0.1:8000/tenant/deleteuser/ -d '{"Email":"akpiyush437@gmail.com","IpAddress": "192.168.0.3","Token":"SoUlSkIl_AsSiNmEnT"}' -H "Content-Type: application/json"

4. View all user in a tenant:
- curl -X POST http://127.0.0.1:8000/tenant/viewtenentuser/ -d '{"IpAddress": "192.168.0.3","TenantName":"Parent","Token":"SoUlSkIl_AsSiNmEnT"}' -H "Content-Type: application/json"

5. Add a tenant:
- curl -X POST http://127.0.0.1:8000/tenant/addtenant/ -d '{"TenantName":"Student","IpAddress": "192.168.0.3","Token":"SoUlSkIl_AsSiNmEnT"}' -H "Content-Type: application/json"
