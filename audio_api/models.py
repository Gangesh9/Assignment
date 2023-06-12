from django.db import models

# Create your models here.
from django.db import models

class AudioElement(models.Model):
    AUDIO_TYPES = (
        ('vo', 'Voice Over'),
        ('bg_music', 'Background Music'),
        ('video_music', 'Video Music'),
    )
    
    id = models.AutoField(primary_key=True)
    type = models.CharField(choices=AUDIO_TYPES, max_length=20)
    high_volume = models.IntegerField()
    low_volume = models.IntegerField()
    video_component_id = models.CharField(max_length=50, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    start_time = models.IntegerField()
    end_time = models.IntegerField()
