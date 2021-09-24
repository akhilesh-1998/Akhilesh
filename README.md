
Python - Overview

This entire repository is dedicated to budding python enthusiats. Hope you will enjoy it. Read through the history of python as well. Few codes on advanced python added as well.

History
Python was conceived in the late 1980s by Guido van Rossum at Centrum Wiskunde & Informatica (CWI) in the Netherlands as a successor to ABC programming language, which was inspired by SETL, capable of exception handling and interfacing with the Amoeba operating system. Its implementation began in December 1989. Van Rossum shouldered sole responsibility for the project, as the lead developer, until 12 July 2018, when he announced his "permanent vacation" from his responsibilities as Python's Benevolent Dictator For Life, a title the Python community bestowed upon him to reflect his long-term commitment as the project's chief decision-maker. In January 2019, active Python core developers elected a 5-member "Steering Council" to lead the project. As of 2021, the current members of this council are Barry Warsaw, Brett Cannon, Carol Willing, Thomas Wouters, and Pablo Galindo Salgado.

Python 2.0 was released on 16 October 2000, with many major new features, including a cycle-detecting garbage collector and support for Unicode.

Python 3.0 was released on 3 December 2008. It was a major revision of the language that is not completely backward-compatible. Many of its major features were backported to Python 2.6.x and 2.7.x version series. Releases of Python 3 include the 2to3 utility, which automates (at least partially) the translation of Python 2 code to Python 3.

Python 2.7's end-of-life date was initially set at 2015 then postponed to 2020 out of concern that a large body of existing code could not easily be forward-ported to Python 3. No more security patches or other improvements will be released for it. With Python 2's end-of-life, only Python 3.6.xand later are supported.

Python 3.9.2 and 3.8.8 were expedited[53] as all versions of Python (including 2.7) had security issues, leading to possible remote code execution and web cache poisoning.

Design philosophy and features
Python is a multi-paradigm programming language. Object-oriented programming and structured programming are fully supported, and many of its features support functional programming and aspect-oriented programming (including by metaprogramming[57] and metaobjects (magic methods)).[58] Many other paradigms are supported via extensions, including design by contract[59][60] and logic programming.[61]

Python uses dynamic typing and a combination of reference counting and a cycle-detecting garbage collector for memory management.[62] It also features dynamic name resolution (late binding), which binds method and variable names during program execution.

Python's design offers some support for functional programming in the Lisp tradition. It has filter,mapandreduce functions; list comprehensions, dictionaries, sets, and generator expressions.[63] The standard library has two modules (itertools and functools) that implement functional tools borrowed from Haskell and Standard ML.[64]

The language's core philosophy is summarized in the document The Zen of Python (PEP 20), which includes aphorisms such as:[65]

Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Readability counts. Rather than having all of its functionality built into its core, Python was designed to be highly extensible (with modules). This compact modularity has made it particularly popular as a means of adding programmable interfaces to existing applications. Van Rossum's vision of a small core language with a large standard library and easily extensible interpreter stemmed from his frustrations with ABC, which espoused the opposite approach.[38]

Python strives for a simpler, less-cluttered syntax and grammar while giving developers a choice in their coding methodology. In contrast to Perl's "there is more than one way to do it" motto, Python embraces a "there should be one— and preferably only one —obvious way to do it" design philosophy.[65] Alex Martelli, a Fellow at the Python Software Foundation and Python book author, writes that "To describe something as 'clever' is not considered a compliment in the Python culture."[66]

Python's developers strive to avoid premature optimization, and reject patches to non-critical parts of the CPython reference implementation that would offer marginal increases in speed at the cost of clarity.[67] When speed is important, a Python programmer can move time-critical functions to extension modules written in languages such as C, or use PyPy, a just-in-time compiler. Cython is also available, which translates a Python script into C and makes direct C-level API calls into the Python interpreter.

Python's developers aim to keep the language fun to use. This is reflected in its name—a tribute to the British comedy group Monty Python[68]—and in occasionally playful approaches to tutorials and reference materials, such as examples that refer to spam and eggs (a reference to a Monty Python sketch) instead of the standard foo and bar.[69][70]

A common neologism in the Python community is pythonic, which can have a wide range of meanings related to program style. To say that code is pythonic is to say that it uses Python idioms well, that it is natural or shows fluency in the language, that it conforms with Python's minimalist philosophy and emphasis on readability. In contrast, code that is difficult to understand or reads like a rough transcription from another programming language is called unpythonic.[71][72]

Users and admirers of Python, especially those considered knowledgeable or experienced, are often referred to as Pythonistas.[73][74]

Syntax and semantics
Main article: Python syntax and semantics Python is meant to be an easily readable language. Its formatting is visually uncluttered, and it often uses English keywords where other languages use punctuation. Unlike many other languages, it does not use curly brackets to delimit blocks, and semicolons after statements are allowed but are rarely, if ever, used. It has fewer syntactic exceptions and special cases than C or Pascal.[75]

Hello world program:
print('Hello, world!')
Program to calculate the factorial of a positive integer:

n = int(input('Type a number, and its factorial will be printed: '))

if n < 0: raise ValueError('You must enter a non negative integer')

factorial = 1 for i in range(2, n + 1): factorial *= i

print(factorial)

Development
Python's development is conducted largely through the Python Enhancement Proposal (PEP) process, the primary mechanism for proposing major new features, collecting community input on issues and documenting Python design decisions.[151] Python coding style is covered in PEP 8.[152] Outstanding PEPs are reviewed and commented on by the Python community and the steering council.[151]

Enhancement of the language corresponds with development of the CPython reference implementation. The mailing list python-dev is the primary forum for the language's development. Specific issues are discussed in the Roundup bug tracker hosted at bugs.python.org.[153] Development originally took place on a self-hosted source-code repository running Mercurial, until Python moved to GitHub in January 2017.[154]

CPython's public releases come in three types, distinguished by which part of the version number is incremented:

Backward-incompatible versions, where code is expected to break and needs to be manually ported. The first part of the version number is incremented. These releases happen infrequently—version 3.0 was released 8 years after 2.0. Major or "feature" releases, occurred about every 18 months but with the adoption of a yearly release cadence starting with Python 3.9 are expected to happen once a year.[155][156] They are largely compatible but introduce new features. The second part of the version number is incremented. Each major version is supported by bugfixes for several years after its release.[157] Bugfix releases,[158] which introduce no new features, occur about every 3 months and are made when a sufficient number of bugs have been fixed upstream since the last release. Security vulnerabilities are also patched in these releases. The third and final part of the version number is incremented.[158] Many alpha, beta, and release-candidates are also released as previews and for testing before final releases. Although there is a rough schedule for each release, they are often delayed if the code is not ready. Python's development team monitors the state of the code by running the large unit test suite during development.[159]

The major academic conference on Python is PyCon. There are also special Python mentoring programmes, such as Pyladies.

Pythons 3.10 deprecates wstr (to be removed in Python 3.12; meaning Python extensions[160] need to be modified by then),[161] and also plans to add pattern matching to the language.[162]
