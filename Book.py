# --- Code adapted from the PyPi module chapterize ---

import re

class Book():
    def __init__(self, text):
        self.contents = text
        self.lines = self.getLines()
        self.headingLocations = self.getHeadings()
        self.discard_too_short()
        self.chapters = self.getTextBetweenHeadings()
        self.numChapters = len(self.chapters)

    def getLines(self):
        """
        Breaks the book into lines.
        """
        return self.contents.split('\n')
    
    def getEndLocation(self):
        """
        Find where the book ends (to cut off the unuseful text at the end).
        """
        ends = ["End of the Project Gutenberg EBook",
                "End of Project Gutenberg's",
                "\*\*\*END OF THE PROJECT GUTENBERG EBOOK",
                "\*\*\* END OF THIS PROJECT GUTENBERG EBOOK"]
        joined = '|'.join(ends)
        pat = re.compile(joined, re.IGNORECASE)
        endLocation = None
        for line in self.lines:
            if pat.match(line) is not None:
                endLocation = self.lines.index(line)
                self.endLine = self.lines[endLocation]
                break
        if endLocation is None: # Can't find the "real" ending
            endLocation = len(self.lines)-1 # The end is the last character
            self.endLine = 'None'
        return endLocation

    def getHeadings(self):
        """
        Gets the heading locations.
        """
        # Form 1: Chapter I, Chapter 1, Chapter the First, CHAPTER 1
        arabicNumerals = '\d+'
        romanNumerals = '(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})'
        numberWordsByTens = ['twenty', 'thirty', 'forty', 'fifty', 'sixty',
                              'seventy', 'eighty', 'ninety']
        numberWords = ['one', 'two', 'three', 'four', 'five', 'six',
                       'seven', 'eight', 'nine', 'ten', 'eleven',
                       'twelve', 'thirteen', 'fourteen', 'fifteen',
                       'sixteen', 'seventeen', 'eighteen', 'nineteen'] + numberWordsByTens
        numberWordsPat = '(' + '|'.join(numberWords) + ')'
        ordinalNumberWordsByTens = ['twentieth', 'thirtieth', 'fortieth', 'fiftieth', 
                                    'sixtieth', 'seventieth', 'eightieth', 'ninetieth'] + \
                                    numberWordsByTens
        ordinalNumberWords = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 
                              'seventh', 'eighth', 'ninth', 'twelfth', 'last'] + \
                             [numberWord + 'th' for numberWord in numberWords] + ordinalNumberWordsByTens
        ordinalsPat = '(the )?(' + '|'.join(ordinalNumberWords) + ')'
        enumeratorsList = [arabicNumerals, romanNumerals, numberWordsPat, ordinalsPat] 
        enumerators = '(' + '|'.join(enumeratorsList) + ')'
        form1 = 'chapter ' + enumerators

        # Form 2: II. The Mail
        enumerators = romanNumerals
        separators = '(\. | )'
        titleCase = '[A-Z][a-z]'
        form2 = enumerators + separators + titleCase

        # Form 3: II. THE OPEN ROAD
        enumerators = romanNumerals
        separators = '(\. )'
        titleCase = '[A-Z][A-Z]'
        form3 = enumerators + separators + titleCase

        # Form 4: a number on its own, e.g. 8, VIII
        arabicNumerals = '^\d+\.?$'
        romanNumerals = '(?=[MDCLXVI])M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})\.?$'
        enumeratorsList = [arabicNumerals, romanNumerals]
        enumerators = '(' + '|'.join(enumeratorsList) + ')'
        form4 = enumerators

        pat = re.compile(form1, re.IGNORECASE)
        pat2 = re.compile('(%s|%s|%s)' % (form2, form3, form4))

        headings = []
        for i, line in enumerate(self.lines):
            if pat.match(line) is not None:
                headings.append(i)
            if pat2.match(line) is not None:
                headings.append(i)

        self.endLocation = self.getEndLocation()
        headings.append(self.endLocation)

        return headings

    def discard_too_short(self):
        """
        Filters headings out that are too close together,
        since they probably belong to a table of contents.
        """
        pairs = zip(self.headingLocations, self.headingLocations[1:])
        toBeDeleted = []
        for pair in pairs:
            delta = pair[1] - pair[0]
            if delta < 10:
                if pair[0] not in toBeDeleted:
                    toBeDeleted.append(pair[0])
                if pair[1] not in toBeDeleted:
                    toBeDeleted.append(pair[1])
        for badLoc in toBeDeleted:
            index = self.headingLocations.index(badLoc)
            del self.headingLocations[index]

    def getTextBetweenHeadings(self):
        chapters = []
        lastHeading = len(self.headingLocations) - 1
        for i, headingLocation in enumerate(self.headingLocations):
            if i != lastHeading:
                nextHeadingLocation = self.headingLocations[i+1]
                chapters.append(self.lines[headingLocation+1:nextHeadingLocation])
        return chapters
    
    def rebuild_chapters(self):
        return ["".join(c) for c in self.chapters]
