#
# Conta quantas ocorrências de uma palavra há no arquivo
#

def stringCount(filename, word, case_sensitive=False):

    if not case_sensitive:
        word = word.lower()

    hFile = open(filename, 'r')

    print('\nEncontrado:\n')

    words_found = 0
    line_number = 0

    for line in hFile:

        line_number += 1

        if len(line) < len(word):
            continue

        words_in_line = 0

        for x in line.split():
            if word in (x.lower() if not case_sensitive else x):
                words_in_line += 1

        if words_in_line == 0:
            continue

        words_found += words_in_line
        print(words_in_line, 'palavra(s) na linha', '#' + str(line_number))

    hFile.close()

    return words_found


word_search = 'PYTHON'

print('\nTotal de', stringCount('teste_string_count.txt', word_search),
      'palavra(s)', '"' + word_search + '" no arquivo')
