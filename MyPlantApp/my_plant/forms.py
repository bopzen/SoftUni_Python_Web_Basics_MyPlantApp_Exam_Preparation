from django import forms

from MyPlantApp.my_plant.models import Profile, Plant


class ProfileCreateForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['profile_picture']


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class ProfileDeleteForm(ProfileEditForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_hidden_fields()

    def save(self, commit=True):
        if self.instance:
            Plant.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __set_hidden_fields(self):
        for _, field in self.fields.items():
            field.widget = forms.HiddenInput()

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'


class PlantDeleteForm(PlantForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_read_only_fields()

    def save(self, commit=True):
        if self.instance:
            self.instance.delete()
        return self.instance

    def __set_read_only_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'
