agency_name = "Creative Digital"
team_size = 8
project_fee = 450000.0
is_accepting_clients = True

services = ["web design", "social media", "SEO", "branding"]
new_services = ["video editing", "AI automation"]

print(type(agency_name))
print(type(team_size))
print(type(project_fee))
print(type(is_accepting_clients))
print(type(services))
print(type(new_services))

if project_fee>=400000:
    print("hight value project")
else:
    print("standard project")
print(services)
services[2]="SEO optimization"
print(services)
services.append("UI/UX design")
print(services)
services.insert(1, "content writing")
print(services)
services.extend(new_services)
print(services)
services.remove("branding")
print(services)
services.pop()
print(services)