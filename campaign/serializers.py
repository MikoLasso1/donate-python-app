from campaign.models import Campaign, CampaignFiles
from rest_framework import serializers


# class CampaignSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Campaign
#         fields = '__all__'

class CampaignFilesSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=False)
    video = serializers.FileField(use_url=False)
    class Meta:
        model = CampaignFiles
        fields = ['id', 'image', 'video','campaign']

class CampaignSerializer(serializers.ModelSerializer):
    campaign_data = CampaignFilesSerializer(many=True, read_only=True)
    class Meta:
        model = Campaign
        fields = ['id','title', 'target_amount', 'raised_amount', 'start_date', 'end_date', 'detail', 'masjid_id', 'campaign_data']




