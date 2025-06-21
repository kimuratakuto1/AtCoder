def function(name, *args, **kwargs):
    print(name)
    print(args)
    print(kwargs)

function("spam", "ham","egg", kwargs1="eggs", kwargs2="spamhameggs")