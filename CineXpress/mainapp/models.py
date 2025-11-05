from django.db import models 

# Here, we model the schema, i.e., 
# directs the project on which tables and their schema has to be built.
# Every class we design here becomes a table on its own in the DB.
# The table name will be <app_name>_<model_class_name> .
# For eg:, the below model will create the table `mainapp_carouselimage` 
# when migrations are run.

# Create your models here.

class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel/')
    title = models.CharField(max_length=100, blank=True, null=True)
    caption = models.TextField(max_length=100, null=True, blank=True)
    added_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"Carousel Image : {self.title}"