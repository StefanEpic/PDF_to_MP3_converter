from gtts import gTTS
from art import tprint
import pdfplumber
from pathlib import Path
import os


def pdf_to_mp3(file_path='test.pdf', language='ru'):
    if Path(file_path).is_file() and Path(file_path).suffix == '.pdf':
        print('Запущен процесс конвертации...')

        with pdfplumber.PDF(open(file=file_path, mode='rb')) as pdf:
            pages = [page.extract_text() for page in pdf.pages]

        text = ''.join(pages).replace('\n', '')
        my_audio = gTTS(text=text, lang=language, slow=False)
        file_name = Path(file_path).stem
        file_path = os.path.abspath(file_path)
        my_audio.save(f'{file_path}.mp3')
        os.system(f'explorer.exe {os.path.abspath(os.path.dirname(file_path))}')

        return f'{file_name}.mp3 успешно создан!'
    else:
        return 'Некорректный формат файла!'


def main():
    tprint('PDF to MP3', font='beer_pub')
    file_path = input('Введите путь к файлу: ')
    language = input('Выберите язык (ru, en): ')
    print(pdf_to_mp3(file_path=file_path, language=language))


if __name__ == '__main__':
    main()
