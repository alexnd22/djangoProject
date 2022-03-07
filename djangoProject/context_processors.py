from category.models import Category


def get_all_categories(request):
    all_categories = Category.objects.all()
    return {'allcategories': all_categories}
