guess_word = 'tomorrow'
under_ = list(len(guess_word)*'_')
while under_ != guess_word:
    guess = input('try')
    while guess in guess_word:
        under_[guess_word.find(guess)] = guess
        kostil = list(guess_word)   # Заміна відгаданої букви на _ що б знайти повтор.
        kostil[guess_word.find(guess)] = '_'
        guess_word = ''.join(kostil)
    print(under_)
