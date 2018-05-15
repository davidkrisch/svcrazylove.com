from PIL import Image, ExifTags
import glob, os

small_size = 768, 768
thumb_size = 256, 256

files = glob.glob('*.jpg')
files.extend(glob.glob('*.JPG'))

for infile in files:
    file_parts = infile.split('.')
    if 'small' not in file_parts and 'thumb' not in file_parts:
        print file_parts
        if not os.path.exists('%s.small.jpg' % file_parts[0]) and not os.path.exists('%s.thumb.jpg' % file_parts[0]):
            small = Image.open(infile)

            # Deal with rotation issues
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation] == 'Orientation':
                    break

            exif = small._getexif()

            if exif is not None:
                exif_items = dict(exif.items())
                if orientation in exif_items:
                    orientation = exif_items[orientation]

                    if orientation == 3:
                        small = small.transpose(Image.ROTATE_180)
                    elif orientation == 6:
                        small = small.transpose(Image.ROTATE_270)
                    elif orientation == 8:
                        small = small.transpose(Image.ROTATE_90)

            thumb = small.copy()

            small.thumbnail(small_size, Image.ANTIALIAS)
            print 'Saving ', file_parts[0] + ".small.jpg"
            small.save(file_parts[0] + ".small.jpg", "JPEG")

            thumb.thumbnail(thumb_size, Image.ANTIALIAS)
            print 'Saving ', file_parts[0] + ".thumb.jpg"
            thumb.save(file_parts[0] + ".thumb.jpg", "JPEG")
