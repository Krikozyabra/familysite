from datetime import date
from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import FamilyMember, Relations, Images


@admin.register(FamilyMember)
class FamilyMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age' ,'bornDate','deathDate','photoC','photo', 'bio')
    list_display_links = ('id', 'name')
    list_editable = ('bio','photo', 'bornDate', 'deathDate')

    @admin.display(description='Дата смерти')
    def deathC(self, man: FamilyMember):
        if man.deathDate:
            return man.deathDate
        return "Жив/Нет информации"

    @admin.display(description="Возраст")
    def age(self, man: FamilyMember):
        dateNow = date.today()
        if man.deathDate:
            dateNow = man.deathDate
        return f"{int(str(dateNow - man.bornDate)[:5])//365} лет"

    @admin.display(description='Фото')
    def photoC(self, man: FamilyMember):
        if man.photo:
            return mark_safe(f'<img src="{man.photo.url}" width="70%">')
        return "Без фото"


@admin.register(Images)
class ImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'photo')

    @admin.display(description='Фото')
    def photo(self, image: Images):
        if image.image:
            return mark_safe(f'<img src="{image.image.url}" width="30%">')
        return "Без фото"


@admin.register(Relations)
class RelationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'parentname', 'childname')

    @admin.display(description="Родитель")
    def parentname(self, relation: Relations):
        return relation.parent.name

    @admin.display(description="Ребенок")
    def childname(self, relation: Relations):
        return relation.child.name
