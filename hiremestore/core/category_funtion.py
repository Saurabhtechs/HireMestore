from .models import Category

def Category_Data():
    data = Category.objects.all()
    # print(data)
    return data


# def SubCategory_Data():
#     data = Category.objects.all()
#     return data