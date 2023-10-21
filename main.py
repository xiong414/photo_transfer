import PIL.Image
import os, shutil

def get_exif(path):
    img = PIL.Image.open(path)
    exif_data = img.getexif()
    date = exif_data[306]
    year = date[:4]
    month = date[5:7]
    day = date[8:10]
    # print('{}_{}_{}_'.format(year, month, day))
    return '{}_{}_{}_'.format(year, month, day)

def img_copy(date, input_path, output_path):
    i = 1
    while True:
        number = '{:05d}'.format(i)
        destination = output_path + date + number + '.JPG'
        if os.path.exists(destination):
            i += 1
            continue
        else:
            shutil.copy2(input_path, destination)
            break

def batch_process(input_dir, output_dir):
    all_img = os.listdir(input_dir)
    all_img.sort(key=lambda x: os.path.getmtime(input_dir + x))
    for img_name in all_img:
        date = get_exif(input_dir + img_name)
        img_copy(date, input_dir + img_name, output_dir)
            


if __name__ == '__main__':
    input_dir = '/Users/xiongguoqing/tools/photo_transfer/input/'
    output_dir = '/Users/xiongguoqing/tools/photo_transfer/output/'
    batch_process(input_dir, output_dir)
