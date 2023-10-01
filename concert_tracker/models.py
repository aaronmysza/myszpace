from django.db import models


class Venue(models.Model):
    # TODO: use setlist fm id as ID
    id = models.IntegerField(primary_key=True)
    manual_id = models.IntegerField()
    venue = models.CharField(max_length=50)
    previous_name = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    # setlist_fm_id = models.CharField(max_length=30, null=True)

    def __str__(self):
        return f'{self.venue} ({self.previous_name})' if self.previous_name else self.venue


class Concert(models.Model):
    # TODO: use setlist fm id as ID
    id = models.IntegerField(primary_key=True)
    manual_id = models.IntegerField()
    tour_name = models.CharField(max_length=255)
    date = models.DateField()
    venue = models.ForeignKey(Venue, on_delete=models.PROTECT)
    # setlist_fm_id = models.CharField(max_length=30, null=True)


class Band(models.Model):
    # TODO: use setlist fm id as ID
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255, null=True)
    url = models.CharField(max_length=255, null=True)
    manual_id = models.IntegerField(null=True)


class Song(models.Model):
    # TODO: use setlist fm id as ID
    id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.PROTECT)


class Setlist(models.Model):
    # TODO: use setlist fm id as ID
    id = models.IntegerField(primary_key=True)
    song_name = models.CharField(max_length=255)
    band = models.ForeignKey(Band, on_delete=models.PROTECT)


class Set(models.Model):
    # TODO: use setlist fm id as ID
    id = models.IntegerField(primary_key=True)
    manual_id = models.IntegerField()
    tour = models.ForeignKey(Concert, on_delete=models.PROTECT)
    band = models.ForeignKey(Band, on_delete=models.PROTECT)
    memorable = models.BooleanField(default=False)
    notes = models.TextField()


class Attendee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=30, null=True)
    nickname = models.CharField(max_length=30, null=True)
    manual_id = models.IntegerField()

    def __str__(self):
        default = f'{self.first_name} {self.last_name}'
        return f'{self.first_name} "{self.nickname}" {self.last_name}' if self.nickname else default


class ConcertAttendance(models.Model):
    attendee = models.ForeignKey(Attendee, on_delete=models.PROTECT)
    concert = models.ForeignKey(Concert, on_delete=models.PROTECT)



