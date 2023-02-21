import urllib.request
contents = urllib.request.urlopen("https://admin.rabbitapp.co/admin/orders/order/?created_at__day=14&created_at__month=2&created_at__year=2023").read()

print(contents)

# https://admin.rabbitapp.co/admin/orders/order/?created_at__day=14&created_at__month=2&created_at__year=2023