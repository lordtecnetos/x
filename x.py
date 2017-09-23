#!/usr/bin/python3

import os
import shutil
import subprocess


JPG, PNG, WEBP = 'jpg', 'png', 'webp'

IMG = '{}.{}'


def convert_webp_to_png(webp, png):
    subprocess.call(['dwebp', webp, '-o', png])
    print()


def convert_png_to_jpg(png, jpg):
    print('Converting {} to {} format...'.format(png, JPG))
    subprocess.call(['mogrify', '-format', JPG, png])
    print('Saved file {}\n'.format(jpg))


def makedirs(*dirs):
    created = []
    print('Creating directorys...')
    for dir_ in dirs:
        try:
            os.mkdir(dir_)
            created.append(dir_ + '/')
        except FileExistsError:
            print('{}/ already exists'.format(dir_))
    
    if created:
        print('Created {}\n'.format(' '.join(created)))


def arrange(*imgs):
    dests = (JPG, PNG, WEBP)
    print('Moving images...')
    for img in imgs:
        dest = os.path.splitext(img)[-1].lstrip('.')
        if dest in dests:
            shutil.move(img, dest)
            print('Moved {} to {}/'.format(img, dest))
        else:
            print('Ignored {}: File format not allowed'.format(img))

    print()


def main(webps):
    if not webps:
        print('Nothing to do...')
        return
    
    print('##### BEGIN #####\n')
    
    # cria as pastas
    makedirs(JPG, PNG, WEBP)
    
    for webp in webps:
        # extrai informações do arquivo
        name = os.path.splitext(webp)[0]
        png = IMG.format(name, PNG)
        jpg = IMG.format(name, JPG)
        
        print('# Starting convertion of {!r} file:\n'.format(name))
        
        # converte as imagens
        convert_webp_to_png(webp, png)
        convert_png_to_jpg(png, jpg)
        
        # organiza os arquivos
        arrange(jpg, png, webp)
    
    print('##### END #####')


if __name__ == '__main__':
    main(sorted([f for f in os.listdir() if f.endswith('.webp')]))

