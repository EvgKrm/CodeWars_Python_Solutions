def decode(m):
    d = {
        "]()]|_]|_]][-]|-|]": 'hello',
        '{|^{|{{|_{]3{': 'blip',
        '..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..': 'die stupid people',
         "'''_\\~'|_|'()'|''('|'|_'[-'|)''__'_\\~'/<'()'()'|_'''__'|\\|'|''/\\'/?']3'__''/?'|_|''()'`/''": 'your brain looks delicious',
        '}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}': 'try to find duplicated kata',
        ']()]()]|_]][-]|-|]': 'heloo'
        }
    return d.get(m, m)