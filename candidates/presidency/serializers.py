from rest_framework import serializers

from candidates.presidency.models import PresidencyModel, ExperienceModel, PoliticModel, Studies, InvestigationModel
from candidates.vpresidency.models import PVpresidencyModel, SVpresidencyModel


class PoliticSerializers(serializers.ModelSerializer):

    class Meta:
        model = PoliticModel
        fields = '__all__'

class ExperienceSerializers(serializers.ModelSerializer):

    class Meta:
        model = ExperienceModel
        fields = '__all__'

class StudiesSerializars(serializers.ModelSerializer):

    class Meta:
        model = Studies
        fields = '__all__'


class InvestigationSerializers(serializers.ModelSerializer):

    class Meta:
        model = InvestigationModel
        fields = '__all__'

#VICE presidencia
class PVpresidencySerializers(serializers.ModelSerializer):

    class Meta:
        model = PVpresidencyModel
        fields = '__all__'

class SVpresidencySerializers(serializers.ModelSerializer):

    class Meta:
        model = SVpresidencyModel
        fields = '__all__'

class PresidencySerializers(serializers.ModelSerializer):

    politic_part = PoliticSerializers(read_only=True)
    experience = ExperienceSerializers(read_only=True, many=True)
    studes = StudiesSerializars(read_only=True, many=True)
    investigation = InvestigationSerializers(read_only=True, many=True)

    pvpresidency = PVpresidencySerializers(read_only=True)
    svpresidency = SVpresidencySerializers(read_only=True)

    class Meta:
        model = PresidencyModel
        fields = ('id',
                  'name',
                  'surname',
                  'birthday',
                  'photo',
                  'politic_part',
                  'experience',
                  'studes',
                  'investigation',
                  'pvpresidency',
                  'svpresidency',
                  )