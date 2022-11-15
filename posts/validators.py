from django.core.exceptions import ValidationError


def validate_image(image):
    file_size = image.file.size
    limit_mb = 1
    if file_size > limit_mb * 1024 * 1024:
        raise ValidationError("Max size of file is %s KB" % limit_mb)
