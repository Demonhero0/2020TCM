import os
import sys
import django


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.local')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
    from project.main.models import Medicine,Disease

    django.setup()
    os.chdir('medicine')
    file_list = os.listdir()
    for txt in file_list:
        disease_name = txt.split('.')[0]
        print(disease_name)
        disease_query = Disease.objects.filter(name=disease_name)
        for disease in disease_query:
            f = open(f'{disease_name}.txt')
            lines = f.readlines()
            count = 1
            name = ''
            composition = ''
            effect = ''
            for line in lines:
                line = line.strip()
                if line == '':
                    continue
                names = line.split('：')
                if count == 1:
                    name = names[0]
                    count += 1
                elif count == 2:
                    composition = names[1]
                    count += 1
                elif count == 3:
                    effect = names[1]
                    medicine,flag = Medicine.objects.get_or_create(name=name,composition=composition,effect=effect)
                    medicine.diseases.add(disease)
                    medicine.save()
                    print(medicine,flag)
                    count = 1
        