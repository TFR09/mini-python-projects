employees = [
    {
        "first_name":"Jose",
        "last_name":"Lopez",
        "email":"joselopez0944@example.com",
        "age":25,
        "job_title":"Project Manager",
        "years_of_experience":1,
        "salary":8500,
        "department":"Product"
    },
    {
        "first_name":"Diane",
        "last_name":"Carter",
        "email":"dianecarter1228@example.com",
        "age":26,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":2,
        "salary":7000,
        "department":"Product"
    },
    {
        "first_name":"Shawn",
        "last_name":"Foster",
        "email": None,
        "age":37,
        "job_title":"Customer Service Rep",
        "years_of_experience":14,
        "salary":17000,
        "department":"Business"
    },
    {
        "first_name":"Brenda",
        "last_name":"Fisher",
        "email":"brendafisher3185@example.com",
        "age":31,
        "job_title":"Web Developer",
        "years_of_experience":8,
        "salary":10000,
        "department":"Product"
    },
    {
        "first_name":"Sean",
        "last_name":"Hunter",
        "email": None,
        "age":35,
        "job_title":"Project Manager",
        "years_of_experience":11,
        "salary":14500,
        "department":"Product"
    },
    {
        "first_name":"Joshua",
        "last_name":"Jacobs",
        "email":"joshuajacobs5904@example.com",
        "age":28,
        "job_title":"Project Manager",
        "years_of_experience":3,
        "salary":10500,
        "department":"Business"
    },
    {
        "first_name":"Brianna",
        "last_name":"Marshall",
        "email":None,
        "age":33,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":10,
        "salary":11000,
        "department":"Product"
    },
    {
        "first_name":"John",
        "last_name":"Tate",
        "email":"johntate7881@example.com",
        "age":33,
        "job_title":"Mobile Developer",
        "years_of_experience":10,
        "salary":11000,
        "department":"Product"
    },
    {
        "first_name":"Jillian",
        "last_name":"Byrd",
        "email":None,
        "age":34,
        "job_title":"Business Analyst",
        "years_of_experience":10,
        "salary":11000,
        "department":"Business"
    },
    {
        "first_name":"Melanie",
        "last_name":"Sharp",
        "email":"melaniesharp9256@example.com",
        "age":41,
        "job_title":"Web Developer",
        "years_of_experience":15,
        "salary":14500,
        "department":"Product"
    },
    {
        "first_name":"Brandy",
        "last_name":"Mckee",
        "email":None,
        "age":37,
        "job_title":"Marketing Manager",
        "years_of_experience":14,
        "salary":14000,
        "department":"Business"
    },
    {
        "first_name":"Robert",
        "last_name":"Simpson",
        "email":"robertsimpson11778@example.com",
        "age":36,
        "job_title":"Marketing Manager",
        "years_of_experience":12,
        "salary":15000,
        "department":"Business"
    },
    {
        "first_name":"George",
        "last_name":"Mckenzie",
        "email":"georgemckenzie12384@example.com",
        "age":28,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":4,
        "salary":10000,
        "department":"Product"
    },
    {
        "first_name":"Joseph",
        "last_name":"Smith",
        "email":None,
        "age":40,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":14,
        "salary":14000,
        "department":"Product"
    },
    {
        "first_name":"Dana",
        "last_name":"Crawford",
        "email":"danacrawford14310@example.com",
        "age":32,
        "job_title":"Project Manager",
        "years_of_experience":8,
        "salary":12000,
        "department":"Product"
    },
    {
        "first_name":"Christopher",
        "last_name":"Benson",
        "email":None,
        "age":29,
        "job_title":"Web Developer",
        "years_of_experience":5,
        "salary":7500,
        "department":"Product"
    },
    {
        "first_name":"Nicole",
        "last_name":"Smith",
        "email":"nicolesmith16360@example.com",
        "age":26,
        "job_title":"Designer",
        "years_of_experience":4,
        "salary":10000,
        "department":"Product"
    },
    {
        "first_name":"Peter",
        "last_name":"Jimenez",
        "email":"peterjimenez17791@example.com",
        "age":28,
        "job_title":"UX Designer",
        "years_of_experience":3,
        "salary":6500,
        "department":"Business"
    },
    {
        "first_name":"Sergio",
        "last_name":"Boyle",
        "email":"sergioboyle18425@example.com",
        "age":31,
        "job_title":"Tester",
        "years_of_experience":6,
        "salary":9000,
        "department":"Product"
    },
    {
        "first_name":"Brianna",
        "last_name":"Moss",
        "email":None,
        "age":31,
        "job_title":"Designer",
        "years_of_experience":5,
        "salary":10500,
        "department":"Product"
    },
    {
        "first_name":"Taylor",
        "last_name":"Garner",
        "email":"taylorgarner20196@example.com",
        "age":32,
        "job_title":"Machine Learning Engineer",
        "years_of_experience":6,
        "salary":11000,
        "department":"Product"
    },
    {
        "first_name":"Michael",
        "last_name":"Padilla",
        "email":"michaelpadilla21381@example.com",
        "age":29,
        "job_title":"Customer Service Rep",
        "years_of_experience":5,
        "salary":9500,
        "department":"Business"
    },
    {
        "first_name":"Yvette",
        "last_name":"Walker",
        "email":None,
        "age":26,
        "job_title":"Designer",
        "years_of_experience":2,
        "salary":7000,
        "department":"Product"
    },
    {
        "first_name":"Kristina",
        "last_name":"Pena",
        "email":"kristinapena23750@example.com",
        "age":34,
        "job_title":"Business Analyst",
        "years_of_experience":11,
        "salary":12500,
        "department":"Business"
    }
]

employees_without_email = []
highest = 0
total_experience = 0

for employee in employees:
    # get highest salary
    highest = max(employee["salary"], highest)

    # get aggregate experience
    total_experience += employee["years_of_experience"]

    # collect details of employees without email
    if not employee["email"]:
        employees_without_email.append(employee)

print(f"The highest salary is ${highest}")
print(f"The total experience of everyone in the company is {total_experience} years")

# Higher department salary cost for business
product_dept_salaries = 0
business_dept_salaries = 0
for employee in employees:
    if employee["department"] == "Business":
        business_dept_salaries += employee["salary"]

    if employee["department"] == "Product":
        product_dept_salaries += employee["salary"]

if product_dept_salaries > business_dept_salaries:
    print(f"Product Department salaries are higher at ${product_dept_salaries} compared to business at ${business_dept_salaries}")
elif product_dept_salaries < business_dept_salaries:
    print(f"Business Department salaries are higher at ${business_dept_salaries} compared to product at ${product_dept_salaries}")
else:
    print(f"They both cost the same at ${business_dept_salaries}") 

# Average salary for people over 30
salary_over_30 = 0
people_over_30 = 0
for employee in employees:
    if employee["age"] > 30:
        salary_over_30 += employee["salary"]
        people_over_30 += 1

avg_salary = round(salary_over_30 / people_over_30)
print(f"Average salary for people over 30 is ${avg_salary}")

# How many people in each job title
jobs = {}
for employee in employees:
    job = employee["job_title"]
    jobs[job] = jobs.get(job, 0) + 1

print(jobs)