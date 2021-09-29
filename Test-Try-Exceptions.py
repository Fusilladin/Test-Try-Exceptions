# TRY EXCEPTIONS




# try:
#     f = open('testfile.txt')
#     var = bad_var
# except FileNotFoundError:
#     print('Sorry. This file does not exist.')
# except Exception:
#     print('Sorry, something went wrong.')
######
try:
    f = open('corrupt_file.txt')
    if f.name == 'corrupt_file.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print('Executing Finally...')
